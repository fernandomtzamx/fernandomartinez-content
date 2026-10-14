#!/usr/bin/env python3
"""Genera migracion/redirecciones.htaccess: URLs del sitio Joomla -> URLs nuevas (301).

Se usa al migrar a la raíz www.fernandomartinez.mx: pegar ANTES del bloque de WordPress en .htaccess.
Requiere la estructura de enlaces permanentes /blog/%postname%/.
"""
import json
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
inv = json.loads((ROOT / "migracion" / "origen" / "inventario.json").read_text(encoding="utf-8"))
enl = json.loads((ROOT / "migracion" / "origen" / "enlaces.json").read_text(encoding="utf-8"))

rules = {}
for p in (ROOT / "content").rglob("*.md"):
    m = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1]) or {}
    if m.get("original"):
        rules[m["original"]] = f"/blog/{m['slug']}/"

fijas = {
    "/temas": "/blog/",
    "/mapa-de-sitio": "/",
    "/base-de-conocimiento": "/recursos/",
    "/busqueda": "/blog/",
    "/enlaces-recomendados": "/recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/",
    "/usuario/inicio-de-sesion": "/",
    "/usuario/registro": "/",
    "/recursos/11-imagenes-libres-de-derechos-gratis": "/recursos/imagenes-libres-de-derechos-gratis/",
}
rules.update(fijas)

out = ["# Redirecciones 301 del sitio Joomla a WordPress (generado por scripts/redirects.py)",
       "# Pegar ANTES de '# BEGIN WordPress' en el .htaccess de la raíz.",
       "<IfModule mod_rewrite.c>", "RewriteEngine On", ""]
out.append("# Variantes de Joomla: /index.php/ruta y feeds RSS (?format=feed)")
out.append("RewriteRule ^index\\.php/(.+)$ /$1 [R=301,L]")
out.append("RewriteCond %{QUERY_STRING} (^|&)format=feed")
out.append("RewriteRule ^ /feed/? [R=301,L]")
out.append("")
out.append("# Directorio de enlaces: el referido de Shopify conserva su destino exacto")
for wid, w in sorted(enl["weblinks"].items(), key=lambda x: int(x[0])):
    if "pxf.io" in (w.get("destino") or ""):
        out.append(f"RewriteCond %{{QUERY_STRING}} (^|&)task=weblink\\.go.*(^|&)id={wid}([:&]|$)")
        out.append(f"RewriteRule ^(enlaces-recomendados|component/weblinks)/?$ {w['destino']}? [R=301,L]")
out.append("RewriteCond %{QUERY_STRING} (^|&)task=weblink\\.go")
out.append("RewriteRule ^(enlaces-recomendados|component/weblinks)/?$ /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/? [R=301,L]")
out.append("")
out.append("# Paginación del blog y categorías de Joomla")
out.append("RewriteCond %{QUERY_STRING} (^|&)start=")
out.append("RewriteRule ^blog/?$ /blog/? [R=301,L]")
out.append("RewriteRule ^temas/.+$ /blog/ [R=301,L]")
out.append("RewriteRule ^enlaces-recomendados/.+$ /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ [R=301,L]")
out.append("RewriteRule ^component/tags/.*$ /blog/ [R=301,L]")
out.append("RewriteRule ^recursos/imagenes-libres-de-derechos-gratis/.+$ /recursos/imagenes-libres-de-derechos-gratis/ [R=301,L]")
out.append("")
out.append("# Entradas y páginas")
for old, new in sorted(rules.items()):
    out.append(f"RewriteRule ^{old.lstrip('/').replace('.', '\\.')}/?$ {new} [R=301,L]")
out.append("")
out.append("# Archivos descargables que cambian de ruta (actualizar con la URL final de la biblioteca de medios)")
out.append("# /media/weTnwLzC8MAT47xS/plg_websitepreloader.zip -> /recursos/website-preloader-joomla-plugin/")
out.append("RewriteRule ^media/weTnwLzC8MAT47xS/plg_websitepreloader\\.zip/?$ /recursos/website-preloader-joomla-plugin/ [R=301,L]")
out.append("RewriteRule ^media/weTnwLzC8MAT47xS/plg_TwitterSummaryCardforArticles\\.zip/?$ /recursos/twitter-summary-card-for-joomla-articles-plugin/ [R=301,L]")
out.append("RewriteRule ^media/weTnwLzC8MAT47xS/25_cosas.*\\.pdf/?$ /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ [R=301,L]")
out.append("</IfModule>")

dest = ROOT / "migracion" / "redirecciones.htaccess"
dest.write_text("\n".join(out) + "\n", encoding="utf-8")
old_urls = [u.replace("https://www.fernandomartinez.mx", "") for u, r in inv.items() if r.get("status") == 200]
print(f"{len(rules)} reglas puntuales; {len(old_urls)} URLs 200 en el sitio viejo")
