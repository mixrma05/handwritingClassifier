import streamlit as st
import numpy as np
import cv2
from preprocessImage import preprocessImage
from modelUtils import loadModel
from trainModel import trainModel


st.title("Handwritten Alphabet Classification (A-Z)")
st.write("Upload an image of your handwritten alphabet.")

# Load or Train model
model = loadModel()

if model is None:
    st.write("No trained model found. Training model now...")
    model = trainModel()
    st.success("Model trained successfully!")

# Upload image
uploadedFile = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploadedFile is not None:
    fileBytes = np.asarray(bytearray(uploadedFile.read()), dtype=np.uint8)
    image = cv2.imdecode(fileBytes, 1)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    features = preprocessImage(imageArray=image)
    features = features.reshape(1, -1)

    prediction = model.predict(features)

    st.success(f"Predicted Alphabet: {prediction[0]}")