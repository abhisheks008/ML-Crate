from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline
model = joblib.load('salary_prediction_pipeline_lr.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()

    # Convert form data to DataFrame
    df = pd.DataFrame([data])

    # Preprocess and predict
    prediction = model.predict(df)

    return render_template('index.html', prediction_text=f'Predicted Salary: {prediction[0]:,.2f}')


if __name__ == '__main__':
    app.run(debug=True)
