# fernandomartinez-content

Contenido de www.fernandomartinez.mx publicado en WordPress desde Markdown. WordPress vive en la raíz desde el 14 de octubre de 2026.

- `content/`: entradas y páginas en Markdown con frontmatter. Cada push a `main` publica lo que cambió.
- `scripts/publish.py`: convierte el Markdown y lo manda por la API REST.
- `.github/workflows/publish.yml`: workflow "Publicar en WordPress" (modo manual `check` para probar credenciales).
- `wordpress/mu-plugins/agente-auth.php`: va en `wp-content/mu-plugins/` del sitio.
- `registro/ultima-publicacion.log`: resultado de la última ejecución.

Secretos en GitHub: `WP_URL` (puede seguir en `/dev`: los scripts lo quitan, ver `scripts/sitio_url.py`), `WP_USER`, `WP_APP_PASSWORD`.
