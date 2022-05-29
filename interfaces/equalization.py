import streamlit as st
from PIL import Image
from apps.histogram_equalization import histogram_equalization


def app():
    st.subheader("Histogram Equalization Tool")
    image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        col1, mid, col2 = st.columns([1, 30, 40])
        with col1:
            st.subheader("Before")
            # View Uploaded Image
            img = Image.open(image_file)
            st.image(img, width=250)

        # call the function
        with col2:
            st.subheader("After")
            new_img = histogram_equalization(img)
            st.image(new_img, width=250)
