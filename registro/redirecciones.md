# Prueba de redirecciones: Apache local con migracion/redirecciones.htaccess, destinos en https://www.fernandomartinez.mx/dev

- URLs viejas probadas: **418**
- Correctas (301 a una página que responde 200, o URL que se conserva igual): **417**
- Para revisar: **1**
- Sin equivalente o con error: **0**

## Sitemaps del sitio actual

| Sitemap | HTTP | URLs |
|---|---|---|
| https://www.fernandomartinez.mx/sitemap.xml | 404 | 0 |
| https://www.fernandomartinez.mx/sitemap_index.xml | 404 | 0 |
| https://www.fernandomartinez.mx/index.php?option=com_osmap&view=xml&id=1 | 200 | 0 |
| https://www.fernandomartinez.mx/component/osmap/?view=xml&id=1 | 200 | 0 |
| https://www.fernandomartinez.mx/index.php?option=com_xmap&view=xml&id=1 | 404 | 0 |
| https://www.fernandomartinez.mx/component/xmap/?view=xml&id=1 | 404 | 0 |
| https://www.fernandomartinez.mx/index.php?option=com_jmap&view=sitemap&format=xml | 500 | 0 |

## Errores y casos a revisar

| Estado | URL vieja | Origen | Destino | Detalle |
|---|---|---|---|---|
| REVISAR | /index.php | variante index.php | /index.php | WordPress además redirige a /dev/ |

## Todas

| Estado | URL vieja | Origen | Saltos | Destino |
|---|---|---|---|---|
| ok | / | rastreo | 0 | / |
| ok | /base-de-conocimiento | rastreo | 1 | /recursos/ |
| ok | /base-de-conocimiento/ | variante con diagonal | 1 | /recursos/ |
| ok | /blog | rastreo | 0 | /blog |
| ok | /blog/ | variante con diagonal | 0 | /blog/ |
| ok | /blog/12-entre-aportar-al-teleton-y-el-odio-a-televisa | rastreo | 1 | /blog/entre-aportar-al-teleton-y-el-odio-a-televisa/ |
| ok | /blog/12-entre-aportar-al-teleton-y-el-odio-a-televisa/ | variante con diagonal | 1 | /blog/entre-aportar-al-teleton-y-el-odio-a-televisa/ |
| ok | /blog/13-como-funciona-los-5-pilares-del-inbound-marketing | rastreo | 1 | /blog/como-funciona-los-5-pilares-del-inbound-marketing/ |
| ok | /blog/13-como-funciona-los-5-pilares-del-inbound-marketing/ | variante con diagonal | 1 | /blog/como-funciona-los-5-pilares-del-inbound-marketing/ |
| ok | /blog/14-que-es-el-inbound-marketing | rastreo | 1 | /blog/que-es-el-inbound-marketing/ |
| ok | /blog/14-que-es-el-inbound-marketing/ | variante con diagonal | 1 | /blog/que-es-el-inbound-marketing/ |
| ok | /blog/15-reducir-tiempo-carga-sitio-web-joomla | rastreo | 1 | /blog/reducir-tiempo-carga-sitio-web-joomla/ |
| ok | /blog/15-reducir-tiempo-carga-sitio-web-joomla/ | variante con diagonal | 1 | /blog/reducir-tiempo-carga-sitio-web-joomla/ |
| ok | /blog/16-para-que-sirve-un-blog-en-mi-sitio-web | rastreo | 1 | /blog/para-que-sirve-un-blog-en-mi-sitio-web/ |
| ok | /blog/16-para-que-sirve-un-blog-en-mi-sitio-web/ | variante con diagonal | 1 | /blog/para-que-sirve-un-blog-en-mi-sitio-web/ |
| ok | /blog/17-10-palabras-que-debes-quitar-de-tu-sitio-web-ya | rastreo | 1 | /blog/10-palabras-que-debes-quitar-de-tu-sitio-web-ya/ |
| ok | /blog/17-10-palabras-que-debes-quitar-de-tu-sitio-web-ya/ | variante con diagonal | 1 | /blog/10-palabras-que-debes-quitar-de-tu-sitio-web-ya/ |
| ok | /blog/2-5-cosas-que-hace-la-gente-super-exitosa | rastreo | 1 | /blog/5-cosas-que-hace-la-gente-super-exitosa/ |
| ok | /blog/2-5-cosas-que-hace-la-gente-super-exitosa/ | variante con diagonal | 1 | /blog/5-cosas-que-hace-la-gente-super-exitosa/ |
| ok | /blog/20-la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas | rastreo | 1 | /blog/la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas/ |
| ok | /blog/20-la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas/ | variante con diagonal | 1 | /blog/la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas/ |
| ok | /blog/22-plantillas-administrador-joomla | rastreo | 1 | /blog/plantillas-administrador-joomla/ |
| ok | /blog/22-plantillas-administrador-joomla/ | variante con diagonal | 1 | /blog/plantillas-administrador-joomla/ |
| ok | /blog/24-inbound-marketing-audiencia-ideal | rastreo | 1 | /blog/inbound-marketing-audiencia-ideal/ |
| ok | /blog/24-inbound-marketing-audiencia-ideal/ | variante con diagonal | 1 | /blog/inbound-marketing-audiencia-ideal/ |
| ok | /blog/26-que-es-el-internet-de-las-cosas-iot-internet-of-things | rastreo | 1 | /blog/que-es-el-internet-de-las-cosas-iot-internet-of-things/ |
| ok | /blog/26-que-es-el-internet-de-las-cosas-iot-internet-of-things/ | variante con diagonal | 1 | /blog/que-es-el-internet-de-las-cosas-iot-internet-of-things/ |
| ok | /blog/27-como-identificar-y-crear-mis-buyer-personas | rastreo | 1 | /blog/como-identificar-y-crear-mis-buyer-personas/ |
| ok | /blog/27-como-identificar-y-crear-mis-buyer-personas/ | variante con diagonal | 1 | /blog/como-identificar-y-crear-mis-buyer-personas/ |
| ok | /blog/28-como-enriquecer-mi-base-de-datos-de-clientes-para-mi-estrategia-de-marketing-digital | rastreo | 1 | /blog/como-enriquecer-tu-base-de-datos-de-clientes/ |
| ok | /blog/28-como-enriquecer-mi-base-de-datos-de-clientes-para-mi-estrategia-de-marketing-digital/ | variante con diagonal | 1 | /blog/como-enriquecer-tu-base-de-datos-de-clientes/ |
| ok | /blog/29-los-consumidores-tienen-el-control | rastreo | 1 | /blog/los-consumidores-tienen-el-control/ |
| ok | /blog/29-los-consumidores-tienen-el-control/ | variante con diagonal | 1 | /blog/los-consumidores-tienen-el-control/ |
| ok | /blog/3-como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas | rastreo | 1 | /blog/como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas/ |
| ok | /blog/3-como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas/ | variante con diagonal | 1 | /blog/como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas/ |
| ok | /blog/31-physical-web-el-nuevo-paso-para-los-negocios | rastreo | 1 | /blog/physical-web-el-nuevo-paso-para-los-negocios/ |
| ok | /blog/31-physical-web-el-nuevo-paso-para-los-negocios/ | variante con diagonal | 1 | /blog/physical-web-el-nuevo-paso-para-los-negocios/ |
| ok | /blog/32-deberias-ofrecer-wi-fi-gratis-en-tu-negocio | rastreo | 1 | /blog/deberias-ofrecer-wi-fi-gratis-en-tu-negocio/ |
| ok | /blog/32-deberias-ofrecer-wi-fi-gratis-en-tu-negocio/ | variante con diagonal | 1 | /blog/deberias-ofrecer-wi-fi-gratis-en-tu-negocio/ |
| ok | /blog/33-el-uso-de-la-redes-sociales-lo-definen-los-usuarios | rastreo | 1 | /blog/el-uso-de-las-redes-sociales-lo-definen-los-usuarios/ |
| ok | /blog/33-el-uso-de-la-redes-sociales-lo-definen-los-usuarios/ | variante con diagonal | 1 | /blog/el-uso-de-las-redes-sociales-lo-definen-los-usuarios/ |
| ok | /blog/34-5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales | rastreo | 1 | /blog/5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales/ |
| ok | /blog/34-5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales/ | variante con diagonal | 1 | /blog/5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales/ |
| ok | /blog/35-3-formas-de-hacer-marketing-digital-con-realidad-virtual | rastreo | 1 | /blog/3-formas-de-hacer-marketing-digital-con-realidad-virtual/ |
| ok | /blog/35-3-formas-de-hacer-marketing-digital-con-realidad-virtual/ | variante con diagonal | 1 | /blog/3-formas-de-hacer-marketing-digital-con-realidad-virtual/ |
| ok | /blog/36-porque-deberias-considerar-el-inbound-marketing | rastreo | 1 | /blog/por-que-deberias-considerar-el-inbound-marketing/ |
| ok | /blog/36-porque-deberias-considerar-el-inbound-marketing/ | variante con diagonal | 1 | /blog/por-que-deberias-considerar-el-inbound-marketing/ |
| ok | /blog/37-marketing-automotriz-en-los-juegos-olimpicos | rastreo | 1 | /blog/marketing-automotriz-en-los-juegos-olimpicos/ |
| ok | /blog/37-marketing-automotriz-en-los-juegos-olimpicos/ | variante con diagonal | 1 | /blog/marketing-automotriz-en-los-juegos-olimpicos/ |
| ok | /blog/38-como-aprovechar-instagram-stories-en-tu-marketing | rastreo | 1 | /blog/como-aprovechar-instagram-stories-en-tu-marketing/ |
| ok | /blog/38-como-aprovechar-instagram-stories-en-tu-marketing/ | variante con diagonal | 1 | /blog/como-aprovechar-instagram-stories-en-tu-marketing/ |
| ok | /blog/39-como-abrir-una-tienda-en-linea-en-mexico-con-shopify | rastreo | 1 | /blog/como-abrir-una-tienda-en-linea-en-mexico-con-shopify/ |
| ok | /blog/39-como-abrir-una-tienda-en-linea-en-mexico-con-shopify/ | variante con diagonal | 1 | /blog/como-abrir-una-tienda-en-linea-en-mexico-con-shopify/ |
| ok | /blog/40-5-datos-duros-para-considerar-implementar-un-chat | rastreo | 1 | /blog/5-datos-duros-para-considerar-implementar-un-chat/ |
| ok | /blog/40-5-datos-duros-para-considerar-implementar-un-chat/ | variante con diagonal | 1 | /blog/5-datos-duros-para-considerar-implementar-un-chat/ |
| ok | /blog/41-credito-automotriz-en-linea-disrupcion-venta-de-autos | rastreo | 1 | /blog/credito-automotriz-en-linea-disrupcion-venta-de-autos/ |
| ok | /blog/41-credito-automotriz-en-linea-disrupcion-venta-de-autos/ | variante con diagonal | 1 | /blog/credito-automotriz-en-linea-disrupcion-venta-de-autos/ |
| ok | /blog/5-activismo-con-hashtags | rastreo | 1 | /blog/activismo-con-hashtags/ |
| ok | /blog/5-activismo-con-hashtags/ | variante con diagonal | 1 | /blog/activismo-con-hashtags/ |
| ok | /blog/6-crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion | rastreo | 1 | /blog/crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion/ |
| ok | /blog/6-crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion/ | variante con diagonal | 1 | /blog/crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion/ |
| ok | /blog/7-manifiesto-de-marketing-digital-de-fernando-martinez | rastreo | 1 | /blog/manifiesto-de-marketing-digital-de-fernando-martinez/ |
| ok | /blog/7-manifiesto-de-marketing-digital-de-fernando-martinez/ | variante con diagonal | 1 | /blog/manifiesto-de-marketing-digital-de-fernando-martinez/ |
| ok | /blog/9-en-contra-de-la-tolerancia | rastreo | 1 | /blog/en-contra-de-la-tolerancia/ |
| ok | /blog/9-en-contra-de-la-tolerancia/ | variante con diagonal | 1 | /blog/en-contra-de-la-tolerancia/ |
| ok | /blog?format=feed&type=rss | variante feed | 1 | /feed/ |
| ok | /blog?start=10 | rastreo | 1 | /blog/ |
| ok | /blog?start=15 | rastreo | 1 | /blog/ |
| ok | /blog?start=20 | rastreo | 1 | /blog/ |
| ok | /blog?start=25 | rastreo | 1 | /blog/ |
| ok | /blog?start=5 | rastreo | 1 | /blog/ |
| ok | /busqueda | rastreo | 1 | /blog/ |
| ok | /busqueda/ | variante con diagonal | 1 | /blog/ |
| ok | /component/weblinks/?task=weblink.go&catid=17:guias-para-principiantes&id=35:googles-seo-guide | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /component/weblinks/?task=weblink.go&catid=17:guias-para-principiantes&id=36:bing-webmaster-guide | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /component/weblinks/?task=weblink.go&catid=17:guias-para-principiantes&id=37:plato-web-design-seo-guide | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /contacto | rastreo | 0 | /contacto |
| ok | /contacto/ | variante con diagonal | 0 | /contacto/ |
| ok | /enlaces-recomendados | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/14-pruebas-a-b | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/14-pruebas-a-b/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/15-publicidad-y-promocion | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/15-publicidad-y-promocion/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/16-analisis-y-metricas | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/16-analisis-y-metricas/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/17-guias-para-principiantes | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/17-guias-para-principiantes/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/18-blogs | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/18-blogs/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/19-conferencias | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/19-conferencias/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/20-marketing-de-contenidos | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/20-marketing-de-contenidos/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/21-correo-electronico | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/21-correo-electronico/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/34-herramientas | rastreo | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados/34-herramientas/ | variante con diagonal | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=1 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=10 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=100 | weblink | 1 | https://shopify.pxf.io/prueba-gratis-shop |
| ok | /enlaces-recomendados?task=weblink.go&id=11 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=12 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=13 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=14 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=15 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=16 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=17 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=18 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=19 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=2 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=20 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=21 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=22 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=23 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=24 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=25 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=26 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=27 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=28 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=29 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=3 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=30 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=31 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=32 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=33 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=34 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=35 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=36 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=37 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=38 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=39 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=4 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=40 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=41 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=42 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=43 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=44 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=45 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=46 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=47 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=48 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=49 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=5 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=50 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=51 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=52 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=53 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=54 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=55 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=56 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=57 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=58 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=59 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=6 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=60 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=61 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=62 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=63 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=64 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=65 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=66 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=67 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=68 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=69 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=7 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=70 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=71 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=72 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=73 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=74 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=75 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=76 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=77 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=78 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=79 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=8 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=80 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=81 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=82 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=83 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=84 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=85 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=86 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=87 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=88 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=89 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=9 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=90 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=91 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=92 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=93 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=94 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=95 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=96 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=97 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=98 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /enlaces-recomendados?task=weblink.go&id=99 | weblink | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /fernando-arturo-martinez-aguilar | rastreo | 0 | /fernando-arturo-martinez-aguilar |
| ok | /fernando-arturo-martinez-aguilar/ | variante con diagonal | 0 | /fernando-arturo-martinez-aguilar/ |
| ok | /gnu-general-public-license | rastreo | 0 | /gnu-general-public-license |
| ok | /gnu-general-public-license/ | variante con diagonal | 0 | /gnu-general-public-license/ |
| ok | /images/blog/10-palabras-que-debes-quitar-de-tu-sitio-web-ya.png | imagen | 1 | /blog/10-palabras-que-debes-quitar-de-tu-sitio-web-ya/ |
| ok | /images/blog/5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales.png | imagen | 1 | /blog/5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales/ |
| ok | /images/blog/activismo-con-hashtags.png | imagen | 1 | /blog/activismo-con-hashtags/ |
| ok | /images/blog/como-aprovechar-instagram-stories-en-tu-marketing.png | imagen | 1 | /blog/como-aprovechar-instagram-stories-en-tu-marketing/ |
| ok | /images/blog/como-funciona-los-5-pilares-del-inbound-marketing.png | imagen | 1 | /blog/como-funciona-los-5-pilares-del-inbound-marketing/ |
| ok | /images/blog/como-identificar-y-crear-mis-buyer-personas.png | imagen | 1 | /blog/como-identificar-y-crear-mis-buyer-personas/ |
| ok | /images/blog/compensacion-ventas.png | imagen | 1 | /blog/como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas/ |
| ok | /images/blog/crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion.png | imagen | 1 | /blog/crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion/ |
| ok | /images/blog/deberias-ofrecer-wi-fi-gratis-en-tu-negocio.png | imagen | 1 | /blog/deberias-ofrecer-wi-fi-gratis-en-tu-negocio/ |
| ok | /images/blog/ecommerce-mistakes.jpg | imagen | 1 | /blog/como-abrir-una-tienda-en-linea-en-mexico-con-shopify/ |
| ok | /images/blog/el-uso-de-la-redes-sociales-lo-definen-los-usuarios.png | imagen | 1 | /blog/el-uso-de-las-redes-sociales-lo-definen-los-usuarios/ |
| ok | /images/blog/file.JPG | imagen | 1 | /blog/physical-web-el-nuevo-paso-para-los-negocios/ |
| ok | /images/blog/implementar-chat-online-mexico.jpg | imagen | 1 | /blog/5-datos-duros-para-considerar-implementar-un-chat/ |
| ok | /images/blog/inbound-marketing-audiencia-ideal.png | imagen | 1 | /blog/inbound-marketing-audiencia-ideal/ |
| ok | /images/blog/la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas.png | imagen | 1 | /blog/la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas/ |
| ok | /images/blog/manifiesto-de-marketing-digital-de-fernando-martinez.png | imagen | 1 | /blog/manifiesto-de-marketing-digital-de-fernando-martinez/ |
| ok | /images/blog/marketing-automotriz-en-los-juegos-olimpicos.png | imagen | 1 | /blog/marketing-automotriz-en-los-juegos-olimpicos/ |
| ok | /images/blog/marketing-realidad-virtual.png | imagen | 1 | /blog/3-formas-de-hacer-marketing-digital-con-realidad-virtual/ |
| ok | /images/blog/plantillas-administrador-joomla.png | imagen | 1 | /blog/plantillas-administrador-joomla/ |
| ok | /images/blog/porque-deberias-considerar-el-inbound-marketing.png | imagen | 1 | /blog/por-que-deberias-considerar-el-inbound-marketing/ |
| ok | /images/blog/que-es-el-inbound-marketing.png | imagen | 1 | /blog/que-es-el-inbound-marketing/ |
| ok | /images/credito-automotriz-en-linea-disrupcion-venta-de-autos.png | imagen | 1 | /blog/credito-automotriz-en-linea-disrupcion-venta-de-autos/ |
| ok | /images/cta/cta-25-cosas-hacer-web-tener-mas-clientes.png | imagen | 1 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ |
| ok | /images/fernando-martinez-enginecx.png | imagen | 1 | /fernando-arturo-martinez-aguilar/ |
| ok | /images/fernando-martinez.png | imagen | 1 | / |
| ok | /images/phocagallery/muestra/thumbs/phoca_thumb_m_ejemplo.jpg | imagen galería | 1 | /recursos/imagenes-libres-de-derechos-gratis/ |
| ok | /images/recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes.png | imagen | 1 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ |
| ok | /images/recursos/TwitterSummaryCardforArticles.png | imagen | 1 | /recursos/twitter-summary-card-for-joomla-articles-plugin/ |
| ok | /images/recursos/imagenes-libres-de-derechos-gratis.png | imagen | 1 | /recursos/imagenes-libres-de-derechos-gratis/ |
| ok | /images/recursos/joomla-brand-remover-administrator-plugin.png | imagen | 1 | /recursos/administration-brand-remover-joomla-plugin/ |
| ok | /images/recursos/joomla-website-preloader.jpg | imagen | 1 | /recursos/website-preloader-joomla-plugin/ |
| ok | /images/recursos/las-mejores-herramientas-para-hacer-seo-e-inbound-marketing.png | imagen | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /images/recursos/screenshots/joomla-administration-brand-remover-1.png | imagen | 1 | /recursos/administration-brand-remover-joomla-plugin/ |
| ok | /images/recursos/screenshots/joomla-administration-brand-remover-2.png | imagen | 1 | /recursos/administration-brand-remover-joomla-plugin/ |
| ok | /images/recursos/screenshots/twitter-summary-card-joomla.jpg | imagen | 1 | /recursos/twitter-summary-card-for-joomla-articles-plugin/ |
| ok | /images/recursos/sumome-joomla-plugin.png | imagen | 1 | /recursos/sumome-joomla-plugin/ |
| REVISAR | /index.php | variante index.php | 0 | /index.php |
| ok | /index.php/base-de-conocimiento | variante index.php | 2 | /recursos/ |
| ok | /index.php/blog | variante index.php | 1 | /blog |
| ok | /index.php/blog/12-entre-aportar-al-teleton-y-el-odio-a-televisa | variante index.php | 2 | /blog/entre-aportar-al-teleton-y-el-odio-a-televisa/ |
| ok | /index.php/blog/13-como-funciona-los-5-pilares-del-inbound-marketing | variante index.php | 2 | /blog/como-funciona-los-5-pilares-del-inbound-marketing/ |
| ok | /index.php/blog/14-que-es-el-inbound-marketing | variante index.php | 2 | /blog/que-es-el-inbound-marketing/ |
| ok | /index.php/blog/15-reducir-tiempo-carga-sitio-web-joomla | variante index.php | 2 | /blog/reducir-tiempo-carga-sitio-web-joomla/ |
| ok | /index.php/blog/16-para-que-sirve-un-blog-en-mi-sitio-web | variante index.php | 2 | /blog/para-que-sirve-un-blog-en-mi-sitio-web/ |
| ok | /index.php/blog/17-10-palabras-que-debes-quitar-de-tu-sitio-web-ya | variante index.php | 2 | /blog/10-palabras-que-debes-quitar-de-tu-sitio-web-ya/ |
| ok | /index.php/blog/2-5-cosas-que-hace-la-gente-super-exitosa | variante index.php | 2 | /blog/5-cosas-que-hace-la-gente-super-exitosa/ |
| ok | /index.php/blog/20-la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas | variante index.php | 2 | /blog/la-grave-desconexion-entre-el-reconocimiento-de-marca-y-las-ventas/ |
| ok | /index.php/blog/22-plantillas-administrador-joomla | variante index.php | 2 | /blog/plantillas-administrador-joomla/ |
| ok | /index.php/blog/24-inbound-marketing-audiencia-ideal | variante index.php | 2 | /blog/inbound-marketing-audiencia-ideal/ |
| ok | /index.php/blog/26-que-es-el-internet-de-las-cosas-iot-internet-of-things | variante index.php | 2 | /blog/que-es-el-internet-de-las-cosas-iot-internet-of-things/ |
| ok | /index.php/blog/27-como-identificar-y-crear-mis-buyer-personas | variante index.php | 2 | /blog/como-identificar-y-crear-mis-buyer-personas/ |
| ok | /index.php/blog/28-como-enriquecer-mi-base-de-datos-de-clientes-para-mi-estrategia-de-marketing-digital | variante index.php | 2 | /blog/como-enriquecer-tu-base-de-datos-de-clientes/ |
| ok | /index.php/blog/29-los-consumidores-tienen-el-control | variante index.php | 2 | /blog/los-consumidores-tienen-el-control/ |
| ok | /index.php/blog/3-como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas | variante index.php | 2 | /blog/como-crear-un-plan-de-compensacion-para-tu-equipo-de-ventas/ |
| ok | /index.php/blog/31-physical-web-el-nuevo-paso-para-los-negocios | variante index.php | 2 | /blog/physical-web-el-nuevo-paso-para-los-negocios/ |
| ok | /index.php/blog/32-deberias-ofrecer-wi-fi-gratis-en-tu-negocio | variante index.php | 2 | /blog/deberias-ofrecer-wi-fi-gratis-en-tu-negocio/ |
| ok | /index.php/blog/33-el-uso-de-la-redes-sociales-lo-definen-los-usuarios | variante index.php | 2 | /blog/el-uso-de-las-redes-sociales-lo-definen-los-usuarios/ |
| ok | /index.php/blog/34-5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales | variante index.php | 2 | /blog/5-ideas-para-fortalecer-tu-marketing-digital-en-redes-sociales/ |
| ok | /index.php/blog/35-3-formas-de-hacer-marketing-digital-con-realidad-virtual | variante index.php | 2 | /blog/3-formas-de-hacer-marketing-digital-con-realidad-virtual/ |
| ok | /index.php/blog/36-porque-deberias-considerar-el-inbound-marketing | variante index.php | 2 | /blog/por-que-deberias-considerar-el-inbound-marketing/ |
| ok | /index.php/blog/37-marketing-automotriz-en-los-juegos-olimpicos | variante index.php | 2 | /blog/marketing-automotriz-en-los-juegos-olimpicos/ |
| ok | /index.php/blog/38-como-aprovechar-instagram-stories-en-tu-marketing | variante index.php | 2 | /blog/como-aprovechar-instagram-stories-en-tu-marketing/ |
| ok | /index.php/blog/39-como-abrir-una-tienda-en-linea-en-mexico-con-shopify | variante index.php | 2 | /blog/como-abrir-una-tienda-en-linea-en-mexico-con-shopify/ |
| ok | /index.php/blog/40-5-datos-duros-para-considerar-implementar-un-chat | variante index.php | 2 | /blog/5-datos-duros-para-considerar-implementar-un-chat/ |
| ok | /index.php/blog/41-credito-automotriz-en-linea-disrupcion-venta-de-autos | variante index.php | 2 | /blog/credito-automotriz-en-linea-disrupcion-venta-de-autos/ |
| ok | /index.php/blog/5-activismo-con-hashtags | variante index.php | 2 | /blog/activismo-con-hashtags/ |
| ok | /index.php/blog/6-crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion | variante index.php | 2 | /blog/crear-lealtad-a-tu-marca-no-se-logra-solo-con-comunicacion/ |
| ok | /index.php/blog/7-manifiesto-de-marketing-digital-de-fernando-martinez | variante index.php | 2 | /blog/manifiesto-de-marketing-digital-de-fernando-martinez/ |
| ok | /index.php/blog/9-en-contra-de-la-tolerancia | variante index.php | 2 | /blog/en-contra-de-la-tolerancia/ |
| ok | /index.php/busqueda | variante index.php | 2 | /blog/ |
| ok | /index.php/contacto | variante index.php | 1 | /contacto |
| ok | /index.php/enlaces-recomendados | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/14-pruebas-a-b | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/15-publicidad-y-promocion | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/16-analisis-y-metricas | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/17-guias-para-principiantes | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/18-blogs | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/19-conferencias | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/20-marketing-de-contenidos | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/21-correo-electronico | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/enlaces-recomendados/34-herramientas | variante index.php | 2 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /index.php/fernando-arturo-martinez-aguilar | variante index.php | 1 | /fernando-arturo-martinez-aguilar |
| ok | /index.php/gnu-general-public-license | variante index.php | 1 | /gnu-general-public-license |
| ok | /index.php/mapa-de-sitio | variante index.php | 2 | / |
| ok | /index.php/media/weTnwLzC8MAT47xS/25_cosas_que_hacer_en_la_web_para_tener_mas_trafico_y_clientes.pdf | variante index.php | 2 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ |
| ok | /index.php/media/weTnwLzC8MAT47xS/plg_TwitterSummaryCardforArticles.zip | variante index.php | 2 | /recursos/twitter-summary-card-for-joomla-articles-plugin/ |
| ok | /index.php/media/weTnwLzC8MAT47xS/plg_websitepreloader.zip | variante index.php | 2 | /recursos/website-preloader-joomla-plugin/ |
| ok | /index.php/programador-web-especialista-en-joomla-en-mexico | variante index.php | 1 | /programador-web-especialista-en-joomla-en-mexico |
| ok | /index.php/recursos | variante index.php | 1 | /recursos |
| ok | /index.php/recursos/11-imagenes-libres-de-derechos-gratis | variante index.php | 2 | /recursos/imagenes-libres-de-derechos-gratis/ |
| ok | /index.php/recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes | variante index.php | 1 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes |
| ok | /index.php/recursos/administration-brand-remover-joomla-plugin | variante index.php | 1 | /recursos/administration-brand-remover-joomla-plugin |
| ok | /index.php/recursos/imagenes-libres-de-derechos-gratis | variante index.php | 1 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /index.php/recursos/las-mejores-herramientas-de-seo-e-inbound-marketing | variante index.php | 1 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing |
| ok | /index.php/recursos/sumome-joomla-plugin | variante index.php | 1 | /recursos/sumome-joomla-plugin |
| ok | /index.php/recursos/twitter-summary-card-for-joomla-articles-plugin | variante index.php | 1 | /recursos/twitter-summary-card-for-joomla-articles-plugin |
| ok | /index.php/recursos/website-preloader-joomla-plugin | variante index.php | 1 | /recursos/website-preloader-joomla-plugin |
| ok | /index.php/temas | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/10-equipos-de-trabajo | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/11-marketing-digital | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/12-inbound-marketing | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/13-filosofia | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/14-ideologia | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/15-prosa | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/16-joomla | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/17-extensiones-de-joomla | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/18-optimizacion-de-sitios-web | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/19-experiencia-de-usuario | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/2-hubspot | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/20-programacion-de-sitios-web | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/21-blogs | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/22-programador-joomla | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/23-internet-de-las-cosas | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/24-internet | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/25-tecnologias-de-la-informacion | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/26-innovacion | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/3-ventas | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/4-redes-sociales | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/5-hashtags | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/6-activismo | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/7-comunidad | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/8-lealtad-de-marca | variante index.php | 2 | /blog/ |
| ok | /index.php/temas/9-seleccion-de-personal | variante index.php | 2 | /blog/ |
| ok | /index.php/usuario/inicio-de-sesion | variante index.php | 2 | / |
| ok | /index.php/usuario/registro | variante index.php | 2 | / |
| ok | /mapa-de-sitio | rastreo | 1 | / |
| ok | /mapa-de-sitio/ | variante con diagonal | 1 | / |
| ok | /media/weTnwLzC8MAT47xS/25_cosas_que_hacer_en_la_web_para_tener_mas_trafico_y_clientes.pdf | descarga | 1 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ |
| ok | /media/weTnwLzC8MAT47xS/25_cosas_que_hacer_en_la_web_para_tener_mas_trafico_y_clientes.pdf/ | variante con diagonal | 1 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ |
| ok | /media/weTnwLzC8MAT47xS/plg_TwitterSummaryCardforArticles.zip | descarga | 1 | /recursos/twitter-summary-card-for-joomla-articles-plugin/ |
| ok | /media/weTnwLzC8MAT47xS/plg_TwitterSummaryCardforArticles.zip/ | variante con diagonal | 1 | /recursos/twitter-summary-card-for-joomla-articles-plugin/ |
| ok | /media/weTnwLzC8MAT47xS/plg_websitepreloader.zip | descarga | 1 | /recursos/website-preloader-joomla-plugin/ |
| ok | /media/weTnwLzC8MAT47xS/plg_websitepreloader.zip/ | variante con diagonal | 1 | /recursos/website-preloader-joomla-plugin/ |
| ok | /programador-web-especialista-en-joomla-en-mexico | rastreo | 0 | /programador-web-especialista-en-joomla-en-mexico |
| ok | /programador-web-especialista-en-joomla-en-mexico/ | variante con diagonal | 0 | /programador-web-especialista-en-joomla-en-mexico/ |
| ok | /recursos | rastreo | 0 | /recursos |
| ok | /recursos/ | variante con diagonal | 0 | /recursos/ |
| ok | /recursos/11-imagenes-libres-de-derechos-gratis | rastreo | 1 | /recursos/imagenes-libres-de-derechos-gratis/ |
| ok | /recursos/11-imagenes-libres-de-derechos-gratis/ | variante con diagonal | 1 | /recursos/imagenes-libres-de-derechos-gratis/ |
| ok | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes | rastreo | 0 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes |
| ok | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ | variante con diagonal | 0 | /recursos/25-cosas-que-hacer-en-la-web-para-tener-mas-trafico-y-clientes/ |
| ok | /recursos/administration-brand-remover-joomla-plugin | rastreo | 0 | /recursos/administration-brand-remover-joomla-plugin |
| ok | /recursos/administration-brand-remover-joomla-plugin/ | variante con diagonal | 0 | /recursos/administration-brand-remover-joomla-plugin/ |
| ok | /recursos/imagenes-libres-de-derechos-gratis | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis/ | variante con diagonal | 0 | /recursos/imagenes-libres-de-derechos-gratis/ |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=0 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=160 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=240 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=320 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=400 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=480 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/imagenes-libres-de-derechos-gratis?start=80 | rastreo | 0 | /recursos/imagenes-libres-de-derechos-gratis |
| ok | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing | rastreo | 0 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing |
| ok | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ | variante con diagonal | 0 | /recursos/las-mejores-herramientas-de-seo-e-inbound-marketing/ |
| ok | /recursos/sumome-joomla-plugin | rastreo | 0 | /recursos/sumome-joomla-plugin |
| ok | /recursos/sumome-joomla-plugin/ | variante con diagonal | 0 | /recursos/sumome-joomla-plugin/ |
| ok | /recursos/twitter-summary-card-for-joomla-articles-plugin | rastreo | 0 | /recursos/twitter-summary-card-for-joomla-articles-plugin |
| ok | /recursos/twitter-summary-card-for-joomla-articles-plugin/ | variante con diagonal | 0 | /recursos/twitter-summary-card-for-joomla-articles-plugin/ |
| ok | /recursos/website-preloader-joomla-plugin | rastreo | 0 | /recursos/website-preloader-joomla-plugin |
| ok | /recursos/website-preloader-joomla-plugin/ | variante con diagonal | 0 | /recursos/website-preloader-joomla-plugin/ |
| ok | /temas | rastreo | 1 | /blog/ |
| ok | /temas/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/10-equipos-de-trabajo | rastreo | 1 | /blog/ |
| ok | /temas/10-equipos-de-trabajo/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/11-marketing-digital | rastreo | 1 | /blog/ |
| ok | /temas/11-marketing-digital/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/12-inbound-marketing | rastreo | 1 | /blog/ |
| ok | /temas/12-inbound-marketing/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/13-filosofia | rastreo | 1 | /blog/ |
| ok | /temas/13-filosofia/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/14-ideologia | rastreo | 1 | /blog/ |
| ok | /temas/14-ideologia/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/15-prosa | rastreo | 1 | /blog/ |
| ok | /temas/15-prosa/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/16-joomla | rastreo | 1 | /blog/ |
| ok | /temas/16-joomla/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/17-extensiones-de-joomla | rastreo | 1 | /blog/ |
| ok | /temas/17-extensiones-de-joomla/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/18-optimizacion-de-sitios-web | rastreo | 1 | /blog/ |
| ok | /temas/18-optimizacion-de-sitios-web/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/19-experiencia-de-usuario | rastreo | 1 | /blog/ |
| ok | /temas/19-experiencia-de-usuario/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/2-hubspot | rastreo | 1 | /blog/ |
| ok | /temas/2-hubspot/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/20-programacion-de-sitios-web | rastreo | 1 | /blog/ |
| ok | /temas/20-programacion-de-sitios-web/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/21-blogs | rastreo | 1 | /blog/ |
| ok | /temas/21-blogs/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/22-programador-joomla | rastreo | 1 | /blog/ |
| ok | /temas/22-programador-joomla/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/23-internet-de-las-cosas | rastreo | 1 | /blog/ |
| ok | /temas/23-internet-de-las-cosas/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/24-internet | rastreo | 1 | /blog/ |
| ok | /temas/24-internet/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/25-tecnologias-de-la-informacion | rastreo | 1 | /blog/ |
| ok | /temas/25-tecnologias-de-la-informacion/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/26-innovacion | rastreo | 1 | /blog/ |
| ok | /temas/26-innovacion/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/3-ventas | rastreo | 1 | /blog/ |
| ok | /temas/3-ventas/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/4-redes-sociales | rastreo | 1 | /blog/ |
| ok | /temas/4-redes-sociales/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/5-hashtags | rastreo | 1 | /blog/ |
| ok | /temas/5-hashtags/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/6-activismo | rastreo | 1 | /blog/ |
| ok | /temas/6-activismo/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/7-comunidad | rastreo | 1 | /blog/ |
| ok | /temas/7-comunidad/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/8-lealtad-de-marca | rastreo | 1 | /blog/ |
| ok | /temas/8-lealtad-de-marca/ | variante con diagonal | 1 | /blog/ |
| ok | /temas/9-seleccion-de-personal | rastreo | 1 | /blog/ |
| ok | /temas/9-seleccion-de-personal/ | variante con diagonal | 1 | /blog/ |
| ok | /usuario/inicio-de-sesion | rastreo | 1 | / |
| ok | /usuario/inicio-de-sesion/ | variante con diagonal | 1 | / |
| ok | /usuario/registro | rastreo | 1 | / |
| ok | /usuario/registro/ | variante con diagonal | 1 | / |
