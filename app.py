import streamlit as st
import tensorflow as tf

# Define your custom hash function
def my_hash_func(func):
    # Implement your custom hash logic here
    return hash(func)

def load_model():
    model = tf.keras.models.load_model('/content/model.hdf5')
    return model

model = load_model()

st.write("""
# Weather detection
""")

file = st.file_uploader("Choose weather photo from computer", type=["jpg", "png"])

import cv2
from PIL import Image, ImageOps
import numpy as np

def import_and_predict(image_data, model):
    size = (64, 64)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis, ...]
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    class_names = ['Cloudy', 'Rain', 'Shine', 'Sunrise']
    string = "OUTPUT : " + class_names[np.argmax(prediction)]
    st.success(string)
