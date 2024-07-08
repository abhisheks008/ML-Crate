import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from PIL import Image
from pathlib import Path

# Define the paths
MODEL_PATH ='Webapp/mineral_classification_model.pkl'  
IMAGE_PATH = Path("Dataset/img")  
if not IMAGE_PATH.exists():
    st.error(f"Image directory does not exist: {IMAGE_PATH}")

# Load class names dynamically
class_names = sorted([d.name for d in IMAGE_PATH.iterdir() if d.is_dir()])

# Load the trained model
with open(MODEL_PATH, 'rb') as file:
    lr_model = pickle.load(file)

# Define the image transformations
def preprocess_image(image):
    image = image.resize((224, 224)).convert('RGB')
    image_array = np.array(image)
    image_array = image_array / 255.0
    return image_array.reshape(1, -1)

# Streamlit app
st.title('Mineral Classification Web App')

st.write("""
         Upload an image of a mineral and the model will predict its class.
         """)

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    image_array = preprocess_image(image)

    # Make prediction
    prediction = lr_model.predict(image_array)
    predicted_class = class_names[prediction[0]]

    # Display the result
    st.write(f"Predicted Class: {predicted_class}")
