import streamlit as st
from PIL import Image

from apps.Band_reject_filter import band_filter


def app():
    st.subheader("Reduce Periodic Noise Tool")
    image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        # style
        col1, mid, col2 = st.columns([1, 30, 40])
        with col1:
            st.subheader("Before")
            # View Uploaded Image
            img = Image.open(image_file)
            st.image(img, width=250)

        # call the function
        lis = band_filter(img)

        with col2:
            st.subheader("After")
            new_img = lis[1]
            st.image(new_img, width=250)

        st.subheader("Band Reject Filter")
        filterIMG = lis[0]
        st.image(filterIMG, width=420)