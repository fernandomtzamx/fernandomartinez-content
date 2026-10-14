#!/usr/bin/env python3
"""Capturas del sitio publicado (escritorio y celular) en registro/capturas/."""
import os
import pathlib
import sys

import requests
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sitio_url import base_url  # noqa: E402
base = base_url()
base = requests.get(base + "/wp-json/", timeout=30).json().get("home", base).rstrip("/")
pages = sys.argv[1:] or ["/", "/fernando-arturo-martinez-aguilar/", "/como-te-ayudo/", "/blog/",
                         "/blog/credito-automotriz-en-linea-disrupcion-venta-de-autos/",
                         "/blog/como-abrir-una-tienda-en-linea-en-mexico-con-shopify/", "/recursos/", "/contacto/"]
out = ROOT / "registro" / "capturas"
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, vp in [("escritorio", {"width": 1366, "height": 900}), ("celular", {"width": 390, "height": 844})]:
        ctx = b.new_context(viewport=vp, device_scale_factor=1)
        page = ctx.new_page()
        for path in pages:
            page.goto(base + path, wait_until="networkidle", timeout=60000)
            slug = path.strip("/").replace("/", "_") or "inicio"
            page.screenshot(path=str(out / f"{slug}-{name}.png"), full_page=(name == "escritorio"))
            print(name, path, page.title())
            if name == "celular" and path == "/":
                boton = page.locator(".wp-block-navigation__responsive-container-open").first
                if boton.count():
                    boton.click()
                    page.wait_for_timeout(600)
                    page.screenshot(path=str(out / "inicio-menu-abierto-celular.png"))
                    page.keyboard.press("Escape")
                    print(name, "menú abierto")
        ctx.close()
    b.close()
