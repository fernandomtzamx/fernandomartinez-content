---
title: "Comprar o desarrollar inteligencia artificial: cómo decidir"
slug: comprar-o-desarrollar-inteligencia-artificial
type: post
status: publish
date: 2026-11-27 11:00
excerpt: "Comprar o desarrollar IA no es una pregunta de ego técnico. Cómo decido como CTO qué se compra, qué se construye y qué se arma combinando las dos cosas."
seo_title: "Comprar o desarrollar IA: cómo decidir"
seo_description: "Comprar o desarrollar IA: qué dicen los datos, tres preguntas para decidir, cuándo sí conviene construir y los costos que casi nadie pone en la cuenta."
focus_keyword: "comprar o desarrollar ia"
categories: [ia-y-tecnologia]
tags: [comprar o desarrollar ia, inteligencia artificial, build vs buy, proveedores de IA, estrategia, dirección de tecnología, CTO]
featured_image: images/comprar-o-desarrollar-inteligencia-artificial.png
featured_alt: "Portada: comprar o desarrollar inteligencia artificial, cómo decidir"
---

Todo equipo técnico que conozco tiene la misma reacción cuando alguien propone comprar una herramienta de IA: "eso lo hacemos nosotros en dos semanas". Yo también la tengo. Llevo programando desde 2008 y el impulso no se quita.

Aquí va lo incómodo: casi siempre son más de dos semanas, y casi nunca es lo que más le conviene a la empresa.

<div class="fm-tldr" markdown="1">
**La versión corta:**

- Las empresas ya eligieron: en 2025, el [76% de las soluciones de IA empresariales se compró en lugar de construirse](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/), contra 53% en 2024 (Menlo Ventures).
- Comprar no es rendirse. Construir no es más serio. La pregunta útil es si ese proceso es lo que te diferencia de tu competencia.
- La opción que más uso es la de en medio: comprar el modelo y la plataforma, y construir la capa que conecta con tus datos y tus reglas.
- Lo que haría yo: separar lo genérico de lo diferenciador, hacer la cuenta a tres años (no al mes uno) y dejar escrita la salida antes de firmar.
</div>

[TOC]

## Qué dicen los datos sobre comprar o desarrollar IA

Los datos dicen que la mayoría de las empresas ya compra, y que lo comprado llega a producción con más frecuencia que lo que se queda en piloto.

Menlo Ventures encuestó a 495 tomadores de decisión de IA en empresas de Estados Unidos en noviembre de 2025. En su reporte [*The State of Generative AI in the Enterprise*](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/), el 76% de los casos de uso de IA se compró en lugar de construirse en casa. Un año antes la proporción estaba casi pareja: 47% construido y 53% comprado.

El mismo reporte encontró que el 47% de los acuerdos de compra de IA llega a producción, contra 25% en el software tradicional como servicio. Es decir, cuando una empresa compra IA, la termina usando casi el doble de veces que cuando compra otro tipo de software.

Ojo con el contexto: es una encuesta a empresas estadounidenses hecha por un fondo que invierte en compañías de IA. No es la realidad de una distribuidora en Guadalajara. Pero la tendencia coincide con lo que he visto en los proyectos en los que he estado, y con el estudio del MIT que comenté en [por qué los pilotos de IA no llegan a producción](/blog/por-que-los-pilotos-de-ia-no-llegan-a-produccion/): las herramientas de proveedores especializados tuvieron éxito bastante más seguido que las construidas desde cero.

## Comprar, construir o combinar: las tres opciones reales

La decisión no es binaria. Gartner la plantea en su guía [*Build, Buy or Blend?*](https://www.gartner.com/en/articles/deploying-ai) con tres fuentes de IA en una empresa:

1. **IA incluida en el software que ya pagas.** El CRM que resume llamadas, el correo que redacta respuestas, el ERP que detecta facturas raras. Gartner la describe como el área de capacidades de IA más grande y de mayor crecimiento.
2. **IA que trae cada persona.** Las herramientas independientes que el equipo usa por su cuenta. A veces con permiso, a veces sin él.
3. **IA construida o "mezclada".** Lo que tu equipo construye y lo que arma conectando los modelos de un proveedor por API con tus propios datos y procesos.

Para mí, en la práctica esto se traduce en tres caminos:

- **Comprar:** una herramienta terminada que resuelve el problema tal cual.
- **Combinar:** pagar el modelo (OpenAI, Anthropic, Google o uno abierto) y construir encima la parte que es tuya: la conexión con el CRM, las reglas de negocio, los permisos.
- **Construir:** entrenar o ajustar modelos propios y mantener toda la infraestructura.

El tercer camino casi nunca tiene sentido para una empresa mediana en México. No porque el equipo no pueda, sino porque el dinero rinde más en otro lado. El reporte de Menlo de 2026 lo resume en una frase: ["More Money Goes into Using AI Than Building It"](https://menlovc.com/perspective/2026-the-state-of-enterprise-ai/).

## Tres preguntas para decidir

Antes de cotizar nada, hago tres preguntas. Las respuestas casi siempre deciden solas.

### 1. ¿Este proceso es lo que te hace diferente?

Si el proceso es igual en tu empresa que en la de enfrente, se compra. Transcribir llamadas, extraer datos de facturas, contestar las preguntas frecuentes de primer nivel, resumir juntas. Nadie te va a elegir como proveedor porque tus actas de junta salen más bonitas.

Si el proceso es tu ventaja (cómo calculas el riesgo de crédito de tus distribuidores, cómo asignas rutas, cómo cotizas proyectos especiales), ahí sí vale la pena construir la capa que lo contiene. Lo que no quieres es que tu ventaja viva dentro de la herramienta de un proveedor que también le vende a tu competencia.

### 2. ¿Tus datos y tus reglas caben en la herramienta?

Muchas compras fallan aquí. La herramienta funciona perfecto en la demo con datos genéricos, y luego resulta que tus reglas de descuento, tus excepciones de crédito o tu forma de clasificar clientes no caben en su configuración.

Pide una prueba con tus datos reales, no con los suyos. Si el proveedor no la acepta, ya tienes tu respuesta. Y si tus datos no están listos para esa prueba, el problema va antes de la decisión de compra; lo expliqué en [calidad de datos para inteligencia artificial](/blog/calidad-de-datos-para-inteligencia-artificial/).

### 3. ¿Quién lo va a mantener dentro de un año?

Construir es la parte fácil. Mantener es la parte cara. Los modelos cambian cada pocos meses, las API se actualizan, los costos por uso se mueven y la persona que lo programó puede irse.

Si no tienes un equipo que pueda cuidar el sistema después de lanzarlo, construir es comprar un problema a plazos.

## Cuándo sí conviene desarrollar

Hay casos en los que yo sí construiría, o al menos combinaría:

- **Cuando el proceso es tu ventaja competitiva** y ningún producto lo resuelve sin desfigurarlo.
- **Cuando la integración es el producto.** Si el valor está en conectar tu ERP, tu CRM y tu WhatsApp de ventas con reglas muy tuyas, una herramienta genérica se queda corta.
- **Cuando el volumen hace que la licencia por usuario no tenga sentido.** A partir de cierto tamaño, pagar el modelo por uso y construir la interfaz sale más barato que una licencia por asiento.
- **Cuando hay restricciones de datos** que ningún proveedor cumple: datos sensibles, requisitos de residencia o contratos con clientes que lo prohíben.

Fuera de esos casos, mi recomendación por defecto es comprar o combinar. Y lo digo como alguien que disfruta construir.

## Los costos que casi nadie pone en la cuenta

Cuando un equipo compara comprar contra desarrollar, casi siempre compara la licencia contra el tiempo de desarrollo del primer mes. Es la cuenta equivocada.

Del lado de **desarrollar** faltan casi siempre:

- El mantenimiento cuando el proveedor del modelo cambia o retira una versión.
- Las pruebas y evaluaciones cada vez que algo cambia.
- La seguridad: permisos, registro de quién preguntó qué, protección contra mal uso.
- El costo de oportunidad: lo que tu equipo dejó de hacer mientras construía esto.

Del lado de **comprar** faltan casi siempre:

- La integración con tus sistemas, que rara vez viene incluida.
- El aumento de precio en la renovación, cuando ya dependes de la herramienta.
- El costo de salir: exportar datos, configuraciones e historial si un día cambias.
- La gestión del proveedor: contratos, revisiones de seguridad y soporte.

Hagamos cuentas siempre a tres años, con las dos columnas completas. La opción "barata" cambia de lado más veces de las que uno espera.

## Lo que haría yo

Si mañana una empresa me preguntara si debe comprar o desarrollar su próximo proyecto de IA, esto haría:

1. **Partir del caso de uso, no de la tecnología.** Sin un caso concreto, la pregunta no tiene respuesta. Si aún no lo tienes, empieza por [cómo elegir el primer caso de uso](/blog/casos-de-uso-de-inteligencia-artificial-en-empresas/).
2. **Revisar lo que ya pagas.** Antes de comprar algo nuevo, revisar qué IA trae ya incluida tu CRM, tu suite de oficina o tu plataforma de marketing. Muchas veces ya está pagada y nadie la activó. Si tu [stack de martech](/blog/que-es-martech/) es grande, ahí suele haber sorpresas.
3. **Clasificar cada proceso** en genérico o diferenciador. Lo genérico se compra. Lo diferenciador se combina.
4. **Probar con datos reales** a dos proveedores durante 30 días, con una métrica de negocio acordada antes de empezar.
5. **Hacer la cuenta a tres años** con las dos columnas de costos de arriba, incluido el tiempo de tu equipo.
6. **Escribir la salida antes de entrar.** Cómo exportas tus datos, qué pasa si el proveedor sube precio o desaparece, y qué parte podrías mover a otro modelo sin reescribir todo.
7. **Revisar la decisión cada año.** Lo que hoy compras puede convenir construirlo cuando crezcas, y al revés.

Todo esto encaja en la [estrategia de inteligencia artificial para empresas](/blog/estrategia-de-inteligencia-artificial-para-empresas/) que propuse hace unos días: decidir cómo se consigue cada capacidad es parte de la estrategia, no un trámite de compras.

## Cierre

Comprar o desarrollar inteligencia artificial no es una pregunta de orgullo técnico. Es una pregunta de dónde quieres que tu equipo gaste su tiempo.

Mi pregunta para esta semana: de los proyectos de IA que tienes en la lista, ¿cuántos son de verdad lo que te diferencia de tu competencia?

Si estás frente a esa decisión y quieres una segunda opinión de alguien que ha estado de los dos lados de la mesa, [platiquemos](/contacto/).
