# Web App

## Overview
This folder contains the web application built to deploy the best model from the Salary Prediction of Data Professionals project.

## Contents
- `templates/`: HTML templates used for rendering web pages.
- `static/`: Static files such as CSS and JavaScript for styling the web application.
- `app.py`: The main Flask application file that serves the predictive model and handles HTTP requests.
- `salary_prediction_pipeline_lr.pkl`: The serialized machine learning pipeline for salary prediction.
- `best_salary_model.sav`: The best-performing machine learning model.
- `demo.mp4`: A demo video showing the usage of the web application.
- `README.md`: This readme file.

## Instructions
1. Make sure to have Flask installed.
2. Run `python app.py` to start the Flask web application.
3. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage
- Enter the required information such as job role, experience, age, and ratings.
- Click the "Predict" button to see the predicted salary.
- The application will display the predicted salary based on the input provided.


<video controls src="demo.mp4" title="Title"></video>