import streamlit as st
import pandas as pd
import joblib
import logging
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the model, encoders, and scaler
with open('/Users/shivanshmahajan/Desktop/Vechile Live Risk Prediction/Model/vehicle_risk_model.pkl', 'rb') as f:
    model, encoders, scaler = joblib.load(f)

logging.info("Loaded model, encoders, and scaler.")

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Main Model Page", "About", "Visualization"])

if page == "Main Model Page":
    st.title('Vehicle Risk Prediction')

    st.header('Enter the following details:')

    st.image('/Users/shivanshmahajan/Desktop/ML-Crate/Vehicle Live Risk Prediction/Images/covid19-risk-assessment-automobile-manufacturers.jpg')

    # Create input fields for the user to enter new data
    visibility = st.selectbox('Visibility', encoders['Visibility'].classes_)
    road_surface_conditions = st.selectbox('Road Surface Conditions', encoders['Road_Surface_Conditions'].classes_)
    weather = st.selectbox('Weather', encoders['Weather'].classes_)
    traffic_density = st.selectbox('Traffic Density', encoders['Traffic_Density'].classes_)
    road_hazards = st.selectbox('Road Hazards', encoders['Road_Hazards'].classes_)
    fatigue_level = st.selectbox('Fatigue Level', encoders['Fatigue_Level'].classes_)
    medical_condition = st.selectbox('Medical Condition', encoders['Medical_Condition'].classes_)
    speeding = st.selectbox('Speeding', encoders['Speeding'].classes_)
    light_condition = st.selectbox('Light Condition', encoders['Light_Conditions'].classes_)

    logging.info("User inputs received.")

    # Encode user inputs
    user_data = {
        'Visibility_n': encoders['Visibility'].transform([visibility])[0],
        'Road_Surface_Conditions_n': encoders['Road_Surface_Conditions'].transform([road_surface_conditions])[0],
        'Weather_n': encoders['Weather'].transform([weather])[0],
        'Traffic_Density_n': encoders['Traffic_Density'].transform([traffic_density])[0],
        'Road_Hazards_n': encoders['Road_Hazards'].transform([road_hazards])[0],
        'Fatigue_Level_n': encoders['Fatigue_Level'].transform([fatigue_level])[0],
        'Medical_Condition_n': encoders['Medical_Condition'].transform([medical_condition])[0],
        'Speeding_n': encoders['Speeding'].transform([speeding])[0],
        'Light_Conditions_n': encoders['Light_Conditions'].transform([light_condition])[0]
    }

    # Convert to DataFrame
    user_df = pd.DataFrame([user_data])
    logging.info("Dataframe created.")

    # Standardize user input
    user_df_scaled = scaler.transform(user_df)
    logging.info("User data standardized.")

    # Make prediction
    if st.button('Predict Risk'):
        logging.info("Prediction button clicked.")
        prediction = model.predict(user_df_scaled)
        risk = 'High Risk' if prediction[0] == 1 else 'Low Risk'

        if risk == 'High Risk':
            st.markdown(
                "<h2 style='color: red;'>The predicted risk is: HIGH RISK 🚨</h2>",
                unsafe_allow_html=True
            )
            st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjA2ZHhtNDBheTN2azd6bmVoazc4OHE0ZW1iNTQxMzl2bnprb2JucSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qQ7QkOrNraxbJcS6Nc/giphy.gif")

        else:
            st.markdown(
                "<h2 style='color: green;'>The predicted risk is: LOW RISK ✅</h2>",
                unsafe_allow_html=True
            )
            st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjViYXA3NTYwdWYzcTI5NTFvZmpjdWM4NHlpNTVheWh2NHkwY3A2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/j9E6whHPamxa5KpDQt/giphy.gif")

        logging.info("Prediction made and displayed.")
elif page == "Visualization":
    df = pd.read_csv("/Users/shivanshmahajan/Desktop/Vechile Live Risk Prediction/Data/Vehicle Risk Prediction Dataset.csv")  # Load the dataset within the Visualization page

    st.title("Exploratory Data Analysis")

    st.header("Data Overview")
    st.write(df.head())  # Display the first few rows of the dataset

    st.header("Data Statistics")
    st.write(df.describe())  # Display summary statistics of numerical columns

    st.header("Correlation Heatmap")
    numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    st.pyplot()
    st.header("Countplots of Categorical Features")
    categorical_features = ['Visibility', 'Road_Surface_Conditions', 'Weather', 'Traffic_Density', 'Road_Hazards',
                            'Fatigue_Level', 'Medical_Condition', 'Speeding', 'Light_Conditions']
    for feature in categorical_features:
        plt.figure(figsize=(8, 6))
        sns.countplot(x=feature, data=df)
        plt.title(f"Countplot of {feature}")
        st.pyplot()

else:
    st.title("About Vehicle Risk Prediction")
    st.image("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGZiejl6cG96ZTVzN2NxcGc0d2prbmJvam45MWMzaTg3aWF4bzVmMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKDa4TeqnpmXc6Q/giphy.gif")
    st.write("The Vehicle Risk Prediction application is designed to predict the risk associated with driving a vehicle "
             "based on various factors such as weather conditions, road hazards, visibility, traffic density, and "
             "driver-related factors like fatigue level, speeding, and medical conditions. The application utilizes a "
             "machine learning model trained on historical data to provide risk predictions.")

    st.subheader("Functionality")
    st.markdown("""
    **Main Model Page:**
    - **Input Fields:** Users can enter details such as Visibility, Road Surface Conditions, Weather, Traffic Density, 
    Road Hazards, Fatigue Level, Medical Condition, Speeding, and Light Condition.
    - **Prediction:** After entering the required information and clicking on the "Predict Risk" button, the application 
    calculates the risk level (High Risk or Low Risk) based on the user's input.
    
    **About Page:**
    - **Model Explanation:** Provides an explanation of the machine learning model used in the application, focusing on 
    the XGBoost (Extreme Gradient Boosting) algorithm.
    - **Purpose:** Explains the purpose and goal of the Vehicle Risk Prediction application.
    """)

    st.subheader("Technology Stack")
    st.markdown("""
    - **Streamlit:** Used for building the user interface and web application.
    - **Pandas:** Used for data manipulation and handling input data.
    - **Joblib:** Used for loading the machine learning model, encoders, and scaler.
    - **XGBoost:** Machine learning algorithm used for risk prediction.
    """)

    st.subheader("How to Use")
    st.markdown("""
    1. **Navigation:** Use the sidebar to navigate between the Main Model Page and the About Page.
    2. **Main Model Page:**
       - Fill in all required fields with relevant information.
       - Click on the "Predict Risk" button to see the risk prediction.
    3. **About Page:**
       - Provides information about the model explanation and purpose of the application.
    """)

    st.subheader("Model Explanation (XGBoost)")
    st.markdown("""
    XGBoost (Extreme Gradient Boosting) is a powerful machine learning algorithm known for its high performance in 
    predictive modeling tasks. It combines the predictions from multiple weak models (typically decision trees) to 
    create a strong ensemble model. Here's a brief overview of how XGBoost works:
    - Boosting Technique: Each new model in the ensemble corrects errors made by previous models, improving overall 
    prediction accuracy.
    - Gradient Boosting: XGBoost optimizes a cost function using gradient descent, adjusting model parameters to minimize 
    prediction errors.
    - Regularization: Includes regularization techniques like L1 and L2 regularization to prevent overfitting and improve 
    model generalization.
    - Parallel Processing: XGBoost is designed for efficiency, leveraging parallel processing capabilities for fast 
    computation on large datasets.
    """)
