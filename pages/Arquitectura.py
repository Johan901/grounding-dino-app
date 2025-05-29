# Importamos las librerías necesarias
import streamlit as st
import plotly.graph_objects as go  # Usamos Plotly para crear un diagrama tipo Sankey

# Mostramos el encabezado de la sección
st.header("🧠 Arquitectura del Modelo")

# Explicamos cómo está estructurada la arquitectura de Grounding DINO
st.markdown("""
Grounding DINO usa dos ramas basadas en **Transformers**:
- Una para la imagen (Visual Backbone: Swin Transformer)
- Otra para el texto (Text Encoder: BERT)

Ambos flujos se integran en un **Cross-Modality Transformer** que alinea el lenguaje con las regiones visuales.

La predicción final se hace mediante **Object Queries**, igual que en DETR.
""")

# Creamos un diagrama Sankey para representar visualmente el flujo de la arquitectura
fig = go.Figure(data=[
    go.Sankey(
        node=dict(
            label=[
                "Imagen",               # Entrada visual
                "Texto",                # Entrada textual
                "Backbone Visual",      # Swin Transformer
                "Encoder de Texto",     # BERT
                "Cross Attention",      # Atención cruzada
                "Bounding Boxes"        # Resultado: cajas delimitadoras
            ],
            pad=20,  # Separación entre nodos
            thickness=20  # Grosor de los bloques
        ),
        link=dict(
            source=[0, 1, 2, 3, 4],  # Conexiones: de dónde parte
            target=[2, 3, 4, 4, 5],  # Conexiones: a dónde va
            value=[1, 1, 1, 1, 1]    # Peso de cada conexión
        )
    )
])

# Mostramos el gráfico interactivo en Streamlit
st.plotly_chart(fig)
