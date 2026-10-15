---
title: "Cómo reducir el tiempo de carga de un sitio Joomla (edición Joomla 5 y 6)"
slug: reducir-tiempo-carga-sitio-web-joomla
type: post
status: publish
date: 2026-10-13 09:30
original: /blog/15-reducir-tiempo-carga-sitio-web-joomla
excerpt: "Pasos para que tu sitio Joomla cargue rápido y apruebe las Core Web Vitals: caché, compresión, imágenes, plantilla y servidor. Actualizado para las versiones actuales."
seo_title: "Reducir el tiempo de carga en Joomla"
seo_description: "Pasos para que tu sitio Joomla 5 o 6 cargue rápido y apruebe las Core Web Vitals: caché, compresión, imágenes, plantilla y servidor."
focus_keyword: "tiempo de carga joomla"
categories: [seo-y-geo, desarrollo-web]
tags: [Joomla, velocidad web, Core Web Vitals, optimización, SEO técnico]
featured_image: images/reducir-tiempo-carga-sitio-web-joomla.png
featured_alt: "Portada: cómo reducir el tiempo de carga de un sitio Joomla"
---

Hace años esta guía era de las más visitadas de mi blog. Tenía una receta para pasar de un Joomla lento a calificaciones de 90 o más en PageSpeed Insights. Muchas cosas siguen funcionando. Otras cambiaron: Joomla ya va en la versión 6, Google mide la velocidad con las Core Web Vitals y algunas extensiones que recomendaba ya no son la mejor opción.

<div class="fm-tldr" markdown="1">
**La versión corta:** actualiza Joomla y PHP, activa la caché y la compresión, optimiza las imágenes (formatos modernos y tamaños correctos), usa una plantilla ligera y mide con PageSpeed Insights antes y después de cada cambio. El servidor importa más de lo que parece.
</div>

## Por qué importa

Un sitio rápido mejora la experiencia, ayuda en buscadores, gasta menos recursos del servidor y consume menos datos del celular de tu cliente. Y desde que Google usa las [Core Web Vitals](https://web.dev/articles/vitals) (velocidad de carga del contenido principal, respuesta a la interacción y estabilidad visual), la velocidad dejó de ser un capricho técnico.

El mito de que "un CMS siempre es más lento que un sitio a la medida" ya casi nadie lo repite. Joomla bien configurado es rápido.

## 1. Antes de empezar

Optimiza cuando el sitio esté completo y con la mayor parte del contenido cargado. Optimizar a mitad del desarrollo es repetir el trabajo.

Y mide primero en [PageSpeed Insights](https://pagespeed.web.dev/). Sin una medición inicial no sabrás qué funcionó.

## 2. Actualiza Joomla y PHP

Es el cambio más barato y el que más se olvida. Las versiones recientes de Joomla y de PHP son notablemente más rápidas que las viejas. Si tu sitio sigue en Joomla 3, que dejó de tener soporte en 2023, la velocidad es el menor de tus problemas: empieza por migrar.

## 3. Activa la caché y la compresión

En la **Configuración global**:

- **Compresión Gzip de la página:** activada (si tu servidor no comprime ya).
- **Caché:** activada en modo conservador.

Y en **Plugins**, activa **Sistema - Caché de página** para servir versiones estáticas de las páginas a visitantes no registrados.

## 4. Configura el servidor (.htaccess)

Si tu hosting usa Apache, puedes agregar reglas de compresión y caducidad de recursos al final del archivo `.htaccess`. Una versión actualizada y más corta que la que publiqué originalmente:

```
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/plain text/css text/xml application/javascript application/json application/xml image/svg+xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresDefault "access plus 1 hour"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType image/webp "access plus 6 months"
  ExpiresByType image/avif "access plus 6 months"
  ExpiresByType image/jpeg "access plus 6 months"
  ExpiresByType image/png "access plus 6 months"
  ExpiresByType image/svg+xml "access plus 6 months"
  ExpiresByType font/woff2 "access plus 1 year"
</IfModule>
```

Haz un respaldo del `.htaccess` antes de tocarlo. Si tu sitio corre en LiteSpeed o Nginx, la configuración es distinta y conviene pedirla a tu proveedor.

## 5. Optimiza las imágenes

En la mayoría de los sitios lentos que he revisado, las imágenes eran el problema número uno.

- Usa **WebP o AVIF**.
- Sube las imágenes **al tamaño en que se muestran**, no la foto de 6,000 pixeles de la cámara.
- Activa la **carga diferida** (lazy loading), que Joomla ya incluye.

## 6. Elige una plantilla ligera

Las plantillas comerciales con constructores visuales suelen cargar mucho código que no usas. La plantilla incluida en Joomla (Cassiopeia) es una buena base ligera. Si usas una comercial, activa sus opciones de minificación y combinación de archivos.

## 7. Considera JCH Optimize

[JCH Optimize](https://www.jch-optimize.net/) sigue siendo una de las extensiones más conocidas para combinar y minificar CSS y JavaScript en Joomla. Configúralo con calma y prueba cada cambio: combinar archivos a ciegas puede romper funciones del sitio.

## 8. No subestimes el hosting

Un buen servidor con PHP actualizado, caché del lado del servidor y una red de distribución de contenido (CDN) puede hacer más por tu sitio que cualquier extensión.

<div class="fm-cta" markdown="1">
¿Pensando si seguir en Joomla o cambiar de plataforma? Te cuento mi opinión en [esta página](/programador-web-especialista-en-joomla-en-mexico/), y si buscas quién te ayude, lee [cómo elegir a un experto en Joomla en México](/blog/experto-en-joomla-en-mexico/).
</div>
