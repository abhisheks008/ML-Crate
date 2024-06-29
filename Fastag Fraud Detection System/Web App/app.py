import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('SVM_Fast_best.pkl', 'rb') as f:
    model = pickle.load(f)

# Define feature columns
features = ['Transaction_Amount', 'Amount_paid', 'Vehicle_Type', 'TollBoothID',
            'Lane_Type', 'Vehicle_Dimensions', 'Geographical_Location',
            'Month', 'Week']

# Streamlit app
st.title('Fastag Fraud Detection System')

st.write("""
# Detecting Fraudulent Transactions
Fill in the details of the transaction to predict if it's fraudulent.
""")

# Get user input
transaction_amount = st.number_input('Transaction Amount', min_value=0.0, format="%.2f")
amount_paid = st.number_input('Amount Paid', min_value=0.0, format="%.2f")
vehicle_type = st.selectbox('Vehicle Type', ['Bus ','Car' ,'Truck', 'Van' ,'Sedan' ,'SUV' ,'Motorcycle'])
tollbooth_id = st.text_input('TollBooth ID')
lane_type = st.selectbox('Lane Type', ['Regular', 'Express'])
vehicle_dimensions = st.selectbox('Vehicle Dimensions', ['Small', 'Medium', 'Large'])
geographical_location = st.text_input('Geographical Location')
month = st.number_input('Month', min_value=1, max_value=12)
week = st.number_input('Week', min_value=1, max_value=52)

# Create input data frame
input_data = pd.DataFrame([[transaction_amount, amount_paid, vehicle_type, tollbooth_id,
                            lane_type, vehicle_dimensions, geographical_location,
                            month, week]], columns=features)

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'
    st.write(f'The transaction is predicted to be: {result}')
