import streamlit as st
from PIL import Image

from apps.functions import adjustment


def app():
    st.subheader("Brightness Adjustment Tool")
    image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        st.subheader("Before")
        # View Uploaded Image
        img = Image.open(image_file)
        st.image(img, width=500)
        # call the function
        st.subheader("After")
        new_img = adjustment(img)
        st.image(new_img, width=500)
