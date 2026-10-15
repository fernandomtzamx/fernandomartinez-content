#!/usr/bin/env python3
"""Puerta de calidad antes de publicar. Uso: python scripts/lint.py [archivos.md] (sin argumentos: todo content/)

Errores (bloquean): frontmatter incompleto, guion largo o medio, enlace interno a una URL que no existe
en el repo, archivo local inexistente, enlace de referido alterado o sin aviso de afiliado, portada faltante.
SEO (errores): seo_title y seo_description obligatorios; título para Google de más de 62 caracteres
con la marca; descripción fuera de 120 a 158 caracteres; seo_title repetido en otro archivo.
Avisos: entradas cortas, pocas fuentes, extracto fuera de rango, título largo.
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
REQ = ["title", "slug", "type", "status", "excerpt", "seo_title", "seo_description", "focus_keyword"]
MARCA = " | Fernando Martínez"
# Referidos conocidos: URL exacta (ver migracion/origen/enlaces.json, weblink id=100)
REFERRALS = {"shopify.pxf.io": ["https://shopify.pxf.io/prueba-gratis-shop"]}
# Parámetros permitidos sobre el enlace base: deep link (u) y medición de impact.com.
REFERRAL_PARAMS = {"u", "subId1", "subId2", "subId3", "sharedid"}
# Dominios a los que se permite hacer deep link con u=.
DEEPLINK_HOSTS = ("shopify.com",)


def referral_ok(u, allowed):
    """El enlace base exacto, opcionalmente con u= hacia un dominio permitido y Sub IDs."""
    from urllib.parse import urlsplit, parse_qsl
    base, _, query = u.partition("?")
    if base not in allowed:
        return False
    if not query:
        return True
    params = parse_qsl(query, keep_blank_values=True)
    names = [k for k, _ in params]
    if len(names) != len(set(names)) or not set(names) <= REFERRAL_PARAMS:
        return False
    for k, v in params:
        if not v:
            return False
        if k == "u":
            dest = urlsplit(v)
            host = (dest.hostname or "").lower()
            if dest.scheme != "https" or not any(host == h or host.endswith("." + h) for h in DEEPLINK_HOSTS):
                return False
        elif k == "sharedid" and not v.isalnum():
            return False
    return True


def load(p):
    text = p.read_text(encoding="utf-8")
    _, fm, body = text.split("---", 2)
    return text, yaml.safe_load(fm) or {}, body


def url_index():
    """Rutas públicas que existirán en el sitio: /slug/, /padre/slug/, /blog/slug/."""
    urls = {"/", "/blog/"}
    for p in CONTENT.rglob("*.md"):
        _, m, _ = load(p)
        if m.get("type") == "page":
            if m.get("slug") == "inicio":
                continue
            urls.add(f"/{m['parent']}/{m['slug']}/" if m.get("parent") else f"/{m['slug']}/")
        else:
            urls.add(f"/blog/{m['slug']}/")
    return urls


def check(p, urls):
    errs, warns = [], []
    text, meta, body = load(p)
    for k in REQ:
        if not meta.get(k):
            errs.append(f"falta '{k}'")
    if "—" in text or "–" in text:
        errs.append("contiene guion largo o medio")
    for target in re.findall(r"\]\((/[^)\s]*)\)|href=\"(/[^\"]*)\"", body):
        t = next(x for x in target if x).split("#")[0]
        if not t.endswith("/"):
            t += "/"
        if t not in urls:
            errs.append(f"enlace interno inexistente: {t}")
    for f in re.findall(r"(?:\]\(|src=\")((?:assets|images)/[^)\"\s]+)", body) + ([meta["featured_image"]] if meta.get("featured_image") else []):
        if not (ROOT / f).exists():
            errs.append(f"archivo inexistente: {f}")
    for host, allowed in REFERRALS.items():
        found = re.findall(rf"https?://{re.escape(host)}[^)\"\s]*", body)
        for u in found:
            if not referral_ok(u, allowed):
                errs.append(f"enlace de referido alterado: {u}")
        if found and 'class="fm-ref"' not in body:
            errs.append("tiene enlace de referido pero no el aviso de afiliado (fm-ref)")
    for u in re.findall(r"https?://(?:[a-z0-9-]+\.)*shopify\.com[^)\"\s]*", body, re.I):
        errs.append(f"enlace directo a Shopify sin afiliado (usa el deep link con ?u=): {u}")
    plain = re.sub(r"\([^)]*\)|<[^>]+>|```.*?```|\[TOC\]|[#*|`>\[\]]", " ", body, flags=re.S)
    words = len(plain.split())
    sources = len(re.findall(r"\]\(https?://", body))
    if meta.get("type") == "post":
        if not meta.get("featured_image"):
            errs.append("entrada sin portada")
        if words < 450:
            warns.append(f"corta ({words} palabras)")
    if len(str(meta.get("title", ""))) > 90:
        warns.append("título de más de 90 caracteres")
    st = str(meta.get("seo_title") or "")
    full = st if ("Fernando" in st and "Martínez" in st) else st + MARCA
    if st and len(full) > 62:
        errs.append(f"título para Google de {len(full)} caracteres con la marca (máximo 62): {full}")
    sd = len(str(meta.get("seo_description") or ""))
    if sd and not 120 <= sd <= 158:
        errs.append(f"seo_description de {sd} caracteres (120 a 158)")
    ex = len(str(meta.get("excerpt", "")))
    if not 110 <= ex <= 175:
        warns.append(f"extracto de {ex} caracteres (ideal 140 a 160)")
    return words, sources, errs, warns


def main():
    files = [pathlib.Path(f) for f in sys.argv[1:]] or sorted(CONTENT.rglob("*.md"))
    urls = url_index()
    slugs = {}
    seo_titles = {}
    bad = 0
    for p in files:
        words, sources, errs, warns = check(p, urls)
        meta = load(p)[1]
        key = (meta.get("type"), meta.get("parent"), meta.get("slug"))
        if key in slugs:
            errs.append(f"slug duplicado con {slugs[key]}")
        slugs[key] = p.name
        st = str(meta.get("seo_title") or "").lower()
        if st and st in seo_titles:
            errs.append(f"seo_title repetido con {seo_titles[st]}")
        seo_titles[st] = p.name
        print(f"{'ERROR' if errs else 'ok':5} {p.relative_to(ROOT)}: {words} palabras, {sources} fuentes")
        for e in errs:
            print(f"      x {e}")
        for w in warns:
            print(f"      ! {w}")
        bad += bool(errs)
    print(f"\n{len(files)} archivos, {bad} con errores")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
