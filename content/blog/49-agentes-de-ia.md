---
title: "Agentes de IA: qué son de verdad y dónde sí los pondría en una empresa hoy"
slug: agentes-de-ia-que-son-y-donde-usarlos
type: post
status: draft
date: 2026-10-22 11:00
excerpt: "Un agente de IA no es un chatbot con nombre nuevo. Qué lo distingue, por qué Gartner prevé que el 40% de los proyectos se cancele y los cuatro lugares donde sí lo pondría hoy."
seo_title: "Agentes de IA: qué son y dónde usarlos"
seo_description: "Un agente de IA no es un chatbot con nombre nuevo. Qué lo distingue de un asistente, por qué tantos proyectos se cancelan y dónde sí pondría uno hoy."
focus_keyword: "agentes de ia"
categories: [ia-y-tecnologia]
tags: [agentes de IA, IA, automatización, agent washing, dirección de tecnología, CTO, procesos]
featured_image: images/agentes-de-ia-que-son-y-donde-usarlos.png
featured_alt: "Portada: agentes de IA, qué son y dónde usarlos"
---

Hace un mes me mostraron un "agente de ventas con IA". Le pregunté qué hacía cuando el cliente pedía factura. Respondía con un texto muy amable y le pasaba el caso a una persona. O sea: un chatbot. Un buen chatbot, pero un chatbot con nombre de 2026.

Esta entrada es para que la próxima vez que te vendan un agente sepas qué preguntar, y para contarte dónde sí he visto que valen la pena.

<div class="fm-tldr" markdown="1">
**La versión corta:**

- Un agente de IA **decide y ejecuta**: recibe un objetivo, elige pasos, usa herramientas (correo, CRM, API, navegador) y entrega un resultado. Un asistente solo responde.
- Gartner calcula que [más del 40% de los proyectos de agentes se cancelará antes de que termine 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) y que, de los miles de proveedores que se anuncian como "agénticos", solo unos 130 lo son de verdad.
- Dónde sí los pondría hoy: tareas repetitivas con reglas claras, datos accesibles por API, bajo costo si se equivoca y un humano que revisa al final.
- Dónde no: decisiones de dinero sin supervisión, procesos que ni tu equipo tiene documentados y cualquier cosa que toque datos personales sin pasar por legal.
</div>

[TOC]

## Qué es un agente (sin diapositivas)

Un modelo de lenguaje, solo, es una función: le das texto, te devuelve texto. Un asistente es ese modelo con una interfaz de chat y, a veces, acceso a tus documentos. Un agente es el modelo con tres cosas más:

1. **Un objetivo**, no una pregunta. "Consigue tres cotizaciones de este proveedor y ponlas en la hoja de cálculo", no "¿qué es una cotización?".
2. **Herramientas** que puede usar por su cuenta: leer y mandar correos, consultar el CRM, llamar a una API, abrir un navegador, ejecutar código.
3. **Un ciclo**: planea, actúa, observa el resultado, corrige y repite hasta terminar o rendirse.

La diferencia práctica es que un asistente te ahorra escribir; un agente te ahorra hacer. Y eso cambia por completo el riesgo: cuando un asistente se equivoca, te da un texto malo; cuando un agente se equivoca, manda un correo malo a un cliente o borra una fila que sí importaba.

## Agent washing: cómo detectarlo en cinco minutos

Gartner le puso nombre en 2025: *agent washing*, [renombrar asistentes, chatbots y herramientas de RPA como "agentes" sin que tengan la capacidad de actuar por su cuenta](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027). Su cálculo: de los miles de proveedores que se venden como agénticos, unos 130 lo son.

Las preguntas que hago en una demo:

- **¿Qué puede hacer sin que un humano apriete un botón?** Si la respuesta es "sugerir", es un asistente.
- **¿A qué sistemas se conecta hoy, en mi empresa, y con qué permisos?** Si la respuesta empieza con "se puede integrar con", todavía no se conecta con nada.
- **Enséñame un caso en el que se equivocó.** Un proveedor que nunca ha visto fallar a su agente no lo ha puesto en producción.
- **¿Qué pasa cuando no sabe qué hacer?** Lo que quiero oír: se detiene y avisa. Lo que no quiero oír: "siempre encuentra una forma".
- **¿Cuánto cuesta por tarea completada?** No por mes, no por usuario: por tarea. Es la única cifra que puedo comparar contra lo que cuesta hacerlo a mano.

## Dónde sí lo pondría hoy

Después de ver bastantes fallar, mi regla para un agente en 2026 tiene cuatro condiciones. Si se cumplen las cuatro, adelante. Si falla una, es un piloto. Si fallan dos, es una demo.

1. **La tarea es repetitiva y tiene reglas que alguien puede escribir en una página.** Conciliar pagos contra facturas. Dar de alta un lead con los datos del formulario. Preparar el resumen semanal de tickets.
2. **Los datos están disponibles por API**, no en capturas de pantalla ni en el Excel de alguien. Si el agente tiene que "navegar" un sistema viejo, va a romperse en la siguiente actualización de ese sistema.
3. **Equivocarse sale barato y se puede deshacer.** Un borrador de correo mal hecho se corrige. Un pago mal hecho no.
4. **Hay un humano que revisa el resultado** antes de que salga de la empresa, al menos los primeros meses.

Con esas condiciones, los cuatro usos que sí he visto rendir:

**Operaciones internas.** Clasificar y enrutar correos, abrir tickets con los datos ya extraídos, preparar reportes que antes armaba una persona cada lunes. Es la parte aburrida del reporte del MIT que mencioné en la [entrada anterior](/blog/por-que-los-pilotos-de-ia-no-llegan-a-produccion/): el dinero rinde donde nadie lo ve.

**Investigación y preparación comercial.** Antes de una llamada, el agente arma la ficha del prospecto con lo que hay en el CRM, en su sitio y en noticias. El vendedor llega preparado y no gastó cuarenta minutos en Google. El agente no vende; prepara.

**Desarrollo de software**, con supervisión. Agentes que escriben pruebas, hacen refactors acotados, revisan un *pull request* o migran código entre versiones. De esto hablo en la [siguiente entrada](/blog/programar-con-ia-en-una-empresa-real/), porque tiene sus propias trampas.

**Atención a clientes de primer nivel**, solo cuando hay un buen proceso de entrega a humano. Es el uso más vendido y el que más veces vi explotar, así que lo pongo al final a propósito.

## Dónde no, por ahora

- **Decisiones de dinero sin supervisión**: descuentos, pagos, compras, cambios de precio. No porque el modelo sea tonto, sino porque nadie en la empresa quiere firmar la responsabilidad de un error, y si nadie firma, no se puede operar.
- **Procesos que tu propio equipo no tiene documentados.** Si no puedes explicárselo a un empleado nuevo en una página, no puedes explicárselo a un agente.
- **Cualquier cosa con datos personales** que no haya pasado por legal. Un agente que lee correos de clientes está tratando datos personales, por más que el proveedor diga que "no entrena con tus datos".
- **Tareas donde el costo de un error silencioso es alto**: un agente que se equivoca y avisa es manejable; uno que se equivoca con confianza y sigue adelante es el que te cuesta un cliente.

## Lo que haría si fuera tu primer agente

Empezaría por lo interno. Un agente que prepara el reporte de los lunes, con un humano que lo revisa antes de mandarlo. Se mide en horas ahorradas, que ya sabes cuánto cuestan. Si en dos meses el humano deja de corregirlo, se amplía; si no, se apaga y aprendiste barato.

Ya vendrán los agentes que hablan con clientes. Primero que aprendan a hablar con tu base de datos.

¿Ya tienes uno funcionando o uno que no arrancó? [Platiquemos](/contacto/), me interesa saber qué condición de las cuatro fue la que falló.
