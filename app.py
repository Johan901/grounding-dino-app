import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Grounding DINO App", layout="wide", page_icon="🦕")

st.markdown(
    """
    <style>
        .main {background-color: #F0F2F6;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🦕 Grounding DINO: Marrying DINO with Grounded Pre-Training")
st.write("Bienvenido a la plataforma interactiva de visual grounding.")
