#!/usr/bin/env python3
"""Rastrea el sitio Joomla actual y guarda cada página (HTML crudo + contenido extraído + enlaces).

Salida en migracion/origen/:
    paginas/<slug>.html     HTML completo tal como lo sirve el sitio
    inventario.json         por URL: título, meta descripción, fecha, cuerpo HTML, enlaces, imágenes
"""
import json
import pathlib
import re
import sys
import time
from collections import deque
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "migracion" / "origen"
BASE = "https://www.fernandomartinez.mx"
HOSTS = {"fernandomartinez.mx", "www.fernandomartinez.mx"}
SKIP = re.compile(r"^/(dev|images|media|templates|cdn-cgi|component|administrator|plugins|modules|cache|tmp)(/|$)|\.(jpg|jpeg|png|gif|webp|svg|pdf|zip|css|js|xml|ico|mp4)$", re.I)
UA = {"User-Agent": "fm-migracion/1.0 (+https://www.fernandomartinez.mx)"}


def norm(url):
    url, _ = urldefrag(url)
    p = urlparse(url)
    if p.scheme not in ("http", "https") or p.netloc.lower() not in HOSTS:
        return None
    path = p.path or "/"
    if SKIP.search(path):
        return None
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    q = p.query
    # Conservar solo la paginación del blog/categorías; descartar format=feed, print, etc.
    if q:
        m = re.search(r"(?:^|&)(start|limitstart)=(\d+)", q)
        if not m or re.search(r"(format|print|tmpl|task)=", q):
            return None
        q = f"start={m.group(2)}"
    return BASE + path + (f"?{q}" if q else "")


def body_of(soup):
    for sel in ['[itemprop="articleBody"]', ".item-page", ".blog", ".category-list", "#content", "main", ".content"]:
        el = soup.select_one(sel)
        if el and len(el.get_text(strip=True)) > 40:
            return el
    return soup.body


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "paginas").mkdir(exist_ok=True)
    s = requests.Session()
    s.headers.update(UA)
    seeds = [BASE + "/", BASE + "/mapa-de-sitio", BASE + "/blog", BASE + "/recursos", BASE + "/temas",
             BASE + "/base-de-conocimiento", BASE + "/enlaces-recomendados"]
    # sitemap.xml si existe
    try:
        r = s.get(BASE + "/sitemap.xml", timeout=30)
        if r.ok and "<loc>" in r.text:
            seeds += re.findall(r"<loc>([^<]+)</loc>", r.text)
            print(f"sitemap.xml: {r.text.count('<loc>')} URLs")
    except Exception as e:  # noqa: BLE001
        print("sin sitemap.xml:", e)

    queue = deque(filter(None, (norm(u) for u in seeds)))
    seen, inv = set(queue), {}
    while queue and len(inv) < 600:
        url = queue.popleft()
        try:
            r = s.get(url, timeout=30)
        except Exception as e:  # noqa: BLE001
            inv[url] = {"error": str(e)}
            continue
        final = r.url
        rec = {"status": r.status_code, "final_url": final}
        if not r.ok or "text/html" not in r.headers.get("content-type", ""):
            inv[url] = rec
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        slug = re.sub(r"[^a-z0-9]+", "-", urlparse(url).path.lower() + "-" + urlparse(url).query).strip("-") or "inicio"
        (OUT / "paginas" / f"{slug}.html").write_text(r.text, encoding="utf-8")
        body = body_of(soup)
        def meta(name, attr="name"):
            t = soup.find("meta", attrs={attr: name})
            return t.get("content") if t else None
        time_el = soup.select_one("time[datetime]")
        rec.update({
            "file": f"paginas/{slug}.html",
            "title": soup.title.get_text(strip=True) if soup.title else None,
            "h1": (soup.select_one("h1, h2[itemprop=headline], .page-header h2") or soup.new_tag("x")).get_text(" ", strip=True),
            "description": meta("description"),
            "keywords": meta("keywords"),
            "og_image": meta("og:image", "property"),
            "canonical": (soup.find("link", rel="canonical") or {}).get("href") if soup.find("link", rel="canonical") else None,
            "date": time_el.get("datetime") if time_el else None,
            "body_html": str(body) if body else "",
            "body_text_len": len(body.get_text(" ", strip=True)) if body else 0,
            "links": [{"href": a.get("href"), "text": a.get_text(" ", strip=True), "rel": a.get("rel"), "target": a.get("target")}
                      for a in (body.find_all("a") if body else []) if a.get("href")],
            "images": [{"src": i.get("src"), "alt": i.get("alt")} for i in (body.find_all("img") if body else [])],
        })
        inv[url] = rec
        for a in soup.find_all("a", href=True):
            n = norm(urljoin(final, a["href"]))
            if n and n not in seen:
                seen.add(n)
                queue.append(n)
        time.sleep(0.3)
        print(f"{r.status_code} {url}")

    (OUT / "inventario.json").write_text(json.dumps(inv, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Total URLs: {len(inv)}")


if __name__ == "__main__":
    sys.exit(main())
