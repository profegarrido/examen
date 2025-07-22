import streamlit as st
import pandas as pd
import os
import datetime # Para añadir la fecha y hora del envío

# Ocultar menú de Streamlit (íconos, menú superior y pie de página)
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Ocultar menú de Streamlit (íconos, menú superior y pie de página)

# --- Configuración del Archivo CSV ---
ARCHIVO_RESPUESTAS = 'respuestas_examen.csv'

# Columnas iniciales del CSV
# Asegúrate de que estas coincidan con las preguntas que harás
COLUMNAS = [
    'Marca_Temporal', 'ID_Participante', 'Pregunta_1_Corta', 'Pregunta_2_Multiple',
    'Pregunta_3_Corta', 'Pregunta_4_Multiple', 'Pregunta_5_Corta',
    'Pregunta_6_Multiple', 'Pregunta_7_Corta', 'Pregunta_8_Multiple',
    'Pregunta_9_Corta', 'Pregunta_10_Multiple'
]

# Crear el archivo CSV si no existe
if not os.path.exists(ARCHIVO_RESPUESTAS):
    df_vacio = pd.DataFrame(columns=COLUMNAS)
    df_vacio.to_csv(ARCHIVO_RESPUESTAS, index=False)

# --- Título y Descripción del Formulario ---
st.title("📝 Examen de Prueba de Conocimientos")
st.write("Por favor, responde las siguientes 10 preguntas.")
st.write("---")

# --- Formulario de Preguntas ---
# Usamos st.form para agrupar las preguntas y el botón de envío
with st.form("examen_form"):
    st.header("Sección de Datos del Participante")
    id_participante = st.text_input("Ingresa tu ID de Participante:")
    st.write("---")

    st.header("Preguntas del Examen")

    # Pregunta 1: Respuesta Corta
    q1 = st.text_area("Pregunta 1: ¿Cuál es la capital de Chile?", key="q1_corta")

    # Pregunta 2: Selección Múltiple
    q2_opciones = ["A) Rojo", "B) Azul", "C) Verde", "D) Amarillo"]
    q2 = st.radio("Pregunta 2: ¿De qué color es el cielo en un día soleado?", q2_opciones, key="q2_multiple")

    # Pregunta 3: Respuesta Corta
    q3 = st.text_area("Pregunta 3: Menciona un animal mamífero.", key="q3_corta")

    # Pregunta 4: Selección Múltiple
    q4_opciones = ["A) Sol", "B) Marte", "C) Tierra", "D) Júpiter"]
    q4 = st.radio("Pregunta 4: ¿Cuál es el tercer planeta del sistema solar?", q4_opciones, key="q4_multiple")

    # Pregunta 5: Respuesta Corta
    q5 = st.text_area("Pregunta 5: ¿Qué lenguaje de programación estamos usando en Streamlit?", key="q5_corta")

    # Pregunta 6: Selección Múltiple
    q6_opciones = ["A) 1", "B) 2", "C) 3", "D) 4"]
    q6 = st.radio("Pregunta 6: ¿Cuántos lados tiene un triángulo?", q6_opciones, key="q6_multiple")

    # Pregunta 7: Respuesta Corta
    q7 = st.text_area("Pregunta 7: Nombra una fruta cítrica.", key="q7_corta")

    # Pregunta 8: Selección Múltiple
    q8_opciones = ["A) Agua", "B) Oxígeno", "C) Hierro", "D) Nitrógeno"]
    q8 = st.radio("Pregunta 8: ¿Cuál es el gas más abundante en la atmósfera terrestre?", q8_opciones, key="q8_multiple")

    # Pregunta 9: Respuesta Corta
    q9 = st.text_area("Pregunta 9: ¿Qué herramienta de visualización de datos usamos con Python?", key="q9_corta")

    # Pregunta 10: Selección Múltiple
    q10_opciones = ["A) Marte", "B) Venus", "C) Luna", "D) Sol"]
    q10 = st.radio("Pregunta 10: ¿Cuál es la estrella más cercana a la Tierra?", q10_opciones, key="q10_multiple")

    st.write("---")

    # Botón de envío del formulario
    submitted = st.form_submit_button("Enviar Respuestas")

    # --- Lógica para Guardar Respuestas ---
    if submitted:
        if not id_participante:
            st.error("Por favor, ingresa tu ID de Participante para enviar el examen.")
        else:
            # Obtener la marca de tiempo actual
            marca_temporal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Crear una fila con las respuestas
            nueva_respuesta = pd.DataFrame([{
                'Marca_Temporal': marca_temporal,
                'ID_Participante': id_participante,
                'Pregunta_1_Corta': q1,
                'Pregunta_2_Multiple': q2,
                'Pregunta_3_Corta': q3,
                'Pregunta_4_Multiple': q4,
                'Pregunta_5_Corta': q5,
                'Pregunta_6_Multiple': q6,
                'Pregunta_7_Corta': q7,
                'Pregunta_8_Multiple': q8,
                'Pregunta_9_Corta': q9,
                'Pregunta_10_Multiple': q10
            }])

            # Cargar el CSV existente y añadir la nueva respuesta
            try:
                df_respuestas = pd.read_csv(ARCHIVO_RESPUESTAS)
            except Exception as e:
                st.error(f"Error al leer el archivo de respuestas: {e}. Asegúrate de que sea un CSV válido.")
                df_respuestas = pd.DataFrame(columns=COLUMNAS) # Crear uno vacío si falla la lectura

            df_respuestas = pd.concat([df_respuestas, nueva_respuesta], ignore_index=True)

            # Guardar el DataFrame actualizado de nuevo al CSV
            df_respuestas.to_csv(ARCHIVO_RESPUESTAS, index=False)

            st.success("¡Respuestas enviadas y guardadas correctamente!")
            st.info("Puedes cerrar esta ventana o enviar otra respuesta.")

            # Opcional: Mostrar las respuestas guardadas (solo para propósitos de depuración/demostración)
            # st.subheader("Respuestas guardadas hasta ahora:")
            # st.dataframe(df_respuestas)