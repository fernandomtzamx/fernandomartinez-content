---
title: "Programar con IA en una empresa real: qué dejo que escriba y qué no"
slug: programar-con-ia-en-una-empresa-real
type: post
status: publish
date: 2026-10-23 11:00
excerpt: "Programo desde 2008 y hoy la IA escribe buena parte de mi código. Lo que le dejo, lo que no, lo que dicen los estudios y las tres reglas que aplico con mi equipo."
seo_title: "Programar con IA: qué le dejo y qué no"
seo_description: "Programo desde 2008 y hoy la IA escribe parte de mi código. Qué le dejo, qué no, qué dicen los estudios de productividad y las reglas de mi equipo."
focus_keyword: "programar con ia"
categories: [desarrollo-web]
tags: [programar con IA, desarrollo de software, productividad, agentes de código, revisión de código, CTO]
featured_image: images/programar-con-ia-en-una-empresa-real.png
featured_alt: "Portada: programar con IA en una empresa real"
---

Confesión: este blog se publica con un flujo que escribí casi por completo con un asistente de IA. Markdown, un script en Python, la API de WordPress y GitHub Actions. Funcionó a la primera en menos cosas de las que me gustaría admitir, pero funcionó.

También he tirado a la basura semanas de código generado que parecía correcto y no lo era. Aquí va lo que aprendí sobre dónde sí y dónde no, con la ventaja de que todavía programo y no solo lo platico en juntas.

<div class="fm-tldr" markdown="1">
**La versión corta:**

- Los estudios no se ponen de acuerdo. METR midió en 2025 que [desarrolladores expertos tardaban 19% más con IA](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) mientras creían ir 20% más rápido; en febrero de 2026 [el mismo equipo dijo que ese dato ya quedó viejo](https://metr.org/blog/2026-02-24-uplift-update/) y que ahora parece haber aceleración, pero sus propios datos nuevos son poco confiables.
- La encuesta de Stack Overflow de 2025 lo resume: [84% usa o planea usar IA, pero 46% desconfía de la exactitud](https://infoworld.com/article/4031673/ai-use-among-software-developers-grows-but-trust-remains-an-issue-stack-overflow-survey.html), y la queja principal son las soluciones "casi correctas".
- Lo que le dejo: pruebas, código repetitivo, migraciones, scripts de un solo uso, documentación, el primer borrador de casi todo.
- Lo que no: decisiones de arquitectura, lógica de negocio que no entiendo al 100%, seguridad y cualquier cosa que no voy a poder revisar.
</div>

[TOC]

## Lo que dicen los estudios (y por qué no me fío de ninguno solo)

El estudio más citado de 2025 es el de METR: [16 desarrolladores con experiencia, 246 tareas reales en sus propios proyectos de código abierto](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Con IA tardaron 19% más. Antes de empezar pensaban que irían 24% más rápido; después de terminar, seguían creyendo que la IA los aceleró 20%. La percepción y el cronómetro no coincidieron.

En febrero de 2026 METR publicó una actualización honesta: [con herramientas de finales de 2025 los datos apuntan a una aceleración, pero el experimento ya no sirve](https://metr.org/blog/2026-02-24-uplift-update/). Entre el 30% y el 50% de los participantes se guardaron tareas porque no querían hacerlas sin IA, y los que prefieren trabajar sin IA dejaron de participar. Están rediseñando el estudio.

Mi lectura: la IA acelera, pero no lo que crees ni cuanto crees, y la sensación de velocidad es un pésimo instrumento de medición. Por eso en mi equipo no medimos "qué tan rápido se siente", medimos tiempo de ciclo y cuántas veces regresa un cambio de revisión.

La encuesta de Stack Overflow de 2025 completa la foto: [84% de los desarrolladores usa o planea usar IA, 46% desconfía de la exactitud de lo que produce](https://infoworld.com/article/4031673/ai-use-among-software-developers-grows-but-trust-remains-an-issue-stack-overflow-survey.html), y la frustración número uno es lidiar con soluciones que están casi bien. Casi bien, en código, es la forma más cara de estar mal.

## Lo que sí le dejo escribir

Después de dos años usando asistentes y agentes todos los días, esta es mi lista. No es dogma; es lo que me ha dado menos sustos.

**Pruebas.** Es el mejor uso que he encontrado. Le doy la función y le pido casos: los normales, los límites y los que a mí me da flojera escribir. Luego reviso que las pruebas prueben algo (a veces generan pruebas que pasan siempre).

**Código repetitivo.** Validaciones, conversiones entre formatos, clientes de API a partir de la documentación, formularios. Todo lo que ya sé cómo se escribe y no quiero volver a teclear.

**Migraciones y scripts de un solo uso.** Mover datos de una tabla a otra, renombrar cosas en 300 archivos, el script que limpia un CSV una vez. Si se rompe, se nota de inmediato y no queda en producción.

**Documentación y comentarios.** Explicar lo que hace un módulo que escribí hace tres años. Primer borrador de un README. Mensajes de commit.

**El primer borrador de casi todo lo demás.** Le pido una versión, la leo completa y la reescribo. Es más rápido corregir que empezar en blanco, siempre y cuando de verdad la lea completa. Ahí está el truco.

## Lo que no le dejo escribir

**Decisiones de arquitectura.** Qué base de datos, cómo se separan los servicios, qué se cachea y qué no. El modelo propone la solución más común en internet, que casi nunca es la más adecuada para una empresa de 40 personas en México con un servidor y medio.

**Lógica de negocio que no entiendo al 100%.** Si no puedo explicar la regla de cálculo de una comisión, no puedo revisar si el código la implementa bien. Y si no puedo revisar, no puedo firmar.

**Seguridad.** Autenticación, permisos, manejo de secretos, todo lo que toca datos personales. Aquí la IA es útil para revisar, no para escribir. Le pido que encuentre problemas en mi código; no le pido que escriba el código que protege.

**Cualquier cosa que no voy a poder revisar.** Esta es la regla madre. Un agente puede generar 2,000 líneas en diez minutos. Si yo no tengo dos horas para leerlas, no debí pedir 2,000 líneas. Pido 200, las reviso, y sigo.

## Las tres reglas con mi equipo

1. **Quien manda el cambio, lo entiende.** No aceptamos "lo generó la IA" como explicación en una revisión de código. Si no puedes explicar cada bloque, no está listo.
2. **La IA no toca producción sin pasar por las mismas pruebas y la misma revisión que un humano.** Ningún atajo por venir de un agente. De hecho, revisamos más.
3. **Medimos el ciclo, no la sensación.** Tiempo desde que se abre una tarea hasta que se despliega, y cuántas veces regresa de revisión. Si la IA de verdad ayuda, se ve ahí. Si solo se siente, no cuenta.

## Lo que haría yo si estás empezando

Empieza por las pruebas. Es el uso con mejor relación entre beneficio y riesgo, y obliga a tu equipo a leer lo que la IA genera, que es el hábito que después salva todo lo demás.

Luego pasa a los scripts de un solo uso y al código repetitivo. Deja la arquitectura, la lógica de negocio y la seguridad para cuando el equipo ya sepa reconocer una solución "casi correcta" a primera vista. Ese ojo se entrena, y se entrena revisando.

Y mide. Con cronómetro, no con encuesta. METR nos enseñó que hasta los expertos se equivocan al calcular su propia velocidad; no hay razón para pensar que tu equipo (o yo) seamos la excepción.

Esta entrada cierra la primera semana de un calendario que va hasta junio de 2027. Si quieres ver cómo arrancó, empieza por [por qué los pilotos de IA no llegan a producción](/blog/por-que-los-pilotos-de-ia-no-llegan-a-produccion/). Y si tu equipo ya tiene reglas para programar con IA, me gustaría compararlas: [platiquemos](/contacto/).
