# Web App

## Overview
This folder contains the web application built to deploy the best model from the ` Fast Tag Fraud Detection project` .


## Contents
This folder contains the files for the web application built with Streamlit.

- **File**: `app.py`
  - Streamlit application script for real-time fraud detection.
  
- **File**: `SVM_Fast_best.pkl`
  - Serialized model file used for predictions in the app.

- **File**: `demo.mp4`
  - A demo video showing the usage of the web application.

- **File**: `readme.md`
  - This readme file.

## Instructions
1. Make sure to have Streamlit installed.
2. Run `streamlit run app.py` to start the Streamlit web application.
3. Open your web browser and navigate to `http://localhost:8501` to access the application.

- **Usage**:
  To run the app, use the following command:
  ```bash
  streamlit run app.py
    ```
    The application will open in your default web browser.
  - **Prediction**:
    - Enter the required information such as the Transaction Amount, Amount Paid, Geographical Location, etc.
    - Click the "Predict" button to see the prediction.
    - The application will display the prediction based on the input provided.

## Demo
Check out the demo video to see the web application in action.

- [Demo Video](https://github.com/abhisheks008/ML-Crate/assets/128123681/3b3ed39a-7963-4315-97ff-f38b3e785d9d)

[demo.webm](https://github.com/abhisheks008/ML-Crate/assets/128123681/3b3ed39a-7963-4315-97ff-f38b3e785d9d)

