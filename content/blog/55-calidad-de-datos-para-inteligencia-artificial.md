---
title: "Calidad de datos para inteligencia artificial: qué necesitas antes de empezar"
slug: calidad-de-datos-para-inteligencia-artificial
type: post
status: publish
date: 2026-11-25 11:00
excerpt: "La calidad de datos decide si tu proyecto de IA llega a producción. Qué revisar antes de empezar, cómo medirla en una tarde y qué arreglar primero."
seo_title: "Calidad de datos para IA: qué revisar"
seo_description: "Calidad de datos para IA: por qué frena más proyectos que el modelo, cómo medirla en una tarde y qué revisar en tu CRM y documentos antes de empezar."
focus_keyword: "calidad de datos para ia"
categories: [crm-y-datos]
tags: [calidad de datos para ia, datos, CRM, inteligencia artificial, gobierno de datos, dirección de tecnología, CTO]
featured_image: images/calidad-de-datos-para-inteligencia-artificial.png
featured_alt: "Portada: calidad de datos para inteligencia artificial, qué necesitas antes de empezar"
---

Todos quieren hablar del modelo. Nadie quiere hablar del Excel con tres columnas de "Teléfono", dos de ellas vacías y una con la palabra "pendiente".

Aquí va lo incómodo: ese Excel decide más sobre tu proyecto de inteligencia artificial que cualquier modelo que elijas.

<div class="fm-tldr" markdown="1">
**La versión corta:**

- Gartner predice que, hasta 2026, las empresas abandonarán el [60% de los proyectos de IA que no tengan datos listos para IA](https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk) (2025).
- En ese mismo estudio, el 63% de las organizaciones no tiene o no sabe si tiene las prácticas de datos correctas para IA.
- "Datos de calidad" no significa datos perfectos: significa datos suficientes, actuales y confiables **para un caso de uso concreto**.
- Lo que haría yo: medir la calidad en una tarde con 100 registros, arreglar solo lo que toca al primer caso y nombrar un dueño de cada fuente.
</div>

[TOC]

## Por qué la calidad de datos frena más proyectos de IA que el modelo

La calidad de datos frena más proyectos de IA que el modelo porque los modelos ya son buenos y baratos, y los datos de la mayoría de las empresas no lo son. Un modelo excelente que lee información vieja, duplicada o contradictoria responde con mucha seguridad cosas equivocadas.

Gartner encuestó a 1,203 líderes de gestión de datos en julio de 2024. Su conclusión, publicada en [febrero de 2025](https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk), es directa: hasta 2026, las organizaciones abandonarán el 60% de los proyectos de IA que no estén respaldados por datos listos para IA. Y el 63% de las organizaciones no tiene, o no sabe si tiene, las prácticas de datos necesarias.

La frase del reporte que más me gusta es casi obvia: "if the data has issues, then the data is not ready for AI". Obvia, sí. Pero en las juntas de arranque casi nadie la dice en voz alta.

Ya lo conté en [por qué los pilotos de IA no llegan a producción](/blog/por-que-los-pilotos-de-ia-no-llegan-a-produccion/): una de las formas más comunes en que muere un piloto es que los datos que importan viven en la cabeza de tres personas.

## Qué tan mal están los datos (spoiler: peor de lo que crees)

Los datos de una empresa típica están peor de lo que su dirección cree, y casi nadie lo ha medido.

El estudio más citado sobre esto sigue siendo de Tadhg Nagle, Thomas C. Redman y David Sammon, publicado en [Harvard Business Review en 2017](https://hbr.org/2017/09/only-3-of-companies-data-meets-basic-quality-standards). Pidieron a 75 ejecutivos tomar 100 registros recientes de su propia área y marcar los errores evidentes. En promedio, el 47% de los registros recién creados tenía al menos un error crítico. Y solo el 3% de las calificaciones resultó aceptable, aun con el criterio más laxo.

Es un estudio de hace años. No tengo razones para pensar que el CRM promedio mejoró solo. Lo que sí cambió es que ahora le vamos a pedir a una IA que lea esos registros y tome decisiones con ellos.

En los proyectos en los que he estado, los errores son siempre los mismos:

- **Duplicados.** El mismo cliente con tres nombres distintos ("Grupo ABC", "ABC SA de CV", "abc").
- **Campos vacíos que alguien rellenó para poder guardar.** El famoso correo "na@na.com".
- **Información vieja que nadie marcó como vieja.** Listas de precios de 2023 en la misma carpeta que las de este año.
- **Reglas que no están escritas.** Qué cliente tiene crédito, qué se le puede prometer, cuándo se escala.

Nada de esto es nuevo. La IA solo lo vuelve visible más rápido.

## Qué significa tener datos listos para IA

Tener datos listos para IA significa que los datos que necesita **un caso de uso específico** están completos, actualizados, sin contradicciones y en un sistema al que la IA puede llegar con permiso. No significa limpiar toda la empresa antes de empezar.

La primera de las cinco recomendaciones de Gartner va en esa línea: alinear los datos con los casos de uso de IA. Es decir, la calidad se mide contra lo que vas a hacer, no en abstracto.

Esto cambia la conversación. Un bot que responde preguntas de políticas internas necesita documentos vigentes y con fecha. Un modelo que prioriza prospectos necesita historial de ventas confiable en el CRM. Son dos proyectos de datos distintos, y ninguno exige que primero arregles el ERP completo.

Las cinco dimensiones que reviso para cada caso:

1. **Completitud.** ¿Los campos que el caso necesita tienen valor en la mayoría de los registros?
2. **Exactitud.** ¿Lo que dice el dato es cierto? (Se comprueba con muestras, no con fe.)
3. **Actualidad.** ¿Hay forma de saber qué está vigente y qué no?
4. **Consistencia.** ¿El mismo dato dice lo mismo en el CRM, en el ERP y en el Excel de ventas?
5. **Acceso y permisos.** ¿La IA puede leerlo sin que alguien exporte un CSV cada semana? ¿Y debería poder leerlo?

## Datos estructurados y documentos: dos problemas distintos

La calidad de datos para IA tiene dos frentes: los datos estructurados (CRM, ERP, tablas) y los documentos (manuales, políticas, contratos, correos). Se arreglan de forma diferente.

**En los datos estructurados** el trabajo es el de siempre: quitar duplicados, normalizar formatos, validar en la captura y decidir cuál sistema manda cuando dos dicen cosas distintas. Si quieres un punto de partida, escribí hace tiempo sobre [cómo enriquecer tu base de datos de clientes](/blog/como-enriquecer-tu-base-de-datos-de-clientes/); antes de enriquecer, hay que limpiar.

**En los documentos** el problema es otro: versiones. La IA generativa no sabe que el manual de 2021 fue reemplazado si los dos están en la misma carpeta. Aquí el trabajo es poner fecha y dueño a cada documento, archivar lo viejo fuera del alcance de la IA y escribir las reglas que hoy solo existen en conversaciones de WhatsApp.

Lo segundo suele ser más barato que lo primero. Y casi siempre da resultados más rápido.

## Datos personales: el filtro que no puedes saltarte en México

Antes de mandar datos de clientes a cualquier herramienta de IA, revisa qué datos personales incluyen y con qué base los usas. En México rige una [nueva Ley Federal de Protección de Datos Personales en Posesión de los Particulares](https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf), publicada en el Diario Oficial el 20 de marzo de 2025.

No soy abogado y esto no es asesoría legal. Pero como CTO mi regla práctica es simple: si el caso de uso no necesita el nombre, el teléfono o el RFC del cliente, esos campos no entran. Menos datos personales significa menos riesgo y, de paso, menos ruido para el modelo. Gartner también incluye el gobierno de datos entre sus cinco recomendaciones, justo para no violar requisitos legales.

## Lo que haría yo

Si mañana una empresa me dijera "queremos empezar con IA", esto es lo que haría con los datos antes de tocar cualquier modelo:

1. **Elegir primero el caso de uso.** Sin caso, no hay forma de saber qué datos importan. Expliqué cómo en [casos de uso de inteligencia artificial en empresas](/blog/casos-de-uso-de-inteligencia-artificial-en-empresas/).
2. **Medir en una tarde.** Tomar los últimos 100 registros que usaría el caso y marcar en rojo cada error evidente, como en el ejercicio de HBR. El porcentaje de registros limpios es tu línea base. Duele, pero es gratis.
3. **Hacer la lista de fuentes.** Qué sistema, qué carpeta, qué Excel. Y para cada uno, un dueño con nombre y apellido que responda por él.
4. **Arreglar solo lo que toca al caso.** No lances un proyecto de "limpieza total de datos" de seis meses. Corrige los campos y documentos que el primer caso necesita.
5. **Cerrar la llave en la captura.** Validaciones en los formularios y en el CRM para que el error no vuelva a entrar. Limpiar sin cerrar la llave es trapear con la llave abierta.
6. **Quitar lo que no hace falta.** Datos personales innecesarios, documentos vencidos y duplicados fuera del alcance de la IA.
7. **Volver a medir a los 30 días.** Los mismos 100 registros, el mismo ejercicio. Si el número no mejoró, el problema es de proceso, no de tecnología.

Todo esto cabe en la [estrategia de inteligencia artificial para empresas](/blog/estrategia-de-inteligencia-artificial-para-empresas/) que propuse la semana pasada: de las cuatro preguntas, "con qué datos" es la que más proyectos tumba. Y si tus datos viven repartidos entre el CRM, la plataforma de correo y las campañas, vale la pena revisar cómo se conecta tu [stack de martech](/blog/que-es-martech/) antes de ponerle IA encima.

## Cierre

La calidad de datos no es el tema más emocionante de la inteligencia artificial. Es el que decide si tu proyecto llega a producción o se queda en demo.

Mi pregunta para esta semana: ¿cuántos de tus últimos 100 registros de clientes aguantarían que una IA los leyera en voz alta frente a tu director general?

Si hiciste el ejercicio y el número te asustó, o quieres hacerlo con alguien que ya lo vivió varias veces, [platiquemos](/contacto/).
