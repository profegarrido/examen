import streamlit as st
import pandas as pd
import io
import datetime
from io import StringIO

# Ocultar menú de Streamlit (íconos, menú superior y pie de página)
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Título y Descripción del Formulario ---
st.title("📝 Examen")
st.subheader("Introducción a la programación con Python y R")
st.write("Por favor, responde las siguientes 10 preguntas.")
st.write("---")

# --- Sección de Datos del Alumno ---
st.header("Sección de Datos del Alumno")
id_participante = st.text_input("Ingresa tu Nombre:")
st.write("---")

# --- Preguntas del Examen ---
st.header("Preguntas del Examen")

q1_opciones = ["A) 42", "B) Hola Mundo", "C) 3.14159", "D) UAHC", "E) huemul"]
q1 = st.radio("Pregunta 1: ¿Qué elemento imprimirá el código `mi_lista[-2]`?", q1_opciones, key="q1")

q2 = st.text_area("Pregunta 2: ¿Cuál es el código para imprimir **Python** desde `mi_lista`?", key="q2")

q3 = st.text_area("Pregunta 3: Crear una función que calcule el precio con IVA.", key="q3")

q4_opciones = ["A) conda activate web", "B) activate conda web", "C) source web activate", "D) conda create web", "E) conda run web"]
q4 = st.radio("Pregunta 4: ¿Cuál es el código para activar el entorno virtual `web` usando conda?", q4_opciones, key="q4")

q5 = st.text_area("Pregunta 5: ¿Cuántas filas y columnas tiene el  DataFrame (pinguinos)?", key="q5")

q6_opciones = ["A) 91%", "B) 92%", "C) 93%", "D) 94%", "E) 95%"]
q6 = st.radio("Pregunta 6: ¿Cuál es el porcentaje general de completitud?", q6_opciones, key="q6")

q7 = st.text_area("Pregunta 7: Si tuviera que imputar la columna **Body Mass (g)**, ¿qué método usaría y por qué?", key="q7")   

q8 = st.text_area("Pregunta 8: ¿Cuál es la especie mayoritaria y qué porcentaje es?", key="q8")

q9 = st.text_area("Pregunta 9: Graficar la columna body mass usando histograma de matplotlib", key="q9")

q10_opciones = ["A) Biscoe: 15.1%, Dream: 36.0%, Torgersen: 48.8%", "B) Biscoe: 15.1%, Dream: 48.8%, Torgersen: 36.0%", "C) Biscoe: 36.0%, Dream: 48.8%, Torgersen: 15.1%", "D) Biscoe: 48.8%, Dream: 36.0%, Torgersen: 15.1%", "E) Biscoe: 48.8%, Dream: 15.1%, Torgersen: 36.0%"]
q10 = st.radio("Pregunta 10: ¿Cuál es el porcentaje de pinguinos por isla (**island**)?", q10_opciones, key="q10")

# --- Armar DataFrame con respuestas ---
respuestas = {
    "Nombre": [id_participante],
    "Fecha": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "Pregunta 1": [q1],
    "Pregunta 2": [q2],
    "Pregunta 3": [q3],
    "Pregunta 4": [q4],
    "Pregunta 5": [q5],
    "Pregunta 6": [q6],
    "Pregunta 7": [q7],
    "Pregunta 8": [q8],
    "Pregunta 9": [q9],
    "Pregunta 10": [q10],
}

# Convertir a DataFrame de dos columnas
df_respuestas = pd.DataFrame(respuestas.items(), columns=["campo", "respuesta"])

# Convertir a CSV en memoria
csv_buffer = StringIO()
df_respuestas.to_csv(csv_buffer, index=False)
csv_data = csv_buffer.getvalue()

st.download_button(
    label="📥 Enviar mis respuestas",
    data=csv_data,
    file_name=f"respuestas_{id_participante.replace(' ', '_')}.csv",
    mime="text/csv"
)

# df_respuestas = pd.DataFrame(respuestas)

# # --- Convertir a CSV en memoria ---
# csv_buffer = io.StringIO()
# df_respuestas.to_csv(csv_buffer, index=False)
# csv_data = csv_buffer.getvalue()

# # --- Botón para descargar las respuestas del alumno ---
# st.download_button(
#     label="📥 Enviar respuestas",
#     data=csv_data,
#     file_name=f"respuestas_examen_{id_participante or 'alumno'}.csv",
#     mime="text/csv",
#     disabled=(id_participante.strip() == "")
# )

# st.info("Recuerda guardar tu archivo CSV como comprobante de envío.")
