#!/usr/bin/env python3
"""Genera docs/calendario-editorial.md: tres entradas por semana (lunes, miércoles y viernes, 11:00).

Los títulos usan la forma en que se busca el tema (palabra clave al inicio, sin juegos de palabras).
El estado de cada fila se calcula solo: "publicado" si content/blog/<n>-<slug>.md existe, "por-escribir" si no.
Uso: python3 scripts/calendario.py
"""
import datetime as dt
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
IA, DEV, MT, SEO, CRM, LID, AUTO = ("ia-y-tecnologia", "desarrollo-web", "martech", "seo-y-geo",
                                    "crm-y-datos", "ventas-y-liderazgo", "automotriz")
INICIO = dt.date(2026, 11, 20)
FIN = dt.date(2027, 6, 30)
SIN_PUBLICACION = {dt.date(2026, 12, 25), dt.date(2027, 1, 1)}

# (título, slug, palabra clave, categoría)
ENTRADAS = [
    # IA en la empresa
    ("Estrategia de inteligencia artificial para empresas: cómo empezar", "estrategia-de-inteligencia-artificial-para-empresas", "estrategia de inteligencia artificial", IA),
    ("Casos de uso de inteligencia artificial en empresas: cómo elegir el primero", "casos-de-uso-de-inteligencia-artificial-en-empresas", "casos de uso de inteligencia artificial", IA),
    ("Calidad de datos para inteligencia artificial: qué necesitas antes de empezar", "calidad-de-datos-para-inteligencia-artificial", "calidad de datos para ia", CRM),
    ("Comprar o desarrollar inteligencia artificial: cómo decidir", "comprar-o-desarrollar-inteligencia-artificial", "comprar o desarrollar ia", IA),
    ("Cuánto cuesta implementar inteligencia artificial en una empresa", "cuanto-cuesta-implementar-inteligencia-artificial", "cuánto cuesta implementar inteligencia artificial", IA),
    ("Ejemplos de inteligencia artificial en empresas mexicanas", "ejemplos-de-inteligencia-artificial-en-empresas", "ejemplos de inteligencia artificial en empresas", IA),
    ("Automatización de procesos con inteligencia artificial: guía para empresas", "automatizacion-de-procesos-con-inteligencia-artificial", "automatización de procesos con ia", IA),
    ("Qué es RAG en inteligencia artificial y para qué sirve", "que-es-rag-inteligencia-artificial", "qué es rag", IA),
    ("Cómo evaluar un agente de IA antes de comprarlo", "como-evaluar-un-agente-de-ia", "evaluar agente de ia", IA),
    ("Modelos de IA de código abierto vs. cerrados: diferencias para empresas", "modelos-de-ia-codigo-abierto-vs-cerrados", "modelos de ia de código abierto", IA),
    ("Cómo medir el ROI de un proyecto de inteligencia artificial", "como-medir-el-roi-de-la-inteligencia-artificial", "roi de la inteligencia artificial", IA),
    ("Chatbot con inteligencia artificial para atención al cliente: cuándo sí conviene", "chatbot-con-ia-para-atencion-al-cliente", "chatbot con ia para atención al cliente", IA),
    ("Shadow AI: qué es y cómo controlarlo en tu empresa", "shadow-ai-que-es", "shadow ai", IA),
    ("Política de uso de inteligencia artificial para empresas (plantilla)", "politica-de-uso-de-inteligencia-artificial-plantilla", "política de uso de inteligencia artificial", IA),
    ("Cómo preparar tu sitio web para el Buen Fin y picos de tráfico", "preparar-sitio-web-para-picos-de-trafico", "preparar sitio web para picos de tráfico", DEV),
    # Presupuesto y cierre de año
    ("Presupuesto de TI 2027: cómo armarlo y en qué invertir", "presupuesto-de-ti-2027", "presupuesto de ti", LID),
    ("Cómo elegir un proveedor de inteligencia artificial: preguntas clave", "como-elegir-proveedor-de-inteligencia-artificial", "proveedor de inteligencia artificial", IA),
    ("Deuda técnica: qué es, cómo medirla y cómo reducirla", "deuda-tecnica-que-es", "deuda técnica", DEV),
    ("Auditoría de herramientas de software: cómo reducir licencias que no usas", "auditoria-de-herramientas-de-software", "auditoría de software", MT),
    ("Herramientas de automatización para empresas: cuáles valen la pena", "herramientas-de-automatizacion-para-empresas", "herramientas de automatización", IA),
    ("Cómo explicar un proyecto de IA a la dirección general", "como-presentar-un-proyecto-de-ia-a-direccion", "presentar proyecto de ia", LID),
    ("Inteligencia artificial para pymes: plan de 90 días", "inteligencia-artificial-para-pymes", "inteligencia artificial para pymes", IA),
    ("Herramientas para un CTO: software que uso todos los días", "herramientas-para-un-cto", "herramientas para cto", IA),
    ("Tendencias de inteligencia artificial 2027 para empresas", "tendencias-de-inteligencia-artificial-2027", "tendencias inteligencia artificial 2027", IA),
    ("Libros de tecnología y liderazgo recomendados para 2027", "libros-de-tecnologia-y-liderazgo-2027", "libros de tecnología", LID),
    # Arquitectura y equipos
    ("Roadmap tecnológico: qué es y cómo hacerlo (con plantilla)", "roadmap-tecnologico-como-hacerlo", "roadmap tecnológico", LID),
    ("Empleos que cambiará la inteligencia artificial en México", "empleos-que-cambiara-la-inteligencia-artificial", "empleos inteligencia artificial", IA),
    ("Arquitectura de datos para inteligencia artificial: guía práctica", "arquitectura-de-datos-para-inteligencia-artificial", "arquitectura de datos", DEV),
    ("Cómo armar un equipo de tecnología en una empresa mediana", "como-armar-un-equipo-de-tecnologia", "equipo de tecnología", LID),
    ("Chief AI Officer: qué hace y cuándo lo necesita tu empresa", "chief-ai-officer-que-hace", "chief ai officer", LID),
    ("Agentes de IA para automatizar tareas: ejemplos reales", "agentes-de-ia-para-automatizar-tareas", "agentes de ia ejemplos", IA),
    ("Qué es MCP (Model Context Protocol) y para qué sirve", "que-es-mcp-model-context-protocol", "qué es mcp", IA),
    ("Pruebas automatizadas con inteligencia artificial: cómo empezar", "pruebas-automatizadas-con-inteligencia-artificial", "pruebas automatizadas con ia", DEV),
    ("Inyección de prompts: qué es y cómo proteger tu aplicación", "inyeccion-de-prompts-que-es", "inyección de prompts", IA),
    ("Seguridad en aplicaciones con LLM: checklist para empresas", "seguridad-en-aplicaciones-con-llm", "seguridad llm", IA),
    ("Cómo evaluar una demo de inteligencia artificial", "como-evaluar-una-demo-de-inteligencia-artificial", "demo de inteligencia artificial", IA),
    ("Datos propios como ventaja competitiva: cómo aprovecharlos con IA", "datos-propios-ventaja-competitiva", "datos propios ventaja competitiva", CRM),
    ("Base de conocimiento para IA: cómo crearla paso a paso", "base-de-conocimiento-para-ia", "base de conocimiento para ia", IA),
    ("Cómo escribir prompts para ChatGPT y Claude en el trabajo", "como-escribir-prompts-en-el-trabajo", "cómo escribir prompts", IA),
    # Datos y CRM
    ("CRM con inteligencia artificial: qué es y cómo usarlo", "crm-con-inteligencia-artificial", "crm con inteligencia artificial", CRM),
    ("Automatización de ventas en el CRM: ejemplos que funcionan", "automatizacion-de-ventas-en-el-crm", "automatización de ventas crm", CRM),
    ("Enriquecimiento de leads con inteligencia artificial: cómo hacerlo bien", "enriquecimiento-de-leads-con-ia", "enriquecimiento de leads", CRM),
    ("Personalización con inteligencia artificial en marketing: límites y ejemplos", "personalizacion-con-inteligencia-artificial", "personalización con ia", MT),
    ("Pipeline de datos: qué es y cómo armar uno sencillo", "pipeline-de-datos-que-es", "pipeline de datos", CRM),
    ("Dashboard de indicadores para dirección: qué métricas incluir", "dashboard-de-indicadores-para-direccion", "dashboard de indicadores", CRM),
    ("Atención al cliente con inteligencia artificial: casos y errores comunes", "atencion-al-cliente-con-inteligencia-artificial", "atención al cliente con ia", IA),
    ("Cómo transferir de un chatbot a un agente humano", "transferir-de-chatbot-a-agente-humano", "chatbot a agente humano", IA),
    ("Métricas de un chatbot: cuáles medir y cuáles no", "metricas-de-un-chatbot", "métricas chatbot", IA),
    ("Inteligencia artificial y protección de datos personales en México", "inteligencia-artificial-y-proteccion-de-datos-personales", "ia y protección de datos personales", CRM),
    ("Cómo anonimizar datos personales antes de usar IA", "como-anonimizar-datos-personales", "anonimizar datos", CRM),
    ("Dónde se guardan tus datos en la nube: residencia de datos en México", "residencia-de-datos-en-la-nube-mexico", "residencia de datos", IA),
    # Software con IA
    ("Vibe coding: qué es y cuándo usarlo en producción", "vibe-coding-que-es", "vibe coding", DEV),
    ("Cómo revisar código generado por IA: checklist", "como-revisar-codigo-generado-por-ia", "revisar código generado por ia", DEV),
    ("Refactorizar código con inteligencia artificial: guía práctica", "refactorizar-codigo-con-inteligencia-artificial", "refactorizar código con ia", DEV),
    ("Desarrolladores junior e inteligencia artificial: cómo cambia el trabajo", "desarrolladores-junior-e-inteligencia-artificial", "desarrolladores junior ia", LID),
    ("Cómo capacitar a un equipo de desarrollo en inteligencia artificial", "capacitar-equipo-de-desarrollo-en-ia", "capacitación en ia para desarrolladores", LID),
    ("¿Hay que aprender a programar con la inteligencia artificial?", "aprender-a-programar-con-inteligencia-artificial", "aprender a programar con ia", DEV),
    ("Inteligencia artificial en WordPress y Shopify: qué cambia para tu sitio", "inteligencia-artificial-en-wordpress-y-shopify", "inteligencia artificial wordpress", DEV),
    ("Cómo publicar en WordPress desde Git con la API REST", "publicar-en-wordpress-desde-git-api-rest", "wordpress api rest", DEV),
    ("Mejores plugins de inteligencia artificial para WordPress", "mejores-plugins-de-inteligencia-artificial-para-wordpress", "plugins de ia para wordpress", DEV),
    ("Velocidad de carga de un sitio web: por qué sigue importando", "velocidad-de-carga-de-un-sitio-web", "velocidad de carga sitio web", SEO),
    ("Core Web Vitals: cómo medirlos y mejorarlos", "core-web-vitals-como-mejorarlos", "core web vitals", DEV),
    ("Pruebas de carga para sitios web: herramientas y cómo hacerlas", "pruebas-de-carga-para-sitios-web", "pruebas de carga", DEV),
    ("Nube o servidor propio: cómo elegir para tu empresa", "nube-o-servidor-propio", "nube o servidor propio", DEV),
    ("Cómo reducir costos de nube al usar inteligencia artificial", "reducir-costos-de-nube-con-ia", "reducir costos de nube", DEV),
    ("Serverless: qué es, ventajas y costos reales", "serverless-que-es-costos", "serverless costos", DEV),
    # Marketing, SEO y GEO
    ("Marketing con inteligencia artificial: guía para empresas", "marketing-con-inteligencia-artificial", "marketing con inteligencia artificial", MT),
    ("Cómo crear contenido con inteligencia artificial sin perder calidad", "crear-contenido-con-inteligencia-artificial", "crear contenido con ia", MT),
    ("Investigación de mercado con inteligencia artificial: cómo hacerla", "investigacion-de-mercado-con-inteligencia-artificial", "investigación de mercado con ia", MT),
    ("Qué es GEO (Generative Engine Optimization) y cómo aplicarlo", "que-es-geo-generative-engine-optimization", "qué es geo", SEO),
    ("Cómo aparecer en ChatGPT, Perplexity y AI Overviews", "como-aparecer-en-chatgpt-y-ai-overviews", "cómo aparecer en chatgpt", SEO),
    ("Qué es llms.txt y si tu sitio lo necesita", "que-es-llms-txt", "llms.txt", SEO),
    ("Performance Max: qué es y cómo auditar tus campañas", "performance-max-como-auditar", "performance max", MT),
    ("Meta Advantage+: cómo funciona y cuándo usarlo", "meta-advantage-plus-como-funciona", "advantage+", MT),
    ("Anuncios creados con inteligencia artificial: herramientas y resultados", "anuncios-con-inteligencia-artificial", "anuncios con ia", MT),
    ("Stack de martech: cómo elegir herramientas en 2027", "stack-de-martech-como-elegir", "stack de martech", MT),
    ("Cómo consolidar herramientas de marketing sin perder datos", "consolidar-herramientas-de-marketing", "consolidar herramientas de marketing", MT),
    ("Qué es un CDP (Customer Data Platform) y si lo necesitas", "que-es-un-cdp-customer-data-platform", "qué es un cdp", MT),
    # Liderazgo técnico
    ("Qué hace un CTO: funciones y responsabilidades", "que-hace-un-cto-funciones", "qué hace un cto", LID),
    ("Entrevista técnica para desarrolladores en la era de la IA", "entrevista-tecnica-para-desarrolladores", "entrevista técnica desarrolladores", LID),
    ("Cómo organizar reuniones de equipo de ingeniería efectivas", "reuniones-de-equipo-de-ingenieria", "reuniones de ingeniería", LID),
    ("Cómo justificar el presupuesto de tecnología ante dirección", "justificar-presupuesto-de-tecnologia", "presupuesto de tecnología", LID),
    ("Caso de negocio para un proyecto de tecnología (plantilla)", "caso-de-negocio-proyecto-de-tecnologia", "caso de negocio", LID),
    ("Cómo demostrar el valor del área de TI en la empresa", "valor-del-area-de-ti", "valor de ti en la empresa", LID),
    ("Agencia, freelancer o equipo interno de desarrollo: cómo elegir", "agencia-freelancer-o-equipo-interno", "agencia o freelancer", LID),
    ("Contrato de desarrollo de software: cláusulas sobre inteligencia artificial", "contrato-de-desarrollo-de-software-clausulas-ia", "contrato de desarrollo de software", LID),
    ("Certificaciones de TI: cuáles valen la pena al contratar", "certificaciones-de-ti-al-contratar", "certificaciones de ti", LID),
    ("Dependencia de un proveedor de IA (vendor lock-in): cómo evitarla", "vendor-lock-in-inteligencia-artificial", "vendor lock-in", IA),
    ("Cómo cambiar de modelo de IA sin reescribir tu aplicación", "cambiar-de-modelo-de-ia", "cambiar de modelo de ia", DEV),
    ("Evals de IA: cómo evaluar un modelo para tu caso de uso", "evals-de-ia-como-evaluar-un-modelo", "evaluar modelos de ia", IA),
    ("Inteligencia artificial en la industria automotriz: ventas y agencias", "inteligencia-artificial-en-la-industria-automotriz", "inteligencia artificial automotriz", AUTO),
    ("Seguimiento de leads automotrices con inteligencia artificial", "seguimiento-de-leads-automotrices-con-ia", "leads automotrices", AUTO),
    ("Asistente virtual para agencias de autos: qué puede y qué no", "asistente-virtual-para-agencias-de-autos", "asistente virtual agencia de autos", AUTO),
    # Mitad de año
    ("Resultados de la inteligencia artificial en empresas: balance 2027", "resultados-de-la-inteligencia-artificial-en-empresas-2027", "resultados inteligencia artificial empresas", IA),
    ("Cómo calcular el retorno de inversión de la automatización", "retorno-de-inversion-de-la-automatizacion", "roi automatización", IA),
    ("Presupuesto de TI 2028: cómo empezar a planearlo", "presupuesto-de-ti-2028", "presupuesto de ti 2028", LID),
    ("Ética en la inteligencia artificial para empresas: reglas prácticas", "etica-en-la-inteligencia-artificial-para-empresas", "ética de la inteligencia artificial", IA),
    ("Cómo informar a tus clientes que usas inteligencia artificial", "informar-a-clientes-uso-de-inteligencia-artificial", "transparencia uso de ia", MT),
    ("Sesgos en la inteligencia artificial: qué son y cómo detectarlos", "sesgos-en-la-inteligencia-artificial", "sesgos de la ia", IA),
    ("Calendario editorial con inteligencia artificial: cómo hacerlo", "calendario-editorial-con-inteligencia-artificial", "calendario editorial", MT),
]

DIAS = {0: "lunes", 2: "miércoles", 4: "viernes"}
MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()


def slots():
    d = INICIO
    while d <= FIN:
        if d.weekday() in DIAS and d not in SIN_PUBLICACION:
            yield d
        d += dt.timedelta(days=1)


def estado(slug):
    hits = list((ROOT / "content/blog").glob(f"*-{slug}.md"))
    if not hits:
        return "por-escribir"
    txt = hits[0].read_text(encoding="utf-8")
    return "publicado" if "\nstatus: publish" in txt else "borrador"


def main():
    fechas = list(slots())
    filas = list(zip(fechas, ENTRADAS))
    assert len({e[1] for e in ENTRADAS}) == len(ENTRADAS), "slug repetido"
    out = [
        "# Calendario editorial: noviembre 2026 a junio 2027",
        "",
        "Tres entradas por semana (lunes, miércoles y viernes a las 11:00) sobre tecnología e inteligencia artificial, desde la perspectiva de un CTO práctico y pragmático.",
        "",
        "Reglas de títulos (desde el 18 nov 2026): el título usa la forma en que la gente busca el tema, con la palabra clave al inicio. Nada de juegos de palabras ni metáforas en el título; la opinión y el tono van en el texto. El slug de la tabla es fijo.",
        "",
        "Este archivo se genera con `python3 scripts/calendario.py`: para cambiar títulos, fechas u orden se edita la lista del script y se vuelve a correr. El estado sale solo de content/blog: publicado, borrador o por-escribir. No hay publicación el 25 de diciembre ni el 1 de enero.",
        "",
        "Publicadas antes de este calendario (21 oct a 18 nov 2026): entradas 47 a 52 de content/blog.",
        "",
        "| Fecha | Día | Título | Slug | Palabra clave | Categoría | Estado |",
        "|---|---|---|---|---|---|---|",
    ]
    for d, (t, s, k, c) in filas:
        out.append(f"| {d.isoformat()} | {DIAS[d.weekday()]} | {t} | {s} | {k} | {c} | {estado(s)} |")
    sobran = ENTRADAS[len(fechas):]
    if sobran:
        out += ["", "## Sin fecha (reserva)", ""] + [f"- {t} ({s})" for t, s, _, _ in sobran]
    text = "\n".join(out) + "\n"
    assert "—" not in text and "–" not in text
    (ROOT / "docs/calendario-editorial.md").write_text(text, encoding="utf-8")
    print(f"{len(filas)} con fecha ({filas[0][0]} a {filas[-1][0]}), {len(sobran)} en reserva, {len(fechas) - len(filas)} huecos")


if __name__ == "__main__":
    main()
