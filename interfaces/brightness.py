import streamlit as st
from PIL import Image

from apps.functions import adjustment


def app():
    uploaded = False
    st.subheader("Brightness Adjustment Tool")
    with st.form("my-form", clear_on_submit=True):
        number = st.slider('choose your value', min_value=-5, max_value=5, value=0, step=1)
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
        st.image(img, width=500)
        # call the function
        st.subheader("After")

        # if the user didn't choose a value the img doesn't change
        if number == 0:
            number = 1

        new_img = adjustment(img, number)
        st.image(new_img, width=500)
        st.markdown('***you can change the value and upload any photo again.***')
