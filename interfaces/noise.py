import streamlit as st
from PIL import Image

from apps.Band_reject_filter import band_filter


def app():
    uploaded = False
    st.subheader("Reduce Periodic Noise Tool")
    with st.form("my-form", clear_on_submit=True):
        image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Upload the dropped file!")
        test1 = st.form_submit_button("Upload colored TEST image!")
        test2 = st.form_submit_button("Upload gray TEST image!")

    if test1:
        uploaded = True
        img = Image.open("./imgs/Image_with_periodic_noise_color.jpeg")

    elif test2:
        uploaded = True
        img = Image.open("./imgs/Image_with_periodic_noise.jpg")

    elif submitted and image_file is not None:
        uploaded = True
        img = Image.open(image_file)

    if uploaded:
        # style
        col1, mid, col2 = st.columns([1, 30, 40])
        with col1:
            st.subheader("Before")
            # View Uploaded Image
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