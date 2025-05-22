import streamlit as st
import plotly.graph_objects as go

st.header("🧠 Arquitectura del Modelo")

st.markdown("""
Grounding DINO usa dos ramas basadas en **Transformers**:
- Una para la imagen (Visual Backbone: Swin Transformer)
- Otra para el texto (Text Encoder: BERT)

Ambos flujos se integran en un **Cross-Modality Transformer** que alinea el lenguaje con las regiones visuales.

La predicción final se hace mediante **Object Queries**, igual que en DETR.
""")

fig = go.Figure(data=[
    go.Sankey(
        node=dict(
            label=["Imagen", "Texto", "Backbone Visual", "Encoder de Texto", "Cross Attention", "Bounding Boxes"],
            pad=20, thickness=20,
        ),
        link=dict(
            source=[0, 1, 2, 3, 4],
            target=[2, 3, 4, 4, 5],
            value=[1, 1, 1, 1, 1]
        )
    )
])
st.plotly_chart(fig)
