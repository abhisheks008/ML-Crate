import joblib
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the fitted scaler
scaler = joblib.load('Model/scaler.pkl')

# Load your trained model
model = joblib.load('Model/model.pkl')

# Function to preprocess and predict the response
def predict_response(gender, age, driving_license, region_code, previously_insured,
                     vehicle_age, vehicle_damage, annual_premium, policy_sales_channel, vintage):
    # Preprocess input data
    gender = 1 if gender == 'Male' else 0
    vehicle_age = {'< 1 Year': 1, '1-2 Year': 0, '> 2 Years': 2}[vehicle_age]
    vehicle_damage = 1 if vehicle_damage == 'Yes' else 0

    # Create a numpy array with the input data
    data = np.array([[gender, age, driving_license, region_code, previously_insured,
                      vehicle_age, vehicle_damage, annual_premium, policy_sales_channel, vintage]])

    # Transform the data using the loaded scaler
    data_scaled = scaler.transform(data)

    # Make predictions
    prediction = model.predict(data_scaled)[0]

    return prediction

def main():
    st.title('Insurance Response Prediction App')
    st.sidebar.title('Input Parameters')

    # Input fields
    gender = st.sidebar.radio('Gender', ['Male', 'Female'])
    age = st.sidebar.slider('Age', 20, 85, 40)
    driving_license = st.sidebar.selectbox('Driving License', [0, 1])
    region_code = st.sidebar.number_input('Region Code', min_value=0.0, max_value=52.0, value=25.0)
    previously_insured = st.sidebar.selectbox('Previously Insured', [0, 1])
    vehicle_age = st.sidebar.selectbox('Vehicle Age', ['< 1 Year', '1-2 Year', '> 2 Years'])
    vehicle_damage = st.sidebar.selectbox('Vehicle Damage', ['No', 'Yes'])
    annual_premium = st.sidebar.number_input('Annual Premium', min_value=2630.0, max_value=540165.0, value=2630.0)
    policy_sales_channel = st.sidebar.number_input('Policy Sales Channel', min_value=1, max_value=163, value=1)
    vintage = st.sidebar.slider('Vintage', 10, 299, 150)

    # Predict function
    if st.button("Predict"):
        prediction = predict_response(gender, age, driving_license, region_code, previously_insured, vehicle_age, vehicle_damage, annual_premium, policy_sales_channel, vintage)
        response = 'True' if prediction == 1 else 'False'
        st.success(f"The predicted response is: {response}")

if __name__ == '__main__':
    main()
