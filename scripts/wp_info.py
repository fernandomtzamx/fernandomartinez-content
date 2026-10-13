#!/usr/bin/env python3
"""Diagnóstico de WordPress: tema, plugins, ajustes, páginas, entradas y menús. Escribe migracion/wp-info.json."""
import json
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from publish import WP, env  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
wp = WP(env("WP_URL"), env("WP_USER"), env("WP_APP_PASSWORD"))
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
