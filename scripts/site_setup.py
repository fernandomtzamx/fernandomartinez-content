#!/usr/bin/env python3
"""Aplica docs/sitio.yml: ajustes, portada y blog, autor, categorías, menú, colores de marca,
pie de página y limpieza de ejemplos. Idempotente: se puede correr las veces que haga falta.
Requiere rol Administrador (ajustes, menús y estilos globales)."""
import html
import importlib.util
import json
import re
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
    sys.path.insert(0, str(ROOT / "scripts"))
    from sitio_url import base_url
    wp = pub.WP(base_url(), pub.env("WP_USER"), pub.env("WP_APP_PASSWORD"))
    wp.whoami()
    root = wp.api.rsplit("/wp/v2", 1)[0]
    errors = []
    estado = {}
    m = cfg.get("marca") or {}

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
            nav_id = found[0]["id"]
            wp.req("POST", f"navigation/{nav_id}", json=payload)
            print(f"Menú actualizado (id {nav_id})")
        else:
            nav_id = wp.req("POST", "navigation", json=payload)["id"]
            print(f"Menú creado (id {nav_id})")
        estado["nav"] = nav_id
        # El bloque de navegación del encabezado apunta explícitamente a este menú
        # (sin "ref" el tema muestra la lista automática de todas las páginas).
        theme = active_theme()
        head = wp.req("GET", f"template-parts/{theme}//header", params={"context": "edit"})
        raw = head["content"]["raw"] if isinstance(head.get("content"), dict) else head.get("content", "")
        new = re.sub(r'<!-- wp:navigation (\{.*?\}) (/?)-->',
                     lambda m: "<!-- wp:navigation " + json.dumps({**json.loads(m.group(1)), "ref": nav_id},
                                                                   ensure_ascii=False, separators=(",", ":")) + f" {m.group(2)}-->",
                     raw, count=1)
        if new == raw and '"ref":' not in raw:
            new = raw.replace("<!-- wp:navigation /-->", '<!-- wp:navigation {"ref":%d} /-->' % nav_id, 1)
        if new != raw:
            wp.req("POST", f"template-parts/{theme}//header", json={"content": new})
            print(f"Encabezado ligado al menú {nav_id}")
        else:
            print("Aviso: no encontré el bloque de navegación en el encabezado")

    def active_theme():
        return wp.s.get(f"{wp.api}/themes", params={"status": "active"}, timeout=30).json()[0]["stylesheet"]

    def plantillas():
        theme = active_theme()
        b = cfg["blog"]
        loop = """<!-- wp:query {"queryId":1,"query":{"inherit":true,"perPage":12},"align":"wide"} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {"layout":{"type":"grid","columnCount":3,"minimumColumnWidth":"18rem"}} -->
<!-- wp:post-featured-image {"isLink":true,"aspectRatio":"auto","style":{"border":{"radius":"12px"}}} /-->

<!-- wp:post-terms {"term":"category","fontSize":"small"} /-->

<!-- wp:post-title {"isLink":true,"fontSize":"large"} /-->

<!-- wp:post-excerpt {"excerptLength":28} /-->
<!-- /wp:post-template -->

<!-- wp:query-pagination {"layout":{"type":"flex","justifyContent":"space-between"}} -->
<!-- wp:query-pagination-previous {"label":"Más recientes"} /-->

<!-- wp:query-pagination-numbers /-->

<!-- wp:query-pagination-next {"label":"Anteriores"} /-->
<!-- /wp:query-pagination --></div>
<!-- /wp:query -->"""
        def wrap(inner):
            return ('<!-- wp:template-part {"slug":"header"} /-->\n\n'
                    '<!-- wp:group {"tagName":"main","align":"full","style":{"spacing":{"padding":{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|60","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}},"layout":{"type":"constrained"}} -->\n'
                    '<main class="wp-block-group alignfull" style="padding-top:var(--wp--preset--spacing--50);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--60);padding-left:var(--wp--preset--spacing--50)">'
                    f"{inner}\n\n{loop}</main>\n<!-- /wp:group -->\n\n"
                    '<!-- wp:template-part {"slug":"footer"} /-->')
        def extra_blog():
            """Fila de temas (enlaces a categorías, con su URL real) y entradas destacadas."""
            out = ""
            temas = []
            for tm in b.get("temas") or []:
                found = wp.req("GET", "categories", params={"slug": tm["categoria"]})
                if found:
                    temas.append(f'<a href="{found[0]["link"]}">{html.escape(tm["label"])}</a>')
            if temas:
                out += ('\n\n<!-- wp:paragraph {"className":"fm-temas"} -->\n<p class="fm-temas"><strong>Temas:</strong> '
                        + " ".join(temas) + "</p>\n<!-- /wp:paragraph -->")
            dest = [f'<a href="{wp.home}{d["url"]}">{html.escape(d["label"])}</a>' for d in b.get("destacadas") or []]
            if dest:
                out += ('\n\n<!-- wp:paragraph {"className":"fm-destacadas"} -->\n<p class="fm-destacadas"><strong>Empieza por aquí:</strong> '
                        + " · ".join(dest) + "</p>\n<!-- /wp:paragraph -->")
            return out
        home = wrap(f"""<!-- wp:heading {{"level":1}} -->
<h1 class="wp-block-heading">{html.escape(b["titulo"])}</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {{"fontSize":"medium"}} -->
<p class="has-medium-font-size">{html.escape(b["intro"])}</p>
<!-- /wp:paragraph -->{extra_blog()}""")
        archive = wrap("""<!-- wp:query-title {"type":"archive","level":1} /-->

<!-- wp:term-description /-->""")
        for slug, content in [("home", home), ("archive", archive)]:
            wp.req("POST", f"templates/{theme}//{slug}", json={"content": content})
            print(f"Plantilla {slug} actualizada")

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
        el["heading"] = {"color": {"text": "var:preset|color|contrast"},
                         "typography": {"fontWeight": "800", "letterSpacing": "-0.02em", "lineHeight": "1.15"}}
        el["button"][":hover"] = {"color": {"background": "var:preset|color|contrast", "text": "var:preset|color|base"}}
        styles.setdefault("typography", {})["fontWeight"] = "400"
        if cfg.get("layout"):
            settings.setdefault("layout", {}).update(cfg["layout"])
        styles["css"] = cfg.get("css", "")
        wp.req("POST", f"global-styles/{gid}", json={"settings": settings, "styles": styles})
        print(f"Estilos globales aplicados (id {gid})")


    def marca():
        """Sube logo, logo blanco e ícono; fija logo e ícono del sitio."""
        if not m:
            return
        logo = wp.media_id(ROOT / m["logo"], "Fernando Martínez")
        icono = wp.media_id(ROOT / m["icono"], "Fernando Martínez")
        estado["logo_blanco"] = wp.media_url(ROOT / m["logo_blanco"], "Fernando Martínez")
        res = wp.req("POST", "settings", json={"site_logo": logo, "site_icon": icono})
        print(f"Marca: logo={res.get('site_logo')} ícono={res.get('site_icon')}")

    def encabezado():
        """Logo a la izquierda, menú y botón de contacto a la derecha. Fijo al hacer scroll."""
        theme = active_theme()
        nav = estado.get("nav")
        nav_attrs = json.dumps({**({"ref": nav} if nav else {}), "overlayBackgroundColor": "base",
                                "overlayTextColor": "contrast",
                                "layout": {"type": "flex", "justifyContent": "right"},
                                "style": {"spacing": {"blockGap": "var:preset|spacing|40"}}},
                               ensure_ascii=False, separators=(",", ":"))
        b = m.get("boton") or {"label": "Platiquemos", "url": "/contacto/"}
        content = f"""<!-- wp:group {{"align":"full","className":"fm-header","style":{{"spacing":{{"padding":{{"top":"14px","bottom":"14px","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull fm-header" style="padding-top:14px;padding-right:var(--wp--preset--spacing--50);padding-bottom:14px;padding-left:var(--wp--preset--spacing--50)"><!-- wp:group {{"align":"wide","layout":{{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between"}}}} -->
<div class="wp-block-group alignwide"><!-- wp:site-logo {{"width":170,"shouldSyncIcon":false}} /-->

<!-- wp:group {{"style":{{"spacing":{{"blockGap":"var:preset|spacing|40"}}}},"layout":{{"type":"flex","flexWrap":"nowrap"}}}} -->
<div class="wp-block-group"><!-- wp:navigation {nav_attrs} /-->

<!-- wp:buttons {{"className":"fm-header-cta"}} -->
<div class="wp-block-buttons fm-header-cta"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{wp.home}{b['url']}">{html.escape(b['label'])}</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons --></div>
<!-- /wp:group --></div>
<!-- /wp:group --></div>
<!-- /wp:group -->"""
        wp.req("POST", f"template-parts/{theme}//header", json={"content": content})
        print(f"Encabezado con logo, menú {nav} y botón '{b['label']}'")

    def entrada():
        """Plantilla de entrada: categoría, título, metadatos, portada ancha, texto, etiquetas,
        anterior/siguiente y tres entradas más en tarjetas."""
        theme = active_theme()
        pad = '"spacing":{"padding":{"left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}'
        content = f"""<!-- wp:template-part {{"slug":"header"}} /-->

<!-- wp:group {{"tagName":"main","align":"full","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}},"blockGap":"var:preset|spacing|40"}}}},"layout":{{"type":"constrained"}}}} -->
<main class="wp-block-group alignfull" style="padding-top:var(--wp--preset--spacing--60);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--60);padding-left:var(--wp--preset--spacing--50)"><!-- wp:post-terms {{"term":"category"}} /-->

<!-- wp:post-title {{"level":1,"style":{{"typography":{{"fontSize":"clamp(2rem, 4.5vw, 3.1rem)"}}}}}} /-->

<!-- wp:post-excerpt {{"fontSize":"large","textColor":"accent-4"}} /-->

<!-- wp:group {{"className":"fm-meta","layout":{{"type":"flex","flexWrap":"wrap"}},"style":{{"spacing":{{"blockGap":"0.6em"}}}}}} -->
<div class="wp-block-group fm-meta"><!-- wp:post-author-name {{"isLink":true}} /-->

<!-- wp:paragraph {{"className":"fm-sep"}} -->
<p class="fm-sep">·</p>
<!-- /wp:paragraph -->

<!-- wp:post-date /--></div>
<!-- /wp:group -->

<!-- wp:post-featured-image {{"align":"wide","style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|40","bottom":"var:preset|spacing|50"}}}}}}}} /-->

<!-- wp:post-content {{"layout":{{"type":"constrained"}}}} /-->

<!-- wp:post-terms {{"term":"post_tag","separator":"  ","className":"is-style-post-terms-1"}} /-->

<!-- wp:separator {{"className":"is-style-wide","backgroundColor":"accent-2","style":{{"spacing":{{"margin":{{"top":"var:preset|spacing|50","bottom":"var:preset|spacing|40"}}}}}}}} -->
<hr class="wp-block-separator has-text-color has-accent-2-color has-alpha-channel-opacity has-accent-2-background-color has-background is-style-wide" style="margin-top:var(--wp--preset--spacing--50);margin-bottom:var(--wp--preset--spacing--40)"/>
<!-- /wp:separator -->

<!-- wp:group {{"layout":{{"type":"flex","flexWrap":"nowrap","justifyContent":"space-between","verticalAlignment":"top"}}}} -->
<div class="wp-block-group"><!-- wp:post-navigation-link {{"type":"previous","label":"Anterior","showTitle":true}} /-->

<!-- wp:post-navigation-link {{"textAlign":"right","label":"Siguiente","showTitle":true}} /--></div>
<!-- /wp:group --></main>
<!-- /wp:group -->

<!-- wp:group {{"align":"full","backgroundColor":"accent-5","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|60","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull has-accent-5-background-color has-background" style="padding-top:var(--wp--preset--spacing--60);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--60);padding-left:var(--wp--preset--spacing--50)"><!-- wp:paragraph {{"align":"wide","className":"fm-kicker-llaves"}} -->
<p class="alignwide fm-kicker-llaves">{{ sigue leyendo }}</p>
<!-- /wp:paragraph -->

<!-- wp:query {{"queryId":7,"query":{{"perPage":3,"postType":"post","order":"desc","orderBy":"date","inherit":false}},"align":"wide"}} -->
<div class="wp-block-query alignwide"><!-- wp:post-template {{"layout":{{"type":"grid","columnCount":3,"minimumColumnWidth":"16rem"}}}} -->
<!-- wp:post-featured-image {{"isLink":true,"aspectRatio":"auto"}} /-->

<!-- wp:post-terms {{"term":"category","fontSize":"small"}} /-->

<!-- wp:post-title {{"level":3,"isLink":true,"fontSize":"large"}} /-->
<!-- /wp:post-template --></div>
<!-- /wp:query --></div>
<!-- /wp:group -->

<!-- wp:template-part {{"slug":"footer"}} /-->"""
        wp.req("POST", f"templates/{theme}//single", json={"content": content})
        print("Plantilla single actualizada")

    def pie():
        nav = " · ".join(f'<a href="{wp.home}{m["url"]}">{html.escape(m["label"])}</a>' for m in cfg["menu"])
        logo = estado.get("logo_blanco")
        marca_html = (f'<!-- wp:image {{"width":"200px","sizeSlug":"full","linkDestination":"custom"}} -->\n'
                      f'<figure class="wp-block-image size-full is-resized"><a href="{wp.home}/"><img src="{logo}" alt="Fernando Martínez" style="width:200px"/></a></figure>\n'
                      f'<!-- /wp:image -->') if logo else (
            '<!-- wp:paragraph {"style":{"typography":{"fontWeight":"800"}},"fontSize":"large"} -->\n'
            '<p class="has-large-font-size" style="font-weight:800">{ Fernando Martínez }</p>\n<!-- /wp:paragraph -->')
        nav = "".join(f'<!-- wp:paragraph -->\n<p><a href="{wp.home}{x["url"]}">{html.escape(x["label"])}</a></p>\n<!-- /wp:paragraph -->\n\n'
                      for x in cfg["menu"])
        content = f"""<!-- wp:group {{"align":"full","className":"fm-footer","backgroundColor":"contrast","textColor":"base","style":{{"spacing":{{"padding":{{"top":"var:preset|spacing|60","bottom":"var:preset|spacing|50","left":"var:preset|spacing|50","right":"var:preset|spacing|50"}}}},"elements":{{"link":{{"color":{{"text":"var:preset|color|base"}}}}}}}},"layout":{{"type":"constrained"}}}} -->
<div class="wp-block-group alignfull fm-footer has-base-color has-contrast-background-color has-text-color has-background has-link-color" style="padding-top:var(--wp--preset--spacing--60);padding-right:var(--wp--preset--spacing--50);padding-bottom:var(--wp--preset--spacing--50);padding-left:var(--wp--preset--spacing--50)"><!-- wp:columns {{"align":"wide"}} -->
<div class="wp-block-columns alignwide"><!-- wp:column {{"width":"55%"}} -->
<div class="wp-block-column" style="flex-basis:55%">{marca_html}

<!-- wp:paragraph {{"style":{{"typography":{{"lineHeight":"1.6"}}}}}} -->
<p style="line-height:1.6">{html.escape(cfg["ajustes"]["description"])}. Hago que la tecnología venda, y si no vende, la apago.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"className":"fm-kicker-llaves"}} -->
<p class="fm-kicker-llaves">{{ sitio }}</p>
<!-- /wp:paragraph -->

<!-- wp:group {{"style":{{"spacing":{{"blockGap":"0.4em"}}}},"layout":{{"type":"flex","orientation":"vertical"}}}} -->
<div class="wp-block-group">{nav}</div>
<!-- /wp:group --></div>
<!-- /wp:column -->

<!-- wp:column -->
<div class="wp-block-column"><!-- wp:paragraph {{"className":"fm-kicker-llaves"}} -->
<p class="fm-kicker-llaves">{{ conecta }}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="https://www.linkedin.com/in/fernandomtza/" rel="nofollow">LinkedIn</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><a href="{wp.home}/contacto/">Escríbeme</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:column --></div>
<!-- /wp:columns -->

<!-- wp:separator {{"align":"wide","style":{{"color":{{"background":"#ffffff26"}}}}}} -->
<hr class="wp-block-separator alignwide has-text-color has-alpha-channel-opacity has-background" style="background-color:#ffffff26;color:#ffffff26"/>
<!-- /wp:separator -->

<!-- wp:paragraph {{"align":"wide","fontSize":"small","style":{{"color":{{"text":"#ffffffb3"}}}}}} -->
<p class="alignwide has-text-color has-small-font-size" style="color:#ffffffb3">© 2026 Fernando Martínez · <a href="{wp.home}/gnu-general-public-license/">Licencia de mis extensiones</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->"""
        theme = active_theme()
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

    for name, fn in [("ajustes", ajustes), ("autor", autor), ("categorías", categorias), ("marca", marca),
                     ("menú", menu), ("encabezado", encabezado), ("estilos", estilos), ("plantillas", plantillas),
                     ("entrada", entrada), ("pie", pie), ("borrar", borrar)]:
        step(name, fn, errors)
    if errors:
        sys.exit(f"{len(errors)} paso(s) con error: {', '.join(errors)}")


if __name__ == "__main__":
    main()
