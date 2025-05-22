import os
import torch
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # CPU

from groundingdino.util.inference import load_model, load_image, predict, annotate
import cv2

# Configuraciones
CONFIG_PATH = "groundingdino/config/GroundingDINO_SwinT_OGC.py"
WEIGHTS_PATH = "weights/groundingdino_swint_ogc.pth"
IMAGE_PATH = "examples/"
TEXT_PROMPT = ""
BOX_THRESHOLD = 0.3
TEXT_THRESHOLD = 0.25
OUTPUT_PATH = "outputs/TEST_output.jpg"


# Cargar modelo y forzar a CPU
print("Cargando modelo...")
device = torch.device("cpu")
model = load_model(CONFIG_PATH, WEIGHTS_PATH)
model = model.to(device)  

# Cargar imagen 
print("Cargando imagen...")
image_source, image = load_image(IMAGE_PATH)
boxes, logits, phrases = predict(
    model=model,
    image=image,
    caption=TEXT_PROMPT,
    box_threshold=BOX_THRESHOLD,
    text_threshold=TEXT_THRESHOLD,
    device=device  # 
)

#guardar resultado
print("Dibujando resultados...")
annotated_frame = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)
os.makedirs("outputs", exist_ok=True)
cv2.imwrite(OUTPUT_PATH, annotated_frame)
print(f"Inferencia completada. Imagen guardada en: {OUTPUT_PATH}")
