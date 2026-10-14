#!/usr/bin/env python3
"""Prueba migracion/redirecciones.htaccess en un Apache real (localhost) contra todas las URLs conocidas
del sitio Joomla y verifica que cada destino responda 200 en el WordPress publicado.

Fuentes de URLs viejas: rastreo (inventario.json), robots.txt y sitemaps XML del sitio actual (si existen),
mapa del sitio HTML, los 100 enlaces del directorio, archivos descargables y variantes típicas de Joomla.
Escribe registro/redirecciones.md. Sale con 1 si alguna URL viva no tiene equivalente.
"""
import json
import os
import pathlib
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOCAL = "http://127.0.0.1"
OLD = "https://www.fernandomartinez.mx"
UA = {"User-Agent": "Mozilla/5.0 (compatible; fm-redirecciones/1.0)"}
inv = json.loads((ROOT / "migracion/origen/inventario.json").read_text(encoding="utf-8"))
enl = json.loads((ROOT / "migracion/origen/enlaces.json").read_text(encoding="utf-8"))
new_base = os.environ["WP_URL"].rstrip("/")
new_base = requests.get(new_base + "/wp-json/", timeout=30, headers=UA).json().get("home", new_base).rstrip("/")

# ---------- 1. URLs viejas ----------
urls = {}  # ruta+query -> origen


def add(u, src):
    p = urlparse(u)
    if p.netloc and "fernandomartinez.mx" not in p.netloc:
        return
    path = (p.path or "/") + (f"?{p.query}" if p.query else "")
    urls.setdefault(path, src)


for u, r in inv.items():
    if r.get("status") == 200:
        add(u, "rastreo")

# Sitemaps del sitio actual
sitemaps = []
try:
    robots = requests.get(OLD + "/robots.txt", timeout=30, headers=UA).text
    sitemaps += re.findall(r"(?im)^sitemap:\s*(\S+)", robots)
except Exception:  # noqa: BLE001
    robots = ""
for cand in ["/sitemap.xml", "/sitemap_index.xml", "/index.php?option=com_osmap&view=xml&id=1",
             "/component/osmap/?view=xml&id=1", "/index.php?option=com_xmap&view=xml&id=1",
             "/component/xmap/?view=xml&id=1", "/index.php?option=com_jmap&view=sitemap&format=xml"]:
    sitemaps.append(OLD + cand)
sitemap_report = []
seen_sm = set()
while sitemaps:
    sm = sitemaps.pop(0)
    if sm in seen_sm:
        continue
    seen_sm.add(sm)
    try:
        r = requests.get(sm, timeout=30, headers=UA)
        locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text) if r.ok else []
    except Exception as e:  # noqa: BLE001
        r, locs = None, []
    sitemap_report.append((sm, r.status_code if r is not None else None, len(locs)))
    for loc in locs:
        if loc.endswith(".xml") or "view=xml" in loc:
            sitemaps.append(loc)
        else:
            add(loc, "sitemap")

# Mapa del sitio HTML
for h in re.findall(r'href="?(/[^" >]*)', (ROOT / "migracion/origen/paginas/mapa-de-sitio.html").read_text(encoding="utf-8")):
    if not h.startswith(("/images", "/media", "/templates", "/cdn-cgi")):
        add(h, "mapa-de-sitio")

# Directorio de enlaces (ambas formas de URL de Joomla)
for wid, w in enl["weblinks"].items():
    add(f"/enlaces-recomendados?task=weblink.go&id={wid}", "weblink")
    h = w.get("href_joomla", "")
    if h.startswith("/component/"):
        add(h, "weblink")

# Descargables y variantes de Joomla
for f in ["/media/weTnwLzC8MAT47xS/plg_websitepreloader.zip", "/media/weTnwLzC8MAT47xS/plg_TwitterSummaryCardforArticles.zip",
          "/media/weTnwLzC8MAT47xS/25_cosas_que_hacer_en_la_web_para_tener_mas_trafico_y_clientes.pdf"]:
    add(f, "descarga")
base_paths = [p for p in list(urls) if "?" not in p]
for p in base_paths:
    if p != "/":
        add("/index.php" + p, "variante index.php")
        add(p + "/", "variante con diagonal")
add("/blog?format=feed&type=rss", "variante feed")
add("/index.php", "variante index.php")

# ---------- 2. Probar en Apache local ----------
def follow_local(path):
    hops, cur = [], path
    for _ in range(6):
        r = requests.get(LOCAL + cur, allow_redirects=False, timeout=15)
        if r.status_code not in (301, 302, 307, 308):
            return hops, cur, None
        loc = r.headers["Location"]
        hops.append(loc)
        p = urlparse(loc)
        if p.netloc and p.netloc not in ("127.0.0.1", "localhost"):
            return hops, None, loc  # destino externo
        cur = (p.path or "/") + (f"?{p.query}" if p.query else "")
    return hops, cur, "BUCLE"


def check(item):
    path, src = item
    hops, final_path, external = follow_local(path)
    res = {"vieja": path, "origen": src, "saltos": len(hops)}
    if external == "BUCLE":
        res.update(estado="ERROR", detalle="bucle de redirecciones")
        return res
    if external:
        res.update(destino=external)
        ok = external.startswith("https://shopify.pxf.io/prueba-gratis-shop")
        res.update(estado="ok" if ok else "REVISAR", detalle="externo")
        return res
    dest = final_path.split("?")[0]
    res["destino"] = dest
    try:
        r = requests.get(new_base + dest, timeout=25, headers=UA, allow_redirects=True)
        final = urlparse(r.url).path
        expected = urlparse(new_base + dest).path
        same = final.rstrip("/") == expected.rstrip("/")
        res["http"] = r.status_code
        if r.status_code == 200 and same:
            res["estado"] = "ok"
        elif r.status_code == 200:
            res.update(estado="REVISAR", detalle=f"WordPress además redirige a {final}")
        else:
            res.update(estado="ERROR", detalle=f"destino {r.status_code}")
    except Exception as e:  # noqa: BLE001
        res.update(estado="ERROR", detalle=str(e)[:80])
    return res


with ThreadPoolExecutor(8) as ex:
    results = list(ex.map(check, sorted(urls.items())))

# ---------- 3. Reporte ----------
errs = [r for r in results if r["estado"] == "ERROR"]
rev = [r for r in results if r["estado"] == "REVISAR"]
lines = [f"# Prueba de redirecciones: Apache local con migracion/redirecciones.htaccess, destinos en {new_base}", "",
         f"- URLs viejas probadas: **{len(results)}**",
         f"- Correctas (301 a una página que responde 200, o URL que se conserva igual): **{len(results) - len(errs) - len(rev)}**",
         f"- Para revisar: **{len(rev)}**", f"- Sin equivalente o con error: **{len(errs)}**", "",
         "## Sitemaps del sitio actual", "", "| Sitemap | HTTP | URLs |", "|---|---|---|"]
lines += [f"| {s} | {c} | {n} |" for s, c, n in sitemap_report]
lines += ["", "## Errores y casos a revisar", "", "| Estado | URL vieja | Origen | Destino | Detalle |", "|---|---|---|---|---|"]
lines += [f"| {r['estado']} | {r['vieja']} | {r['origen']} | {r.get('destino', '')} | {r.get('detalle', '')} |" for r in errs + rev]
lines += ["", "## Todas", "", "| Estado | URL vieja | Origen | Saltos | Destino |", "|---|---|---|---|---|"]
lines += [f"| {r['estado']} | {r['vieja']} | {r['origen']} | {r['saltos']} | {r.get('destino', '')} |" for r in results]
out = ROOT / "registro" / "redirecciones.md"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[:16]))
sys.exit(1 if errs else 0)
