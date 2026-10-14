# fernandomartinez-content

Contenido de www.fernandomartinez.mx publicado en WordPress desde Markdown. Los archivos de WordPress viven en `/dev` y el sitio se sirve desde la raíz (ver `migracion/raiz`).

- `content/`: entradas y páginas en Markdown con frontmatter. Cada push a `main` publica lo que cambió.
- `scripts/publish.py`: convierte el Markdown y lo manda por la API REST.
- `.github/workflows/publish.yml`: workflow "Publicar en WordPress" (modo manual `check` para probar credenciales).
- `wordpress/mu-plugins/agente-auth.php`: va en `wp-content/mu-plugins/` del sitio.
- `registro/ultima-publicacion.log`: resultado de la última ejecución.

Secretos en GitHub: `WP_URL` (`https://www.fernandomartinez.mx/dev`), `WP_USER`, `WP_APP_PASSWORD`.
Al migrar a la raíz solo cambia `WP_URL`.
