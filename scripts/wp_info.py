#!/usr/bin/env python3
"""Diagnóstico de WordPress: tema, plugins, ajustes, páginas, entradas y menús. Escribe migracion/wp-info.json."""
import json
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from publish import WP, env  # noqa: E402
from sitio_url import base_url  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------- Sondeo sin autenticación (antes de conectar) ----------
import requests as _rq  # noqa: E402
_UA = {"User-Agent": "Mozilla/5.0 (compatible; fm-diagnostico/1.0)"}
for _base in ("https://www.fernandomartinez.mx", "https://fernandomartinez.mx"):
    for _p in ("/", "/?rest_route=/", "/index.php?rest_route=/", "/wp-json/", "/index.php/wp-json/", "/blog/",
               "/blog/que-es-el-inbound-marketing/", "/?p=72", "/dev/", "/dev/wp-json/", "/wp-login.php", "/wp-admin/"):
        try:
            _r = _rq.get(_base + _p, headers=_UA, timeout=30, allow_redirects=False)
            _extra = ""
            if "rest_route" in _p and _r.status_code == 200:
                try:
                    _j = _r.json(); _extra = f"home={_j.get('home')} url={_j.get('url')}"
                except ValueError:
                    _extra = "no-json"
            print(f"sondeo {_base}{_p} -> {_r.status_code} loc={_r.headers.get('location')} srv={_r.headers.get('server')} "
                  f"cf={_r.headers.get('cf-cache-status')} {_extra} | {_r.text[:90]!r}")
        except Exception as _e:  # noqa: BLE001
            print(f"sondeo {_base}{_p} -> ERROR {str(_e)[:120]}")
import fix_raiz  # noqa: E402  (arreglo único de la migración)
fix_raiz.main()
wp = WP(base_url(), env("WP_USER"), env("WP_APP_PASSWORD"))
info = {"me": {k: wp.whoami().get(k) for k in ("username", "roles")}}


def get(path, **params):
    r = wp.s.get(f"{wp.api.rsplit('/wp/v2', 1)[0]}/{path}", params=params, timeout=30)
    try:
        return r.status_code, r.json()
    except ValueError:
        return r.status_code, r.text[:300]


for key, path, params in [
    ("settings", "wp/v2/settings", {}),
    ("themes", "wp/v2/themes", {}),
    ("plugins", "wp/v2/plugins", {}),
    ("pages", "wp/v2/pages", {"per_page": 100, "context": "edit", "status": "any"}),
    ("posts", "wp/v2/posts", {"per_page": 100, "context": "edit", "status": "any"}),
    ("categories", "wp/v2/categories", {"per_page": 100}),
    ("menus", "wp/v2/menus", {}),
    ("menu_locations", "wp/v2/menu-locations", {}),
    ("templates", "wp/v2/templates", {"per_page": 100}),
    ("navigation", "wp/v2/navigation", {"context": "edit"}),
]:
    code, data = get(path, **params)
    if isinstance(data, list):
        slim = []
        for d in data:
            if isinstance(d, dict):
                slim.append({k: (v.get("raw", v.get("rendered")) if isinstance(v, dict) and k in ("title", "content") else v)
                             for k, v in d.items() if k in ("id", "slug", "status", "title", "name", "stylesheet", "plugin",
                                                            "version", "link", "template", "parent", "description", "locations", "content", "count")})
        if key in ("templates", "navigation"):
            for s in slim:
                if isinstance(s.get("content"), str):
                    s["content"] = s["content"][:1500]
        data = slim
    info[key] = {"status": code, "data": data}
    print(key, code, len(data) if isinstance(data, (list, dict)) else data)

root = wp.s.get(wp.api.rsplit("/wp/v2", 1)[0] + "/", timeout=30).json()
info["site"] = {k: root.get(k) for k in ("name", "description", "url", "home", "gmt_offset", "timezone_string", "namespaces")}
(ROOT / "migracion").mkdir(exist_ok=True)
(ROOT / "migracion" / "wp-info.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")


# ---------- Revisión del sitio en vivo después de la migración a la raíz ----------
import re  # noqa: E402

import requests  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0 (compatible; fm-diagnostico/1.0)"}
home = (root.get("home") or base_url()).rstrip("/")
vivo = {"home": root.get("home"), "url": root.get("url")}


def probe(path):
    try:
        r = requests.get(home + path, headers=UA, timeout=30, allow_redirects=False)
        return {"status": r.status_code, "location": r.headers.get("location"), "server": r.headers.get("server"),
                "cache": r.headers.get("cf-cache-status")}
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)[:200]}


for path in ["/", "/blog/", "/blog/que-es-el-inbound-marketing/", "/fernando-arturo-martinez-aguilar/",
             "/dev/", "/dev/blog/que-es-el-inbound-marketing/", "/dev/wp-json/",
             "/blog/14-que-es-el-inbound-marketing", "/index.php/blog", "/temas/inbound",
             "/robots.txt", "/wp-sitemap.xml", "/wp-admin/", "/wp-content/uploads/"]:
    vivo[path] = probe(path)
    print("vivo", path, vivo[path])

html = requests.get(home + "/", headers=UA, timeout=30).text
vivo["home_html_dev_refs"] = sorted(set(re.findall(r'https?://[^"\'\s)]*?/dev/[^"\'\s)]*', html)))[:40]
vivo["home_html_title"] = (re.search(r"<title>(.*?)</title>", html, re.S) or [None, None])[1]
vivo["home_html_noindex"] = "noindex" in html
print("dev en portada:", len(vivo["home_html_dev_refs"]), vivo["home_html_dev_refs"][:8])
print("titulo:", vivo["home_html_title"], "| noindex:", vivo["home_html_noindex"])

# /dev en contenido guardado (páginas, entradas, plantillas, navegación)
dev_hits = {}
for kind in ("pages", "posts", "templates", "template-parts", "navigation", "global-styles"):
    try:
        items = wp.req("GET", kind, params={"per_page": 100, "context": "edit", **({"status": "any"} if kind in ("pages", "posts") else {})}) \
            if kind != "global-styles" else []
    except Exception as e:  # noqa: BLE001
        dev_hits[kind] = f"error {str(e)[:120]}"
        continue
    for it in items:
        c = it.get("content")
        raw = c.get("raw", "") if isinstance(c, dict) else (c or "")
        n = len(re.findall(r"fernandomartinez\.mx/dev/", raw))
        if n:
            dev_hits[f"{kind}:{it.get('slug') or it.get('id')}"] = n
vivo["contenido_con_dev"] = dev_hits
print("contenido con /dev:", len(dev_hits), list(dev_hits.items())[:10])
info["vivo"] = vivo
(ROOT / "migracion" / "wp-info.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
