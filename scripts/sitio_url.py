"""URL base del WordPress publicado.

El sitio vivió en /dev mientras se construía y el 14 de octubre de 2026 se pasó a la raíz.
El secreto WP_URL puede seguir terminando en /dev: aquí se quita, para no depender de cambiarlo.
SITE_URL, si existe, tiene prioridad.
"""
import os
import re


def base_url():
    url = (os.environ.get("SITE_URL") or os.environ.get("WP_URL") or "").strip().rstrip("/")
    if not url:
        raise SystemExit("Falta la variable de entorno WP_URL")
    return re.sub(r"/dev$", "", url)
