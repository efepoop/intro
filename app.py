

import streamlit as st
from PIL import Image

st.title("Los tralas")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('Valerina.png')

st.image(image, caption='interfaces multimodales')

texto = st.text_input("escribe algo", "este es mi texto")
st.write("el texto escrito es",texto)
