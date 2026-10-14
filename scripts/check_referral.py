#!/usr/bin/env python3
"""Sigue el enlace de afiliado de Shopify salto por salto y verifica que llegue a Shopify con el
identificador de afiliado. También revisa que el sitio publicado lo enlace exacto y con rel="sponsored".
Escribe registro/shopify.md. Sale con 1 si algo falla."""
import os
import pathlib
import re
import sys
from urllib.parse import parse_qs, urlparse

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
MASK = "https://shopify.pxf.io/prueba-gratis-shop"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36",
      "Accept-Language": "es-MX,es;q=0.9"}

hops, url, ok = [], MASK, True
s = requests.Session()
for _ in range(10):
    r = s.get(url, allow_redirects=False, timeout=30, headers=UA)
    loc = r.headers.get("Location")
    hops.append((r.status_code, url, loc))
    if r.status_code in (301, 302, 303, 307, 308) and loc:
        url = loc if loc.startswith("http") else requests.compat.urljoin(url, loc)
        continue
    break
final = url
q = parse_qs(urlparse(final).query)
checks = {
    "La máscara responde y redirige": hops[0][0] in (301, 302, 303, 307, 308),
    "Llega a shopify.com": urlparse(final).netloc.endswith("shopify.com"),
    "Página final responde 200": hops[-1][0] == 200,
    "Lleva el ID de afiliado (partner / utm_source)": bool(q.get("partner") or any("impact" in v for v in q.get("utm_source", []))),
    "Lleva el identificador de clic de impact (irclickid)": "irclickid" in q,
}

base = os.environ.get("WP_URL", "").rstrip("/")
paginas = ["/blog/como-abrir-una-tienda-en-linea-en-mexico-con-shopify/", "/recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/"]
if base:
    home = requests.get(base + "/wp-json/", timeout=30, headers=UA).json().get("home", base).rstrip("/")
    for p in paginas:
        html = requests.get(home + p, timeout=30, headers=UA).text
        tags = re.findall(r"<a\s[^>]*shopify\.pxf\.io[^>]*>", html)
        good = [t for t in tags if f'href="{MASK}"' in t and "sponsored" in t]
        checks[f"{p}: {len(good)} de {len(tags)} enlaces exactos y sponsored"] = bool(tags) and len(good) == len(tags)

lines = ["# Enlace de afiliado de Shopify", "", f"- **Máscara (enlace de afiliado):** {MASK}",
         f"- **Destino final:** {final}", "", "## Saltos", "", "| HTTP | URL | Redirige a |", "|---|---|---|"]
lines += [f"| {c} | {u} | {l or ''} |" for c, u, l in hops]
lines += ["", "## Comprobaciones", ""]
for k, v in checks.items():
    lines.append(f"- {'OK' if v else 'FALLA'}: {k}")
    ok &= v
out = ROOT / "registro" / "shopify.md"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
sys.exit(0 if ok else 1)
