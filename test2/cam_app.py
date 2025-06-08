import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale converter")
#create a file uploader component allowing the user to upload a file
upload_image = st.file_uploader("Upload Image")

with st.expander("Start Camera: "):
#start camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #create pillow image
    img = Image.open(camera_image)

    #convert the pillow image to grayscale
    gray_img = img.convert("L")

    #render the grayscale image on the webpage
    st.image(gray_img)

if upload_image:
    img = Image.open(upload_image)
    #convert to gray
    gray_upload_img = img.convert('L')
    #display the image
    st.image(gray_upload_img)