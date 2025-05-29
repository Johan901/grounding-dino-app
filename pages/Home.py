# Importamos las librerías necesarias
import streamlit as st
from streamlit_lottie import st_lottie  # Para mostrar animaciones Lottie
import requests  # Para hacer solicitudes HTTP y traer la animación

# Función para cargar una animación Lottie desde una URL
def load_lottie_url(url):
    return requests.get(url).json()

# Cargamos la animación desde LottieFiles 
lottie = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json")

# Mostramos el título principal de la app
st.title("👋 Bienvenido")

# Mensaje de introducción explicando el propósito de la aplicación
st.write("Esta app permite explorar Grounding DINO para grounding visual basado en texto.")

# Mostramos la animación Lottie como elemento visual atractivo
st_lottie(lottie, height=300)
