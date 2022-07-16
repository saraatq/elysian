import streamlit as st
from PIL import Image

from apps.functions import show_histogram


def app():
    uploaded = False
    st.subheader("Show Image Histogram")
    with st.form("my-form", clear_on_submit=True):
        image_file = st.file_uploader("", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Upload the dropped file!")
        test1 = st.form_submit_button("Upload colored TEST image!")
        test2 = st.form_submit_button("Upload gray TEST image!")

    if test1:
        uploaded = True
        img = Image.open("./imgs/Image_to_be_segmented.jpg")

    elif test2:
        uploaded = True
        img = Image.open("./imgs/Image_before_equalization.jpg")

    elif submitted and image_file is not None:
        uploaded = True
        img = Image.open(image_file)

    if uploaded:
        st.subheader("Image")
        # View Uploaded Image
        st.image(img, width=450)

        # call the function
        st.subheader("Histogram")
        new_img = show_histogram(img)
        st.image(new_img, width=450)
