import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    return requests.get(url).json()

lottie = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json")  # animación Lottie

st.title("👋 Bienvenido")
st.write("Esta app permite explorar Grounding DINO para grounding visual basado en texto.")

st_lottie(lottie, height=300)
