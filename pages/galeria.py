# Importamos las librerías necesarias
import streamlit as st
from PIL import Image  # Para cargar imágenes
import os  # Para manejar rutas de archivos

# Mostramos el título principal centrado
st.markdown("<h1 style='text-align: center;'>🖼 Galería de Inferencias</h1>", unsafe_allow_html=True)

# Texto descriptivo debajo del título
st.markdown("""
Estas son algunas de las inferencias realizadas con Grounding DINO.  
Cada imagen incluye su tiempo de respuesta promedio.
""")

# Definimos la ruta donde están guardadas las imágenes de la galería
img_dir = os.path.join(os.path.dirname(__file__), "gallery")

# Listamos todos los archivos .png en la carpeta 'gallery', ordenados alfabéticamente
img_files = sorted([f for f in os.listdir(img_dir) if f.endswith(".png")])

# Lista de tiempos de inferencia (estos fueron nuestros resultados)
tiempos = [20, 17, 19, 19, 21, 22]

# Mostramos cada imagen con su tiempo de inferencia correspondiente
for i, (img_name, tiempo) in enumerate(zip(img_files, tiempos)):
    # Abrimos la imagen con PIL
    image = Image.open(os.path.join(img_dir, img_name))
    
    # Mostramos la imagen en la app con su texto
    st.image(image, caption=f"Inferencia #{i+1} - {tiempo} segundos", use_container_width=False)
    
    # Insertamos una línea divisoria para separar cada imagen
    st.markdown("---")
