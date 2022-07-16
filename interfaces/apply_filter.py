import streamlit as st
from PIL import Image

from apps.functions import apply_filter


def app():
    st.subheader("laplacian Filter Tool")
    image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        st.subheader("Before")
        # View Uploaded Image
        img = Image.open(image_file)
        img.thumbnail((250, 250), Image.ANTIALIAS)
        st.image(img, width=400)

        # call the function
        st.subheader("After")
        new_img = apply_filter(img)
        st.image(new_img, width=400)
