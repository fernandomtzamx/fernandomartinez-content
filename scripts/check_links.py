#!/usr/bin/env python3
"""Verificación después de publicar. Escribe registro/verificacion.md.

1. Cada página y entrada de content/ responde 200 en el sitio publicado.
2. Los enlaces de referido aparecen exactos y con rel="sponsored" en el HTML publicado.
3. Estado de todos los enlaces externos del contenido (avisos, no bloquea).
"""
import os
import pathlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor

import requests
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lint import REFERRALS  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0 (compatible; fm-verificador/1.0)"}
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sitio_url import base_url  # noqa: E402
base = base_url()
base = requests.get(base.rstrip("/") + "/wp-json/", timeout=30, headers=UA).json().get("home", base).rstrip("/")

items, externos = [], {}
for p in sorted((ROOT / "content").rglob("*.md")):
    _, fm, body = p.read_text(encoding="utf-8").split("---", 2)
    m = yaml.safe_load(fm) or {}
    if m.get("type") == "page":
        path = "/" if m["slug"] == "inicio" else (f"/{m['parent']}/{m['slug']}/" if m.get("parent") else f"/{m['slug']}/")
    else:
        path = f"/blog/{m['slug']}/"
    items.append((p.relative_to(ROOT), path, body))
    for u in re.findall(r"\]\((https?://[^)\s]+)\)", body):
        externos.setdefault(u, set()).add(str(p.relative_to(ROOT)))


def get(url):
    try:
        r = requests.get(url, timeout=25, headers=UA, allow_redirects=True)
        return r.status_code, r.url, r.text
    except Exception as e:  # noqa: BLE001
        return None, str(e)[:80], ""


lines, bad = [f"# Verificación de {base}", ""], 0
lines += ["## Páginas publicadas", "", "| Estado | URL | Archivo | Referidos |", "|---|---|---|---|"]
with ThreadPoolExecutor(8) as ex:
    results = list(ex.map(lambda it: (it, get(base + it[1])), items))
for (f, path, body), (code, final, text) in results:
    ref_note = ""
    for host, allowed in REFERRALS.items():
        if host in body:
            tags = re.findall(r"<a\s[^>]*" + re.escape(host) + r"[^>]*>", text)
            ok = [t for t in tags if any(f'href="{a}"' in t for a in allowed) and "sponsored" in t]
            ref_note = f"{len(ok)}/{len(tags)} ok" if tags else "NO ENCONTRADO"
            if not tags or len(ok) != len(tags):
                bad += 1
    if code != 200:
        bad += 1
    lines.append(f"| {code} | {base}{path} | {f} | {ref_note} |")

lines += ["", "## Enlaces externos", "", "| Estado | URL | Final | Dónde |", "|---|---|---|---|"]
with ThreadPoolExecutor(8) as ex:
    ext = list(ex.map(lambda u: (u, get(u)), sorted(externos)))
for u, (code, final, _) in ext:
    flag = "" if code and code < 400 else " ⚠"
    shown_final = final if final != u else ""
    lines.append(f"| {code}{flag} | {u} | {shown_final} | {', '.join(sorted(externos[u]))[:80]} |")

out = ROOT / "registro" / "verificacion.md"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[:4]))
print(f"Problemas en páginas o referidos: {bad}. Externos con error: {sum(1 for _, (c, _, _) in ext if not c or c >= 400)}")
sys.exit(1 if bad else 0)
