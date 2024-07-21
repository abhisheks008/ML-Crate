import streamlit as st
import pandas as pd
import joblib

# Load the preprocessor and Ridge model
preprocessor = joblib.load('Model/preprocessor.pkl')
ridge_model = joblib.load('Model/ridgemodel.pkl')

# Load unique values for categorical columns
unique_values = joblib.load('Model/unique_values.pkl')

# Define input features
categorical_cols = ['brand', 'model', 'fuel_type', 'engine', 'transmission', 'ext_col', 'int_col', 'accident', 'clean_title']
numerical_cols = ['model_year', 'milage']

# Define the web app
st.title('Car Price Prediction App')

st.write("""
## Predict the price of a car based on its attributes
""")

# Input fields
inputs = {}
for col in numerical_cols:
    inputs[col] = st.number_input(f'Enter {col}', min_value=0)
for col in categorical_cols:
    options = unique_values[col]
    inputs[col] = st.selectbox(f'Select {col}', options=options)

# When the user clicks the Predict button
if st.button('Predict'):
    input_df = pd.DataFrame([inputs])
    
    # Apply the transformations to the input data
    input_transformed = preprocessor.transform(input_df)
    
    # Make a prediction
    prediction = ridge_model.predict(input_transformed)
    
    st.write(f'The predicted price of the car is: ${prediction[0]:,.2f}')
