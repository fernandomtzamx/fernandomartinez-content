---
title: "¿Plantillas para el administrador de Joomla? Sigue siendo mala idea"
slug: plantillas-administrador-joomla
type: post
status: publish
date: 2026-10-13 10:10
original: /blog/22-plantillas-administrador-joomla
excerpt: "Personalizar el administrador de Joomla con plantillas de terceros complica el mantenimiento. Desde Joomla 4 ya puedes poner tu logo y colores sin instalar nada. Así se hace."
categories: [desarrollo-web]
tags: [Joomla, administrador, plantillas, extensiones, mantenimiento]
featured_image: images/plantillas-administrador-joomla.png
featured_alt: "Portada: plantillas para el administrador de Joomla"
---

Una pregunta que me hacían seguido cuando programaba sitios en Joomla: "¿Le ponemos una plantilla personalizada al administrador?". Mi respuesta era no. Diez años y tres versiones mayores de Joomla después, sigue siendo no, aunque ahora por mejores razones.

<div class="fm-tldr" markdown="1">
**La versión corta:** las plantillas de administrador de terceros tienden a quedar abandonadas y a romperse con cada actualización. Desde Joomla 4, la plantilla de administración incluida permite cambiar logotipos y colores desde su configuración. Si lo que quieres es entregar un panel con la marca de tu cliente, ya no necesitas nada extra.
</div>

## Por qué era mala idea (y lo sigue siendo)

Muchos proveedores intentaron vender plantillas para el área de administración de Joomla. La mayoría terminó abandonando los proyectos, y no porque fueran malas, sino porque los usuarios regresaban a la plantilla predeterminada. La de Joomla la mantiene un equipo grande, dedicado a que sea clara y consistente.

Los problemas siguen siendo los mismos:

- **Se rompen con las actualizaciones.** Cada versión nueva de Joomla cambia algo del administrador. Una plantilla de terceros siempre va un paso atrás.
- **Confunden a otros administradores.** Si otro programador entra a tu sitio y no reconoce el panel, pierde tiempo y comete errores.
- **Agregan código que no necesitas** en la parte más sensible de tu sitio.

## Lo que la gente realmente quería

En mi experiencia, quien pedía una plantilla de administrador buscaba dos cosas: que el panel se viera más limpio y quitar los logotipos de Joomla para entregarle al cliente algo con su propia marca.

Por eso en su momento escribí [Administrator Brand Remover](/recursos/administration-brand-remover-joomla-plugin/), un plugin que hacía exactamente eso en Joomla 3, sin tocar la navegación ni la experiencia. Miles de sitios lo usaron.

## Cómo hacerlo hoy, sin plugins

Desde Joomla 4, la plantilla de administración incluida (Atum) trae opciones para personalizar la marca. En **Sistema > Estilos de plantillas de administrador** puedes cambiar:

- El logotipo de la pantalla de inicio de sesión.
- Los logotipos grande y pequeño del panel.
- Los colores principales de la interfaz.

Es la forma más segura: se actualiza con Joomla, no depende de nadie más y cualquier administrador lo reconoce.

## Si sigues en Joomla 3

Joomla 3 dejó de recibir soporte oficial en agosto de 2023. Si tu sitio sigue ahí, el logo del administrador es el menor de tus problemas: prioriza la migración a una versión con soporte. Mi plugin sigue disponible como archivo para sitios viejos, pero no es una razón para quedarte.

<div class="fm-cta" markdown="1">
¿Tienes un sitio Joomla y no sabes por dónde empezar? Lee [cómo elegir a un experto en Joomla en México](/blog/experto-en-joomla-en-mexico/).
</div>
