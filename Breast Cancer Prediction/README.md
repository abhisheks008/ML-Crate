
# Breast Cancer Predictor

## Website


## Overview
This Streamlit app assists medical professionals in diagnosing breast cancer from tissue samples. It predicts whether a breast mass is benign or malignant based on measurements received from a cytology lab. Users can interact with the app by adjusting the measurements using sliders in the sidebar.

## Features
- **Interactive Sidebar**: Allows users to adjust cell nuclei measurements using sliders for various features.
- **Predictions**: Provides predictions on whether the cell cluster is benign or malignant, along with the probability of each prediction.
- **Radar Chart Visualization**: Displays radar charts showing the distribution of features for mean, standard error, and worst values.
- **Professional Diagnosis Disclaimer**: Reminds users that the app is for assistance only and should not replace professional medical diagnosis.

## Installation
1. Clone the repository: `git clone repository-url`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app/main.py`

## Usage
1. Adjust the sliders in the sidebar to update the cell nuclei measurements.
2. View the radar chart to visualize the distribution of features.
3. Check the predictions to see whether the cell cluster is predicted as benign or malignant.
4. Note the probabilities associated with each prediction.
5. Use the app as a tool to assist in making a diagnosis but always consult a professional for medical advice.

## File Structure
- `app/main.py`: Main script containing the Streamlit app.
- `data/data.csv`: CSV file containing the dataset with cell nuclei measurements.
- `model/model.pkl`: Pickle file containing the trained machine learning model.
- `model/scaler.pkl`: Pickle file containing the scaler used for feature scaling.
- `assets/style.css`: CSS file for custom styling.
- `README.md`: README file with project information.

## Requirements
- Python 3.x
- Streamlit
- Pandas
- Plotly
- NumPy
- Pickle
  



