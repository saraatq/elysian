import streamlit as st
from PIL import Image

from apps.functions import show_histogram


def app():
    st.subheader("Show Image Histogram")
    image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        st.subheader("Image")
        # View Uploaded Image
        img = Image.open(image_file)
        st.image(img, width=450)

        # call the function
        st.subheader("Histogram")
        new_img = show_histogram(img)
        st.image(new_img, width=450)
