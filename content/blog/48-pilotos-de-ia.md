---
title: "Por qué el 95% de los pilotos de IA no llegan a nada (y qué haría yo distinto)"
slug: por-que-los-pilotos-de-ia-no-llegan-a-produccion
type: post
status: publish
date: 2026-10-21 11:00
excerpt: "Casi todos los pilotos de IA en empresas se quedan en demo. No es culpa del modelo: es del problema que eligieron, de los datos y de quién lo dirige. Lo que haría yo como CTO."
seo_title: "Por qué los pilotos de IA mueren en demo"
seo_description: "Casi todos los pilotos de IA en empresas se quedan en demo. No es el modelo: es el problema elegido, los datos y quién lo dirige. Qué haría distinto un CTO."
focus_keyword: "pilotos de ia"
categories: [ia-y-tecnologia]
tags: [IA, inteligencia artificial, pilotos, estrategia, dirección de tecnología, CTO, datos, ROI]
featured_image: images/por-que-los-pilotos-de-ia-no-llegan-a-produccion.png
featured_alt: "Portada: por qué los pilotos de IA no llegan a producción"
---

En los últimos dos años me han presentado más pilotos de inteligencia artificial que proyectos terminados. La proporción es brutal: por cada cosa que vi funcionando con usuarios reales, vi diez demos preciosas que murieron en una carpeta compartida.

No es una impresión mía. Y no es que los modelos sean malos. Aquí va lo incómodo: la mayoría de los pilotos de IA están diseñados para impresionar, no para sobrevivir.

<div class="fm-tldr" markdown="1">
**La versión corta:**

- Un estudio del MIT de 2025 encontró que [cerca del 95% de los pilotos de IA generativa en empresas no mueven el estado de resultados](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo). Solo el 5% llega a impactar ingresos.
- La causa principal no es el modelo. Es que las herramientas no aprenden del proceso real y que el piloto nunca tuvo un dueño con poder de decisión.
- Comprar a un proveedor especializado funcionó en ese estudio alrededor del doble de veces que construir desde cero.
- Lo que haría yo: elegir un problema aburrido y medible, meter la IA dentro de un proceso que ya existe, ponerle un dueño de negocio y una métrica de dinero, y decidir en 60 días si se queda o se apaga.
</div>

[TOC]

## Los datos que nadie quiere ver en la presentación

El reporte *The GenAI Divide: State of AI in Business 2025* del MIT NANDA revisó cientos de implementaciones y entrevistó a directivos de empresas grandes. La conclusión que se volvió titular: [el 95% de los pilotos no tiene impacto medible en resultados](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo). El otro 5% acelera ingresos de forma clara.

Dos detalles del mismo reporte me parecen más útiles que el titular:

1. **Las herramientas compradas a proveedores especializados tuvieron éxito más o menos el 67% de las veces; las construidas en casa, cerca de un tercio de eso.** Esto le duele al ego de cualquier equipo técnico (al mío incluido), pero tiene lógica: el proveedor ya se tropezó con los problemas que tú vas a descubrir en el mes tres.
2. **Más de la mitad del presupuesto de IA se fue a ventas y marketing, y el mayor retorno estuvo en la trastienda:** operaciones, menos gasto en agencias y en subcontratación. Es decir, el dinero se gasta donde se ve y rinde donde no se ve.

Gartner, por su lado, predijo en junio de 2025 que [más del 40% de los proyectos de agentes de IA se cancelará antes de que termine 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027), por costos que se disparan, valor de negocio poco claro y controles de riesgo insuficientes. Tres razones que no tienen nada que ver con la calidad del modelo.

Spoiler: el problema casi nunca es la IA.

## Las cuatro formas en que vi morir un piloto

No voy a dar nombres. Pero los patrones se repiten tanto que ya los reconozco en la primera reunión.

### 1. Nació como demo, no como proceso

Alguien del consejo vio un video, alguien de marketing pidió "algo con IA" y el equipo armó un chatbot en dos semanas. Quedó espectacular en la presentación. Nunca se conectó al CRM, al inventario ni al sistema de tickets. Un piloto que no toca el proceso real no puede fallar, pero tampoco puede ganar.

### 2. Nadie era el dueño

El proyecto era "de tecnología" para la gente de negocio y "de negocio" para la gente de tecnología. Cuando hubo que decidir si el bot podía ofrecer un descuento o no, nadie tenía la autoridad. El piloto se quedó esperando una junta que nunca se agendó.

### 3. Los datos estaban en la cabeza de tres personas

El modelo respondía bien sobre lo que estaba en los PDF. Pero las reglas que de verdad importaban (a quién se le da crédito, qué se puede prometer de entrega, cuándo se escala a un humano) vivían en el WhatsApp de la gerente de operaciones. El reporte del MIT le llama a esto *learning gap*: la herramienta no aprende de cómo trabaja la empresa, y la empresa no la alimenta.

### 4. Se midió con aplausos

"El bot tuvo miles de conversaciones". ¿Y? ¿Cuántas terminaron en venta, en ticket cerrado, en horas ahorradas? Si la métrica del piloto no se puede convertir a pesos, el piloto se va a cancelar en el primer recorte de presupuesto, aunque haya sido bueno.

## Lo que haría yo (y lo que hago)

Vengo del marketing, dirijo tecnología y mido las cosas en ventas y en procesos que funcionan. Con esa deformación profesional, así arranco un piloto hoy:

**Elijo un problema aburrido.** Clasificar correos, extraer datos de facturas, resumir llamadas de ventas, responder las veinte preguntas que representan el 80% de los tickets. Nada que salga en un video de lanzamiento. Todo lo que ahorre horas que ya sé cuánto cuestan.

**Lo meto dentro de un proceso que ya existe.** Si el equipo de ventas vive en el CRM, la IA aparece en el CRM. Si operaciones vive en el correo, aparece en el correo. Una herramienta más a la que hay que entrar es una herramienta que nadie va a usar en marzo.

**Le pongo un dueño de negocio y un dueño técnico.** El de negocio decide qué puede hacer la IA y qué no. El técnico decide cómo. Los dos firman la métrica antes de escribir una línea de código.

**Una métrica, en dinero, con fecha.** "Reducir el tiempo de respuesta a cotizaciones de 48 a 4 horas, medido en 60 días". Si en 60 días no se movió, se apaga sin drama. Un piloto que no puede morir no es un piloto, es un gasto fijo disfrazado.

**Compro antes de construir, salvo que el proceso sea mi ventaja.** Para lo genérico (transcripción, extracción de documentos, atención de primer nivel) uso un proveedor. Construyo solo cuando el proceso es lo que me diferencia de la competencia y el proveedor no lo entiende.

**Dejo los datos listos antes del modelo.** En todos los pilotos serios en los que he estado, la mayor parte del tiempo se fue en ordenar lo que el modelo necesita leer, no en el modelo. Si esa parte no está presupuestada, el piloto ya nació con fecha de caducidad.

## Cómo saber si tu piloto está en el 95%

Tres preguntas rápidas. Si contestas que no a cualquiera, estás en el grupo grande:

1. ¿Puedes decir, en una frase, cuánto dinero ahorra o genera por mes?
2. ¿Hay una persona que pueda apagarlo o escalarlo sin pedir permiso a un comité?
3. ¿Está conectado al sistema donde ya vive el trabajo (CRM, ERP, tickets, correo)?

No es una lista sofisticada. Por eso casi nadie la pasa.

## Lo que viene en este blog

Con esta entrada arranco un calendario de tres publicaciones por semana, hasta junio de 2027, sobre tecnología e inteligencia artificial vistas desde el escritorio de un director de tecnología que todavía programa. Lunes visión, miércoles práctica, viernes contrapeso. Sin siglas nuevas ni promesas de transformación.

Esta semana sigue con qué son de verdad los agentes de IA y dónde sí los pondría en una empresa, y cierra con lo que dejo que la IA escriba en mi código y lo que no.

Si tienes un piloto atorado, o uno que sí funcionó y quieres presumirlo, [platiquemos](/contacto/). Me interesan más los segundos, pero aprendo más de los primeros. Y si quieres el contexto del resto de lo que escribo, está en el [blog de un director de tecnología](/blog/).
