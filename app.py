# Importamos las librerías necesarias
import streamlit as st
from streamlit_option_menu import option_menu  # Para menú lateral personalizado
import sys
import os

# Agregamos rutas para permitir la correcta importación de módulos desde el proyecto o desde Docker
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append("/app")  # Usado especialmente si se corre dentro de un contenedor Docker

# Configuramos la página principal de la app en Streamlit
st.set_page_config(
    page_title="Grounding DINO App",  # Título de la pestaña
    layout="wide",                    # Layout ancho
    page_icon="🦕"                    # Icono de dinosaurio
)

# Aplicamos estilo personalizado con CSS para modificar fondo y ocultar el pie de página
st.markdown(
    """
    <style>
        .main {background-color: #F0F2F6;}  /* Color de fondo */
        footer {visibility: hidden;}        /* Oculta el footer de Streamlit */
    </style>
    """,
    unsafe_allow_html=True,
)

# Mostramos el título de la aplicación en la parte superior
st.title("🦕 Grounding DINO: Marrying DINO with Grounded Pre-Training")

# Mostramos una breve descripción de bienvenida
st.write("Bienvenido a la plataforma interactiva de visual grounding.")
