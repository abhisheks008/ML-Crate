import os
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input


app = Flask(__name__)

def create_model(optimizer='adam'):
    model = Sequential()
    model.add(Input(shape=(X_resampled.shape[1],)))  # Assuming X_resampled.shape[1] is known
    model.add(Dense(128, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
    model.add(Dropout(0.5))
    model.add(Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
    model.add(Dense(5, activation='softmax'))
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# Load the trained model
with open('/Users/akshay/Desktop/ML-Crate/DataAnalyticsSalaryPrediction/Model/model1', 'rb') as file:
    model = pickle.load(file)

# Load the encoder and scaler
with open('/Users/akshay/Desktop/ML-Crate/DataAnalyticsSalaryPrediction/Model/encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('/Users/akshay/Desktop/ML-Crate/DataAnalyticsSalaryPrediction/Model/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Preprocessing function
def preprocess_input(data):
    df = pd.DataFrame(data, index=[0])
    df_encoded = encoder.transform(df)
    df_scaled = scaler.transform(df_encoded)
    return df_scaled

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = preprocess_input(data)
    prediction = model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
