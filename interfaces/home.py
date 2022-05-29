import streamlit as st
from PIL import Image


def app():
    logo = "imgs/logo.png"

    # logo with text
    image = Image.open(logo)
    col1, mid, col2 = st.columns([1, 6, 20])
    with col1:
        st.image(image, width=150)
    with col2:
        st.title("Photo Tools")


"""" 
sdgsgd
    "Image Segmentation Tool"

app.add_app("Reduce Periodic Noise Tool", noise.app)
app.add_app("Histogram Equalization Tool", equalization.app)
app.add_app("Filter Tool", apply_filter.app)
app.add_app("Show Image Histogram", histogram.app)
app.add_app("Brightness Adjustment Tool", brightness.app)
"""


