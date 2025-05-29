# 🦕 Grounding DINO App – Sistema de Localización Visual Guiado por Texto

Esta es una aplicación web interactiva construida con **Python** y **Streamlit**, que permite a los usuarios realizar tareas de *Visual Grounding* mediante el modelo **Grounding DINO**. Además, la aplicación es completamente portable gracias a su contenedor Docker. Con esta app, cualquier persona puede subir una imagen, escribir una descripción en lenguaje natural (por ejemplo, "a red car"), y obtener la predicción visual del objeto indicado, destacado con cajas delimitadoras (bounding boxes).

---

## ✒️ Autores del Proyecto

- **Johan Hurtado**
- **Andrés Enríquez**

Este proyecto fue desarrollado como una iniciativa para explorar la integración de modelos de lenguaje y visión computacional en aplicaciones accesibles para el usuario final.

---

## 🎯 Objetivo del Proyecto

El objetivo de esta aplicación es democratizar el acceso a modelos de detección basados en texto, permitiendo a cualquier persona interactuar con imágenes sin necesidad de conocer clases predefinidas. Basta con describir lo que desea localizar en la imagen, y el sistema se encargará del resto.

---

## ❓ ¿Qué es Visual Grounding y por qué es importante?

**Visual Grounding** es la tarea de localizar objetos en imágenes a partir de descripciones textuales. Es una tecnología fundamental en aplicaciones como:
- Interfaces multimodales (ej. asistentes virtuales)
- Edición automática de imágenes
- Navegación autónoma con lenguaje natural
- Análisis de imágenes médicas guiado por texto

---

## 🔍 ¿Qué es Grounding DINO?

**Grounding DINO** es un modelo de código abierto que combina:
- **DINO** (DETR con mejor entrenamiento) para detección de objetos
- **Modelos de lenguaje como BERT** para procesar descripciones en texto

Este modelo permite identificar objetos en una imagen a partir de **descripciones naturales**, sin estar limitado a un conjunto de clases fijas. Está entrenado con millones de pares texto-imagen y logra detección en entornos abiertos (*open-set detection*).

---

## 🧠 Arquitectura del Sistema

```text
Usuario (imagen + descripción en texto)
        ↓
Interfaz Web en Streamlit
        ↓
Grounding DINO (Transformers en CPU)
        ↓
Procesamiento y visualización con OpenCV
        ↓
Resultado: imagen anotada con bounding boxes
```

### Componentes:

- **Backbone Visual**: Swin Transformer
- **Text Encoder**: BERT base uncased
- **Cross-Modal Attention**: alinea texto e imagen
- **Decoder tipo DETR**: predice cajas de objetos relevantes al texto

---


## :sauropod: Modelo: Grounding DINO

Incluye: una estructura de texto, una estructura de imágenes, un potenciador de funciones, una selección de consultas guiada por idioma y un decodificador de modalidades cruzadas.
![arch](.asset/arch.png)

---

## 🚀 Cómo Ejecutar la Aplicación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Johan901/grounding-dino-app.git
cd grounding-dino-app
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
venv\Scripts\activate     # En Windows
pip install -r requirements.txt
```

### 3. Descargar los pesos del modelo

Debes colocar el siguiente archivo en una carpeta `weights/`:

📥 [`groundingdino_swint_ogc.pth`](https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth)

### 4. Ejecutar la aplicación localmente

```bash
streamlit run app.py
```

---


---

## 🐳 Ejecutar con Docker

También puedes correr la aplicación en un contenedor Docker sin necesidad de instalar dependencias localmente.

### 1. Clonar el repositorio

```bash
git clone https://github.com/Johan901/grounding-dino-app.git
cd grounding-dino-app
```

### 2. Construir la imagen Docker

```bash
docker build -t grounding-dino-app .
```

### 3. Ejecutar el contenedor

```bash
docker run -p 8501:8501 grounding-dino-app
```

### 4. Acceder desde el navegador

```
http://localhost:8501
```

> Asegúrate de tener el archivo `groundingdino_swint_ogc.pth` dentro de la carpeta `weights/` antes de construir la imagen.


## 🧩 Estructura del Proyecto

```text
GroundingDINO/
├── app.py                    ← punto de entrada principal
├── pages/
│   ├── Home.py               ← página de bienvenida
│   ├── Introduccion.py       ← explica visual grounding
│   ├── Arquitectura.py       ← arquitectura explicada + gráfico
│   └── Inferencia.py         ← permite subir imagen y hacer predicción
├── groundingdino/            ← implementación del modelo original
├── weights/                  ← pesos descargados del modelo
├── examples/                 ← imágenes subidas por el usuario
├── outputs/                  ← imágenes procesadas
├── requirements.txt
└── README.md
```

---

## 🛠️ Tecnologías y Librerías Utilizadas

- **Python 3.8**
- **Streamlit** (interfaz web)
- **PyTorch** (inferencia del modelo)
- **Transformers - Hugging Face**
- **OpenCV** (anotación de imágenes)
- **Plotly** (visualizaciones)
- **Lottie** (animaciones visuales)
- **PIL, NumPy, Matplotlib**

---

## 🎓 Aplicaciones Prácticas

Este sistema puede adaptarse a:
- Interfaces con IA multimodal
- Plataformas de accesibilidad visual
- Educación en visión computacional
- Herramientas de etiquetado automático de datasets
- Edición de imágenes orientada por lenguaje

---

## 📜 Licencia

Este proyecto ha sido creado con fines académicos y de investigación. Su uso está permitido para propósitos educativos, experimentales y no comerciales.

---

## 📬 Contacto

Para consultas, propuestas o colaboraciones:

📧 johanhurtaalt@gmail.com  
📧 enrriquezandres7@gmail.com

---

¡Gracias por utilizar nuestra aplicación de Grounding DINO! Esperamos que este proyecto te sea útil para aprender, explorar y construir nuevas ideas con visión y lenguaje.