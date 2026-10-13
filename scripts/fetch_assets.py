#!/usr/bin/env python3
"""Descarga del sitio actual las imágenes y archivos referenciados por las páginas exportadas.

Guarda en assets/origen/<ruta original> y escribe assets/origen/manifest.json.
Excluye la galería de Phoca (imágenes libres) y los recursos de la plantilla.
"""
import glob
import html
import json
import pathlib
import re

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORIG = ROOT / "migracion" / "origen" / "paginas"
OUT = ROOT / "assets" / "origen"
BASE = "https://www.fernandomartinez.mx"

refs = {}
for f in glob.glob(str(ORIG / "*.html")):
    if "imagenes-libres" in f:
        continue
    t = html.unescape(open(f, encoding="utf-8").read())
    for m in re.findall(r'(?:src|href|data-src|content)=["\']?((?:https?://(?:www\.)?fernandomartinez\.mx)?/(?:images|media/weTnwLzC8MAT47xS)/[^"\'\s>)]+)', t):
        path = re.sub(r"^https?://(?:www\.)?fernandomartinez\.mx", "", m).split("?")[0]
        if re.search(r"\.(png|jpe?g|gif|webp|svg|pdf|zip)$", path, re.I) and "/phocadownload" not in path:
            refs.setdefault(path, set()).add(pathlib.Path(f).name)

s = requests.Session()
s.headers["User-Agent"] = "fm-migracion/1.0"
manifest = {}
for path in sorted(refs):
    dest = OUT / path.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        r = s.get(BASE + path, timeout=60)
        if r.ok:
            dest.write_bytes(r.content)
        manifest[path] = {"status": r.status_code, "bytes": len(r.content), "paginas": sorted(refs[path])[:10]}
    except Exception as e:  # noqa: BLE001
        manifest[path] = {"error": str(e)[:150]}
    print(manifest[path].get("status"), path)

(OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(manifest)} archivos")
