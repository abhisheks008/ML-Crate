
## [Feature Addition]: Web App for Vehicle Live Risk Prediction #602
![Visual Overview](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzdqZjlmZXZnODI0YTJyd2NmNGdkZmRndnk0MDY0ZjN1MDNjZmYxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gKBRsM4xJJS2GhAQij/giphy-downsized-large.gif)

### Overview
The Vehicle Risk Prediction application is designed to predict the risk associated with driving a vehicle based on various factors such as weather conditions, road hazards, visibility, traffic density, and driver-related factors like fatigue level, speeding, and medical conditions. The application utilizes a machine learning model trained on historical data to provide risk predictions.

![Alt Text](/Users/shivanshmahajan/Desktop/ML-Crate/Vehicle Live Risk Prediction/Images/mainmodel.png)
![Alt Text](/Users/shivanshmahajan/Desktop/ML-Crate/Vehicle Live Risk Prediction/Images/about.png)

### Goal 🎯
'The aim is to create a web app for the Vehicle Live Risk Prediction project. Use the best existing model in the project folder. Follow the Web App README template for the same.'


### Functionality
#### Main Model Page:
- **Input Fields:** Users can enter details such as Visibility, Road Surface Conditions, Weather, Traffic Density, Road Hazards, Fatigue Level, Medical Condition, Speeding, and Light Condition.
- **Prediction:** After entering the required information and clicking on the "Predict Risk" button, the application calculates the risk level (High Risk or Low Risk) based on the user's input.

#### Visualization Page:
- **Data Overview:** Displays the first few rows of the dataset and provides an overview of the data.
- **Data Statistics:** Shows summary statistics of numerical columns in the dataset.
- **Correlation Heatmap:** Visualizes the correlation between numerical features using a heatmap.
- **Countplots of Categorical Features:** Displays count plots for each categorical feature in the dataset.


#### About Page:
- **Model Explanation (XGBoost):** Provides an explanation of the machine learning model used in the application, focusing on the XGBoost (Extreme Gradient Boosting) algorithm.
- **Purpose:** Explains the purpose and goal of the Vehicle Risk Prediction application.

## Technology Stack
The Vehicle Risk Prediction application is built using the following technologies:
- **Streamlit:** Used for building the user interface and web application.
- **Pandas:** Used for data manipulation and handling input data.
- **Joblib:** Used for loading the machine learning model, encoders, and scaler.
- **XGBoost:** Machine learning algorithm used for risk prediction.

## How to Use
1. **Navigation:** Use the sidebar to navigate between the Main Model Page, Visualization Page, and About Page.
2. **Main Model Page:**
   - Fill in all required fields with relevant information.
   - Click on the "Predict Risk" button to see the risk prediction.
3. **Visualization Page:**
   - Explore data overview, statistics, correlations, countplots, and pairplots to gain insights into the dataset.
4. **About Page:**
   - Provides information about the model explanation and purpose of the application.

### Video Demonstration 🎥
[Watch the video](https://vimeo.com/953208773?share=copy)

### Signature ✒️

Name:-Shivansh Mahajan

Github:-https://github.com/shivansh-2003

Linkedin:-https://www.linkedin.com/in/shivansh-mahajan-13227824a/
