#!/usr/bin/env python3
"""Aplica docs/sitio.yml: ajustes, portada y blog, autor, categorías, menú, colores de marca,
pie de página y limpieza de ejemplos. Idempotente: se puede correr las veces que haga falta.
Requiere rol Administrador (ajustes, menús y estilos globales)."""
import html
import importlib.util
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("publish", ROOT / "scripts" / "publish.py")
pub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pub)

PALETTE_NAMES = {"base": "Base", "contrast": "Contrast", "accent-1": "Accent 1", "accent-2": "Accent 2",
                 "accent-3": "Accent 3", "accent-4": "Accent 4", "accent-5": "Accent 5"}


def step(name, fn, errors):
    try:
        fn()
    except Exception as e:  # noqa: BLE001
        errors.append(name)
        print(f"ERROR {name}: {str(e)[:300]}")


def main():
    cfg = yaml.safe_load((ROOT / "docs" / "sitio.yml").read_text(encoding="utf-8"))
    wp = pub.WP(pub.env("WP_URL"), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    wp.whoami()
    root = wp.api.rsplit("/wp/v2", 1)[0]
    errors = []

    def ajustes():
        a = dict(cfg["ajustes"])
        payload = {k: a[k] for k in ("title", "description", "timezone", "date_format", "posts_per_page",
                                     "default_comment_status", "default_ping_status") if k in a}
        front = wp.find_by_slug("pages", a["portada"])
        blog = wp.find_by_slug("pages", a["pagina_blog"])
        if front and blog:
            payload.update(show_on_front="page", page_on_front=front["id"], page_for_posts=blog["id"])
        else:
            print("Aviso: aún no existen las páginas de portada o blog; publica primero el contenido.")
        res = wp.req("POST", "settings", json=payload)
        print(f"Ajustes: {res.get('title')} | portada={res.get('page_on_front')} blog={res.get('page_for_posts')} | zona={res.get('timezone')}")

    def autor():
        me = wp.req("POST", "users/me", json=cfg["autor"])
        print(f"Autor: {me.get('name')}")

    def categorias():
        for c in cfg.get("categorias") or []:
            payload = {"name": c["name"], "description": c.get("description", "")}
            found = wp.req("GET", "categories", params={"slug": c["slug"]})
            if found:
                wp.req("POST", f"categories/{found[0]['id']}", json=payload)
            else:
                wp.req("POST", "categories", json={**payload, "slug": c["slug"]})
            print(f"Categoría: {c['slug']} -> {c['name']}")

    def menu():
        links = "\n".join(
            '<!-- wp:navigation-link {"label":"%s","url":"%s","kind":"custom","isTopLevelLink":true} /-->'
            % (html.escape(m["label"]), wp.home + m["url"]) for m in cfg["menu"])
        found = [n for n in wp.req("GET", "navigation", params={"per_page": 50, "context": "edit"})
                 if (n.get("title") or {}).get("raw") == "Menú principal"]
        payload = {"title": "Menú principal", "status": "publish", "content": links}
        if found:
            wp.req("POST", f"navigation/{found[0]['id']}", json=payload)
            print(f"Menú actualizado (id {found[0]['id']})")
        else:
            res = wp.req("POST", "navigation", json=payload)
            print(f"Menú creado (id {res['id']})")

    def estilos():
        themes = wp.s.get(f"{wp.api}/themes", params={"status": "active"}, timeout=30).json()
        href = themes[0]["_links"]["wp:user-global-styles"][0]["href"]
        gid = href.rstrip("/").rsplit("/", 1)[1]
        cur = wp.req("GET", f"global-styles/{gid}", params={"context": "edit"})
        settings = cur.get("settings") or {}
        styles = cur.get("styles") or {}
        palette = [{"slug": k, "name": PALETTE_NAMES[k], "color": v} for k, v in cfg["paleta"].items()]
        palette.append({"slug": "accent-6", "name": "Accent 6", "color": "color-mix(in srgb, currentColor 20%, transparent)"})
        settings.setdefault("color", {}).setdefault("palette", {})["theme"] = palette
        el = styles.setdefault("elements", {})
        el["link"] = {"color": {"text": "var:preset|color|accent-3"}, ":hover": {"color": {"text": "var:preset|color|contrast"}}}
        el["button"] = {"color": {"background": "var:preset|color|accent-3", "text": "var:preset|color|base"},
                        "border": {"radius": "999px"}, "typography": {"fontWeight": "700"}}
        el["heading"] = {"typography": {"fontWeight": "800", "letterSpacing": "-0.02em"}}
        wp.req("POST", f"global-styles/{gid}", json={"settings": settings, "styles": styles})
        print(f"Estilos globales aplicados (id {gid})")

    def pie():
        nav = " · ".join(f'<a href="{wp.home}{m["url"]}">{html.escape(m["label"])}</a>' for m in cfg["menu"])
        content = f"""<!-- wp:group {{"align":"full","backgroundColor":"contrast","textColor":"base","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|50","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}},"elements":{{"link":{{"color":{{"text":"var:preset|color|accent-1"}}}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-base-color has-contrast-background-color has-text-color has-background has-link-color" style="padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--50)"><!-- wp:paragraph {{"style":{{"typography":{{"fontWeight":"800"}}}},"fontSize":"large"}} -->
<p class="has-large-font-size" style="font-weight:800">{{ Fernando Martínez }}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>{html.escape(cfg["ajustes"]["description"])}. Hago que la tecnología venda, y si no vende, la apago.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>{nav} · <a href="https://www.linkedin.com/in/fernandomtza/" rel="nofollow">LinkedIn</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {{"fontSize":"small"}} -->
<p class="has-small-font-size">© 2026 Fernando Martínez · <a href="{wp.home}/gnu-general-public-license/">Licencia de mis extensiones</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""
        theme = wp.s.get(f"{wp.api}/themes", params={"status": "active"}, timeout=30).json()[0]["stylesheet"]
        wp.req("POST", f"template-parts/{theme}//footer", json={"content": content})
        print("Pie de página actualizado")

    def borrar():
        for b in cfg.get("borrar") or []:
            tipo = b.get("tipo", "pages")
            try:
                cur = wp.req("GET", f"{tipo}/{b['id']}", params={"context": "edit"})
            except Exception:  # noqa: BLE001
                print(f"Ya no existe {tipo}/{b['id']} ({b['slug']})")
                continue
            if cur.get("status") == "trash":
                print(f"Ya en papelera: {tipo}/{b['id']}")
                continue
            if not (cur.get("slug") or cur.get("generated_slug", "")).startswith(b["slug"]):
                print(f"No se borra {tipo}/{b['id']}: el slug no coincide con '{b['slug']}'")
                continue
            wp.req("DELETE", f"{tipo}/{b['id']}")
            print(f"A la papelera: {tipo}/{b['id']} ({b['slug']})")

    for name, fn in [("ajustes", ajustes), ("autor", autor), ("categorías", categorias), ("menú", menu),
                     ("estilos", estilos), ("pie", pie), ("borrar", borrar)]:
        step(name, fn, errors)
    if errors:
        sys.exit(f"{len(errors)} paso(s) con error: {', '.join(errors)}")


if __name__ == "__main__":
    main()
