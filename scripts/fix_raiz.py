#!/usr/bin/env python3
"""Arreglo único después de mover WordPress de /dev a la raíz a mano (14 oct 2026).

1. Cambia home y siteurl a la raíz.
2. Escribe el .htaccess de la raíz: redirecciones (Joomla y /dev) + bloque de WordPress.
   Conserva bloques de plugins (# BEGIN X ... # END X) y guarda respaldo .htaccess.fm-respaldo-<fecha>.
Se hace con un fragmento de Code Snippets que se instala, se ejecuta una vez y se borra (plugin incluido).
Funciona aunque /wp-json/ dé 404: usa /index.php/wp-json/.
"""
import base64
import os
import pathlib
import time

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://www.fernandomartinez.mx"
UA = {"User-Agent": "Mozilla/5.0 (compatible; fm-agente/1.0)"}


def main():
    user, pw = os.environ["WP_USER"], os.environ["WP_APP_PASSWORD"].replace(" ", "")
    s = requests.Session()
    s.auth = (user, pw)
    s.headers.update(UA)
    s.headers["X-Agente-Auth"] = "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()

    def api(method, route, **kw):
        for base in (f"{SITE}/wp-json", f"{SITE}/index.php/wp-json"):
            r = s.request(method, f"{base}/{route.lstrip('/')}", timeout=60, **kw)
            if r.status_code != 404 or "rest_no_route" in r.text:
                return r
        return r

    me = api("GET", "wp/v2/users/me", params={"context": "edit"})
    print("fix_raiz: usuario", me.status_code, (me.json().get("roles") if me.ok else me.text[:200]))
    if not me.ok:
        return

    ht = (ROOT / "migracion" / "raiz" / ".htaccess").read_text(encoding="utf-8")
    code = r"""
$fm_url = 'https://www.fernandomartinez.mx';
if ( get_option( 'siteurl' ) !== $fm_url ) { update_option( 'siteurl', $fm_url ); }
if ( get_option( 'home' ) !== $fm_url ) { update_option( 'home', $fm_url ); }
if ( ! get_option( 'fm_htaccess_raiz' ) ) {
	$fm_file = ABSPATH . '.htaccess';
	$fm_old  = file_exists( $fm_file ) ? (string) file_get_contents( $fm_file ) : '';
	if ( '' !== $fm_old ) { @copy( $fm_file, ABSPATH . '.htaccess.fm-respaldo-' . gmdate( 'Ymd-His' ) ); }
	$fm_keep = '';
	if ( preg_match_all( '/^# BEGIN (.+?)\R.*?^# END \1\s*$/ms', $fm_old, $fm_m, PREG_SET_ORDER ) ) {
		foreach ( $fm_m as $fm_b ) {
			if ( in_array( trim( $fm_b[1] ), array( 'WordPress', 'Redirecciones fernandomartinez.mx' ), true ) ) { continue; }
			$fm_keep .= trim( $fm_b[0] ) . "\n\n";
		}
	}
	$fm_new = $fm_keep . <<<'FMHT'
""" + ht + r"""FMHT;
	$fm_ok = false !== @file_put_contents( $fm_file, $fm_new );
	update_option( 'fm_htaccess_raiz', array( 'ok' => $fm_ok, 'antes' => substr( $fm_old, 0, 3000 ), 'bloques_conservados' => $fm_keep, 'abspath' => ABSPATH, 'fecha' => gmdate( 'c' ) ), false );
}
"""
    # 1. Plugin Code Snippets (temporal)
    r = api("GET", "wp/v2/plugins/code-snippets/code-snippets")
    if r.status_code != 200:
        r = api("POST", "wp/v2/plugins", json={"slug": "code-snippets", "status": "active"})
        print("fix_raiz: instalar Code Snippets", r.status_code, r.text[:200])
    elif r.json().get("status") != "active":
        r = api("POST", "wp/v2/plugins/code-snippets/code-snippets", json={"status": "active"})
        print("fix_raiz: activar Code Snippets", r.status_code)

    # 2. Fragmento
    r = api("POST", "code-snippets/v1/snippets",
            json={"name": "fm: mover a la raíz (temporal)", "code": code, "scope": "global", "active": True})
    print("fix_raiz: fragmento", r.status_code, r.text[:300])
    sid = r.json().get("id") if r.ok else None
    if sid and not r.json().get("active"):
        r2 = api("POST", f"code-snippets/v1/snippets/{sid}/activate")
        print("fix_raiz: activar fragmento", r2.status_code, r2.text[:200])

    # 3. Ejecutarlo con una carga del sitio y revisar
    for _ in range(3):
        s.get(f"{SITE}/index.php?rest_route=/", timeout=60)
        time.sleep(2)
    idx = requests.get(f"{SITE}/index.php?rest_route=/", headers=UA, timeout=60).json()
    print("fix_raiz: home ahora =", idx.get("home"), "| url =", idx.get("url"))
    st = api("GET", "wp/v2/settings").json()
    print("fix_raiz: siteurl ahora =", st.get("url"))

    # Resultado del .htaccess (se lee con otro fragmento de solo lectura no hace falta: lo deja en una opción)
    chk = api("POST", "code-snippets/v1/snippets",
              json={"name": "fm: leer resultado (temporal)", "scope": "global", "active": True,
                    "code": "add_action('rest_api_init',function(){register_rest_route('fm/v1','/htaccess',array('methods'=>'GET','permission_callback'=>function(){return current_user_can('manage_options');},'callback'=>function(){return get_option('fm_htaccess_raiz');}));});"})
    cid = chk.json().get("id") if chk.ok else None
    res = api("GET", "fm/v1/htaccess")
    print("fix_raiz: .htaccess", res.status_code, res.text[:1500])

    for x in (sid, cid):
        if x:
            print("fix_raiz: borrar fragmento", x, api("DELETE", f"code-snippets/v1/snippets/{x}").status_code)
    api("POST", "wp/v2/plugins/code-snippets/code-snippets", json={"status": "inactive"})
    print("fix_raiz: borrar Code Snippets", api("DELETE", "wp/v2/plugins/code-snippets/code-snippets").status_code)

    for p in ("/", "/blog/", "/blog/que-es-el-inbound-marketing/", "/wp-json/", "/dev/", "/dev/contacto/",
              "/blog/14-que-es-el-inbound-marketing", "/wp-admin/"):
        r = requests.get(SITE + p, headers=UA, timeout=30, allow_redirects=False)
        print(f"fix_raiz: después {p} -> {r.status_code} {r.headers.get('location') or ''}")


if __name__ == "__main__":
    main()
