# Importamos la librería de Streamlit
import streamlit as st

# Mostramos un encabezado en la página
st.header("📘 Introducción")

# Mostramos una explicación sencilla del concepto de Visual Grounding y del modelo Grounding DINO
st.markdown("""
**Visual Grounding** es el proceso de localizar objetos en imágenes a partir de descripciones de lenguaje natural.
Esta técnica permite interactuar con imágenes usando texto libre.

Grounding DINO es un modelo de código abierto que combina lo mejor de los detectores visuales (DINO) con modelos de lenguaje como BERT para lograr detecciones sin clases predefinidas.
""")
