# Este archivo lo creamos y utilizamos solamente para pruebas en local
# Importamos las librerías necesarias
import os
import torch
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Forzamos a que se use solo CPU

# Importamos las funciones de inferencia desde Grounding DINO
from groundingdino.util.inference import load_model, load_image, predict, annotate
import cv2  # Para guardar la imagen resultante

# Configuración del modelo y rutas
CONFIG_PATH = "groundingdino/config/GroundingDINO_SwinT_OGC.py"  # Configuración del modelo
WEIGHTS_PATH = "weights/groundingdino_swint_ogc.pth"              # Pesos preentrenados
IMAGE_PATH = "examples/"                                          # Carpeta de imágenes de entrada
TEXT_PROMPT = ""                                                  # Texto para detección 
BOX_THRESHOLD = 0.3                                               # Umbral de confianza para cajas
TEXT_THRESHOLD = 0.25                                             # Umbral de confianza para texto
OUTPUT_PATH = "outputs/TEST_output.jpg"                           # Ruta para guardar resultado


# Carga del modelo
print("Cargando modelo...")
device = torch.device("cpu")  # Indicamos que se usará CPU
model = load_model(CONFIG_PATH, WEIGHTS_PATH)
model = model.to(device)      # Movemos el modelo a CPU


# Carga del modelo e inferencia 
print("Cargando imagen...")
image_source, image = load_image(IMAGE_PATH)  # Cargamos imagen y tensor

# Realizamos la inferencia usando el prompt de texto
boxes, logits, phrases = predict(
    model=model,
    image=image,
    caption=TEXT_PROMPT,
    box_threshold=BOX_THRESHOLD,
    text_threshold=TEXT_THRESHOLD,
    device=device
)


# Guardamos los resultados
print("Dibujando resultados...")

# Dibujamos cajas y etiquetas sobre la imagen original
annotated_frame = annotate(image_source=image_source, boxes=boxes, logits=logits, phrases=phrases)

# Creamos la carpeta de salida si no existe
os.makedirs("outputs", exist_ok=True)

# Guardamos la imagen anotada
cv2.imwrite(OUTPUT_PATH, annotated_frame)
print(f"Inferencia completada. Imagen guardada en: {OUTPUT_PATH}")
