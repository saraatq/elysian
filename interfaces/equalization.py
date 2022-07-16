import streamlit as st
from PIL import Image
from apps.histogram_equalization import histogram_equalization


def app():
    uploaded = False
    st.subheader("Histogram Equalization Tool")
    with st.form("my-form", clear_on_submit=True):
        image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Upload the dropped file!")
        test = st.form_submit_button("upload TEST image!")

    if test:
        uploaded = True
        img = Image.open("./imgs/Image_before_equalization.jpg")

    elif submitted and image_file is not None:
        uploaded = True
        img = Image.open(image_file)

    if uploaded:
        col1, mid, col2 = st.columns([1, 30, 40])
        with col1:
            st.subheader("Before")
            # View Uploaded Image
            st.image(img, width=250)

        # call the function
        with col2:
            st.subheader("After")
            new_img = histogram_equalization(img)
            st.image(new_img, width=250)
