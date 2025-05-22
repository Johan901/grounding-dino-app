import streamlit as st
import torch
import cv2
from PIL import Image
import numpy as np
from groundingdino.util.inference import load_model, load_image, predict, annotate

st.markdown("<h1 style='text-align: center; font-size: 40px;'>🔍 Inferencia con Grounding DINO</h1>", unsafe_allow_html=True)

CONFIG_PATH = "groundingdino/config/GroundingDINO_SwinT_OGC.py"
WEIGHTS_PATH = "weights/groundingdino_swint_ogc.pth"

@st.cache_resource
def cargar_modelo():
    model = load_model(CONFIG_PATH, WEIGHTS_PATH)
    return model.to("cpu")

model = cargar_modelo()

uploaded_file = st.file_uploader("📤 Subí una imagen para procesar", type=["jpg", "jpeg", "png"])
prompt = st.text_input("📝 ¿Qué objeto querés detectar?", value="", placeholder="Ej: a red car")

# Solo si hay imagen
if uploaded_file:
    file_bytes = uploaded_file.read()
    image_pil = Image.open(uploaded_file).convert("RGB")
    st.subheader("🖼 Imagen original")
    st.image(image_pil, use_container_width=True)

    if st.button("🔎 Hacer predicción") and prompt.strip() != "":
        image_path = "examples/temp_input.jpg"
        with open(image_path, "wb") as f:
            f.write(file_bytes)  # usamos los bytes guardados antes

        st.subheader("🔄 Procesando...")

        image_source, image = load_image(image_path)
        boxes, logits, phrases = predict(
            model=model,
            image=image,
            caption=prompt,
            box_threshold=0.3,
            text_threshold=0.25,
            device=torch.device("cpu")
        )

        annotated = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)
        annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

        st.subheader("✅ Resultado")
        st.image(annotated, caption="Predicción", use_container_width=True)
