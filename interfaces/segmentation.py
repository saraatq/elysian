import streamlit as st
from PIL import Image
from apps.img_segmentation import segment


def app():
    uploaded = False
    st.subheader("Image Segmentation Tool")
    with st.form("my-form", clear_on_submit=True):
        image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Upload the dropped file!")
        test = st.form_submit_button("upload TEST image!")

    if test:
        uploaded = True
        img = Image.open("./imgs/Image_to_be_segmented.jpg")

    elif submitted and image_file is not None:
        uploaded = True
        img = Image.open(image_file)

    if uploaded:
        st.subheader("Before")
        # View Uploaded Image
        img.thumbnail((300, 300), Image.ANTIALIAS)
        st.image(img, width=400)

        # call the function
        st.subheader("After")
        new_img = segment(img, 3)
        st.image(new_img, width=400)

