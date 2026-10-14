#!/usr/bin/env python3
"""Texto alternativo (alt) de todas las imágenes.

1. Biblioteca de medios: toda imagen sin alt_text recibe uno (el featured_alt de la entrada que la usa
   como portada, o un texto derivado de su título). Con --fix lo escribe; sin él solo reporta.
2. HTML publicado: revisa cada <img> de cada página, entrada, listado y categoría. Un alt vacío o
   ausente es error (salvo imágenes decorativas marcadas con role="presentation" o aria-hidden).
Escribe registro/alt.md. Sale con 1 si queda alguna imagen sin alt en el HTML.
"""
import pathlib
import re
import sys
from html.parser import HTMLParser

import requests
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from publish import WP, env  # noqa: E402

FIX = "--fix" in sys.argv
wp = WP(env("WP_URL"), env("WP_USER"), env("WP_APP_PASSWORD"))
UA = {"User-Agent": "Mozilla/5.0 (compatible; fm-alt/1.0)"}

# alt deseado por nombre de archivo de portada
alts, urls = {}, ["/", "/blog/", "/blog/page/2/", "/blog/page/3/"]
for p in (ROOT / "content").rglob("*.md"):
    m = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1]) or {}
    if m.get("featured_image"):
        alts[pathlib.Path(m["featured_image"]).stem.lower()] = m.get("featured_alt") or m["title"]
    if m.get("type") == "page":
        if m["slug"] != "inicio":
            urls.append(f"/{m['parent']}/{m['slug']}/" if m.get("parent") else f"/{m['slug']}/")
    else:
        urls.append(f"/blog/{m['slug']}/")
for c in wp.req("GET", "categories", params={"per_page": 100}):
    if c.get("count"):
        urls.append(c["link"].replace(wp.home, ""))

# 1. Biblioteca de medios
lines = ["# Texto alternativo de las imágenes", "", "## Biblioteca de medios", ""]
page, fixed, missing = 1, [], []
while True:
    r = wp.s.get(f"{wp.api}/media", params={"per_page": 100, "page": page, "context": "edit", "media_type": "image"}, timeout=30)
    if r.status_code != 200:
        break
    items = r.json()
    if not items:
        break
    for it in items:
        if (it.get("alt_text") or "").strip():
            continue
        stem = pathlib.Path(it.get("source_url", "")).stem.lower()
        base = re.sub(r"-(\d+|scaled|e\d+)$", "", stem)
        alt = alts.get(base) or alts.get(stem)
        if not alt:
            title = (it.get("title") or {}).get("raw") or base
            alt = re.sub(r"[-_]+", " ", title).strip().capitalize()
            if base.startswith("fernando-martinez"):
                alt = "Fernando Martínez"
        if FIX:
            wp.req("POST", f"media/{it['id']}", json={"alt_text": alt})
            fixed.append((it["id"], stem, alt))
        else:
            missing.append((it["id"], stem, alt))
    if page >= int(r.headers.get("X-WP-TotalPages", 1)):
        break
    page += 1
lines.append(f"- Imágenes que no tenían alt y {'se corrigieron' if FIX else 'necesitan uno'}: **{len(fixed) or len(missing)}**")
for mid, stem, alt in fixed or missing:
    lines.append(f"  - {mid} `{stem}`: {alt}")


# 2. HTML publicado
class Imgs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imgs = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            self.imgs.append(dict(attrs))


problems, total = [], 0
for u in sorted(set(urls)):
    r = requests.get(wp.home + u, timeout=30, headers=UA)
    if r.status_code != 200:
        continue
    parser = Imgs()
    parser.feed(r.text)
    for a in parser.imgs:
        src = a.get("src", "")
        if src.startswith("data:") or "s.w.org/images/core/emoji" in src:
            continue
        total += 1
        decorative = a.get("role") == "presentation" or a.get("aria-hidden") == "true"
        if not (a.get("alt") or "").strip() and not decorative:
            problems.append((u, src[-80:]))
lines += ["", "## HTML publicado", "", f"- Páginas revisadas: **{len(set(urls))}**", f"- Imágenes revisadas: **{total}**",
          f"- Sin alt: **{len(problems)}**"]
lines += [f"  - {u}: `{s}`" for u, s in problems]
out = ROOT / "registro" / "alt.md"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
sys.exit(1 if problems else 0)
