#!/usr/bin/env python3
"""Resuelve las redirecciones de Joomla (weblink.go) y lista todos los enlaces externos del HTML completo.

Salida: migracion/origen/enlaces.json
    weblinks: id -> {titulo, categoria, destino (Location exacto), destino_final, status}
    externos: href exacto -> [páginas donde aparece] (incluye menús, barras laterales y pie)
"""
import glob
import html
import json
import pathlib
import re
import time

import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORIG = ROOT / "migracion" / "origen"
BASE = "https://www.fernandomartinez.mx"
UA = {"User-Agent": "fm-migracion/1.0"}

weblinks, externos = {}, {}
for f in sorted(glob.glob(str(ORIG / "paginas" / "*.html"))):
    name = pathlib.Path(f).name
    soup = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
    for a in soup.find_all("a", href=True):
        h = html.unescape(a["href"]).strip()
        m = re.search(r"task=weblink\.go.*?[&?]id=(\d+)", h)
        if m:
            wid = m.group(1)
            w = weblinks.setdefault(wid, {"href_joomla": h, "titulo": a.get_text(" ", strip=True), "paginas": []})
            if not w["titulo"]:
                w["titulo"] = a.get_text(" ", strip=True)
            cat = re.search(r"catid=\d+:([\w-]+)", h)
            if cat:
                w["categoria"] = cat.group(1)
            if name not in w["paginas"]:
                w["paginas"].append(name)
        elif re.match(r"(?i)https?://", h) and "fernandomartinez.mx" not in h:
            externos.setdefault(h, [])
            if name not in externos[h]:
                externos[h].append(name)
    # descripción del weblink en la página de categoría
    for item in soup.select(".list-title, li, tr"):
        a = item.find("a", href=re.compile("weblink.go"))
        if not a:
            continue
        m = re.search(r"[&?]id=(\d+)", html.unescape(a["href"]))
        desc = item.select_one(".weblink-description, p")
        if m and desc and m.group(1) in weblinks and not weblinks[m.group(1)].get("descripcion"):
            weblinks[m.group(1)]["descripcion"] = desc.get_text(" ", strip=True)

s = requests.Session()
s.headers.update(UA)
for wid, w in sorted(weblinks.items(), key=lambda x: int(x[0])):
    url = BASE + "/enlaces-recomendados?task=weblink.go&id=" + wid
    try:
        r = s.get(url, allow_redirects=False, timeout=30)
        w["status"] = r.status_code
        w["destino"] = r.headers.get("Location")
        if w["destino"]:
            try:
                f = s.get(w["destino"], timeout=20, allow_redirects=True)
                w["destino_final"] = f.url
                w["destino_status"] = f.status_code
            except Exception as e:  # noqa: BLE001
                w["destino_error"] = str(e)[:150]
    except Exception as e:  # noqa: BLE001
        w["error"] = str(e)[:150]
    print(wid, w.get("status"), w.get("destino"), "->", w.get("destino_status"))
    time.sleep(0.2)

# Estado de los externos directos
for h in list(externos):
    try:
        r = s.get(h, timeout=20, allow_redirects=True)
        externos[h] = {"paginas": externos[h], "status": r.status_code, "final": r.url}
    except Exception as e:  # noqa: BLE001
        externos[h] = {"paginas": externos[h], "error": str(e)[:150]}

(ORIG / "enlaces.json").write_text(json.dumps({"weblinks": weblinks, "externos": externos}, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"weblinks: {len(weblinks)}  externos: {len(externos)}")
