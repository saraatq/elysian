import streamlit as st
from PIL import Image
from apps.img_segmentation import segment


def app():
    st.subheader("Image Segmentation Tool")
    image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        st.subheader("Before")
        # View Uploaded Image
        img = Image.open(image_file)
        img.thumbnail((300, 300), Image.ANTIALIAS)
        st.image(img, width=400)

        # call the function
        st.subheader("After")
        new_img = segment(img, 3)
        st.image(new_img, width=400)

