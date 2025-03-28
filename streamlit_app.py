import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Modelo de Madurez GC", layout="wide")

# Título principal
st.title("📊 Modelo de Madurez en Gestión del Conocimiento")
st.markdown("---")

# Menú de navegación
menu = st.sidebar.selectbox("Menú", [
    "🏠 Inicio",
    "📚 Glosario",
    "📝 Encuesta de Diagnóstico",
    "🗺️ Generar Hoja de Ruta",
    "🧠 Recursos Didácticos"
])

# Contenido de cada sección
if menu == "🏠 Inicio":
    st.header("Bienvenido al Analizador de Madurez en GC")
    st.image("https://cdn.pixabay.com/photo/2018/05/08/08/44/artificial-intelligence-3382507_1280.jpg", width=600)
    st.markdown("""
    ### ¿Qué aprenderás aquí?
    1. Fundamentos de la Gestión del Conocimiento (GC)
    2. Niveles del Modelo de Madurez (desde *Principiantes* hasta *Óptimo*)
    3. Cómo evaluar tu empresa con nuestra **Encuesta Interactiva**
    4. Pasos concretos para mejorar usando nuestra **Hoja de Ruta Personalizada**
    """)

elif menu == "📚 Glosario":
    st.header("📖 Glosario de Términos Clave")
    terms = {
        "Conocimiento Tácito": "Saber hacer no formalizado (ej: experiencia de un trabajador).",
        "Capital Intelectual": "Activos intangibles que generan valor (ej: patentes, relaciones con clientes).",
        "Espiral del Conocimiento (Nonaka)": "Proceso SECI: Socialización, Externalización, Combinación, Internalización.",
        "COSO III": "Marco integrado para control interno y gestión de riesgos (2013)."
    }
    for term, definition in terms.items():
        st.subheader(f"**{term}**")
        st.info(definition)

elif menu == "📝 Encuesta de Diagnóstico":
    st.header("🔍 ¿Cuál es tu nivel actual de GC?")
    
    # Preguntas usando escala Likert
    questions = [
        "1. ¿Existen repositorios centralizados para documentación clave?",
        "2. ¿Se realizan capacitaciones periódicas para transferir conocimiento?",
        "3. ¿Utilizan herramientas tecnológicas para compartir conocimiento (ej: intranet)?",
        "4. ¿Hay procesos definidos para capturar lecciones aprendidas?"
    ]
    
    answers = {}
    for q in questions:
        answers[q] = st.slider(q, 1, 5, 3, 
                             help="1 = Nunca | 5 = Siempre")
    
    if st.button("🔎 Calcular Nivel de Madurez"):
        total_score = sum(answers.values())
        if total_score <= 10:
            nivel = "Principiantes sin Conciencia"
        elif total_score <= 15:
            nivel = "Conciencia Básica"
        elif total_score <= 20:
            nivel = "Conocimiento Organizado"
        else:
            nivel = "Nivel Pre-Óptimo/Óptimo"
        
        st.success(f"## Tu nivel actual: {nivel}")
        st.balloons()

elif menu == "🗺️ Generar Hoja de Ruta":
    st.header("🚀 Hoja de Ruta Personalizada")
    nivel = st.selectbox("Selecciona tu nivel actual:", [
        "Principiantes sin Conciencia",
        "Conciencia Básica",
        "Conocimiento Organizado",
        "Pre-Óptimo/Óptimo"
    ])
    
    roadmap = {
        "Principiantes sin Conciencia": [
            "🔹 Identificar conocimiento tácito en colaboradores",
            "🔹 Implementar repositorio digital básico (ej: Google Drive)",
            "🔹 Capacitación inicial sobre conceptos GC"
        ],
        "Conciencia Básica": [
            "🔸 Mapear flujos de conocimiento críticos",
            "🔸 Establecer comunidad de prácticas",
            "🔸 Implementar software colaborativo (ej: Confluence)"
        ],
        "Conocimiento Organizado": [
            "🔺 Vincular GC a objetivos estratégicos",
            "🔺 Sistema de gestión de lecciones aprendidas",
            "🔺 Métricas de ROI del conocimiento"
        ],
        "Pre-Óptimo/Óptimo": [
            "🚀 Integrar IA para análisis predictivo",
            "🚀 Modelos de innovación abierta",
            "🚀 Sistema de reconocimiento por aportes de conocimiento"
        ]
    }
    
    st.subheader(f"Acciones recomendadas para **{nivel}**:")
    for action in roadmap[nivel]:
        st.markdown(f"- {action}")

elif menu == "🧠 Recursos Didácticos":
    st.header("🎓 Material de Apoyo")
    
    with st.expander("📈 Modelo de Madurez (Infografía)"):
        st.image("https://miro.medium.com/v2/resize:fit:1400/1*L7q7wXGjoaDg5k2WJ7gqTA.png")
    
    with st.expander("📼 Video Explicativo"):
        st.video("https://youtu.be/6s0OVWoo8vQ?si=QxQqo5f3Qn6Q0-Xh")
    
    with st.expander("📑 Casos de Éxito"):
        st.markdown("""
        - **Caso Microsoft**: Sistema de mentoría inversa
        - **Caso Siemens**: Plataforma ShareNet para innovación colaborativa
        - **Caso Ecopetrol**: Gestión del conocimiento técnico en yacimientos
        """)

st.markdown("---")
st.caption("© 2023 Modelo de Madurez GC - Desarrollado por Ricardo Castrillon Jimenez")
