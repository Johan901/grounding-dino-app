# Importamos librerías necesarias y configuramos rutas del sistema
import sys
import os

# Añadimos las rutas para que Python pueda acceder correctamente a los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append("/app")

# Cargamos las librerías principales
import streamlit as st
import torch
import cv2
from PIL import Image
import numpy as np

# Importamos funciones utilitarias del modelo Grounding DINO
from groundingdino.util.inference import load_model, load_image, predict, annotate

# Mostramos el título de la interfaz
st.markdown(
    "<h1 style='text-align: center; font-size: 40px;'>🔍 Inferencia con Grounding DINO</h1>",
    unsafe_allow_html=True
)

# Definimos las rutas del archivo de configuración y los pesos preentrenados del modelo
CONFIG_PATH = "groundingdino/config/GroundingDINO_SwinT_OGC.py"
WEIGHTS_PATH = "weights/groundingdino_swint_ogc.pth"

# Creamos una función para cargar el modelo y lo cacheamos para que no se vuelva a cargar cada vez
@st.cache_resource
def cargar_modelo():
    model = load_model(CONFIG_PATH, WEIGHTS_PATH)
    return model.to("cpu")  # Nos aseguramos de que corra en CPU

# Cargamos el modelo
model = cargar_modelo()

# Permitimos al usuario subir una imagen desde su equipo
uploaded_file = st.file_uploader("📤 Sube una imagen para procesar", type=["jpg", "jpeg", "png"])

# Solicitamos al usuario que escriba el texto con el objeto que quiere detectar
prompt = st.text_input("📝 ¿Qué objeto quieres detectar?", value="", placeholder="Ej: a red car")

# Si el usuario sube una imagen
if uploaded_file:
    # Leemos el archivo como bytes
    file_bytes = uploaded_file.read()

    # Convertimos la imagen a formato RGB usando PIL
    image_pil = Image.open(uploaded_file).convert("RGB")

    # Mostramos la imagen original subida por el usuario
    st.subheader("🖼 Imagen original")
    st.image(image_pil, use_container_width=True)

    # Si el usuario hace clic en el botón y ha escrito un prompt
    if st.button("🔎 Hacer predicción") and prompt.strip() != "":
        # Guardamos temporalmente la imagen en disco
        image_path = "examples/temp_input.jpg"
        with open(image_path, "wb") as f:
            f.write(file_bytes)

        # Mostramos mensaje de procesamiento
        st.subheader("🔄 Procesando...")

        # Cargamos la imagen y la preparamos para el modelo
        image_source, image = load_image(image_path)

        # Ejecutamos la inferencia con el modelo Grounding DINO
        boxes, logits, phrases = predict(
            model=model,
            image=image,
            caption=prompt,
            box_threshold=0.3,     # Umbral para mostrar solo cajas con confianza alta
            text_threshold=0.25,   # Umbral para mostrar texto relevante
            device=torch.device("cpu")
        )

        # Anotamos la imagen con las cajas y frases detectadas
        annotated = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)

        # Convertimos la imagen anotada de BGR a RGB (para que se vea bien en Streamlit)
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

        # Mostramos el resultado final con las detecciones
        st.subheader("✅ Resultado")
        st.image(annotated, caption="Predicción", use_container_width=True)
