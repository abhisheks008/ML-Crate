# AirBus Ship Detection Web App

## 📝 Description
This folder contains the Streamlit web application for detecting ships in satellite images using a pre-trained UNet segmentation model. The app allows users to upload an image, and it performs ship segmentation, displaying the results.


https://github.com/tanuj437/ML-Crate/assets/128210429/3a1b2d6a-9bb6-40b9-a858-c089a1248b0f


## 📂 Contents
**app.py:** Streamlit application script for ship detection.
**README.md:** This document.
**RNS_model.pkl:** Pre-trained UNet segmentation model used in the application.

## 🎯 Goal
The goal of this AirBus Ship detection web app is to provide an interactive platform for users to upload satellite images and obtain ship segmentation results using a deep learning model.

## 🚀 How to Run the App
1. Install the required libraries:
    ```sh
    pip install streamlit torch torchvision pillow numpy
    ```

2. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

3. Open the provided local URL in your web browser to access the app.

## 🧠 How It Works
The app performs the following steps:
1. Loads the pre-trained UNet model using PyTorch.
2. Accepts image uploads from the user through the web interface.
3. Preprocesses the uploaded image (resizes and converts to tensor).
4. Performs inference using the model to generate a segmentation mask.
5. Displays the uploaded image and the corresponding segmentation mask.

## ✒️ Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
