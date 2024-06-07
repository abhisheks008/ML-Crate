---
noteId: "5336f36024b711ef81150b8fd372c2c7"
tags: []

---

# Live Vehicle Risk Detection using XGBoost Model

This project aims to predict vehicle risk scores using various environmental and driver-related factors. The model is trained using an XGBoost classifier and is capable of making real-time risk predictions based on the input data.

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Usage](#usage)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Saving the Model](#saving-the-model)

## Project Description

The Live Vehicle Risk Detection project utilizes machine learning to predict the risk associated with a vehicle's current conditions. The model considers factors such as visibility, road surface conditions, weather, traffic density, road hazards, driver fatigue level, medical conditions, speeding, and light conditions to determine a risk score. The XGBoost model categorizes the risk as high or low based on a threshold value.

## Dataset

https://www.kaggle.com/datasets/punyamodi/vehicle-live-risk-prediction



## Usage

To use the vehicle risk detection model, follow these steps:

1. **Prepare the Dataset**:
   Ensure the dataset is named `Vehicle Risk Prediction Dataset.csv` and placed in the project directory.
 
2. Make Predictions:
Once the model is trained, you can use the saved model to make predictions on new data. Load the model, encoders, and scaler from the vehicle_risk_model.pkl file and use them to transform and predict new data inputs. 

## Model Training
### The training process involves several steps:

Load the Dataset:
The dataset is loaded from a CSV file using pandas.

Encode Categorical Features:
Categorical features are encoded using LabelEncoder to convert them into numerical values that can be used by the model.

Define Features and Target:
The features (X) include various environmental and driver-related factors. The target (y) is a binary classification based on the risk score (1 if the risk score is above 50, otherwise 0).

Split the Data:
The dataset is split into training and testing sets using train_test_split.

Standardize Features:
Feature values are standardized using StandardScaler to have a mean of 0 and a standard deviation of 1.

Train the Model:
An XGBoost classifier is created and trained on the scaled training data.


## Evaluation
After training the model, its performance is evaluated on the test set:

Make Predictions:
The model makes predictions on the scaled test data.

Calculate Accuracy:
The accuracy of the model is computed to determine how well the model predicts the correct class.

Classification Report:
A detailed classification report is generated, which includes precision, recall, and F1 scores for both classes (high risk and low risk).

## Saving the Model
After training and evaluating the model, the following components are saved to a single file named vehicle_risk_model.pkl using joblib:

## Model used in this Project
1) Decision Tree 
2) Random Forest
3) ANN 
4) Multivariate Logisitic Regression
5) Lasso
6) Gradient Boost
7) Ridge
8) MLP
9) XGBoost

### Models and Accuracies

| Model                         | Accuracy   | MSE SCORE          |
| ----------------------------- |:----------:| ------------------:|
| Decision Tree                 | 0.9996     |                    |
| Random Forest                 | 1.0        |                    |
| ANN                           | 1.0        |                    |
| Logistic Regression           | 1.0        |                    |
| Lasso                         | N.A        | 0.03247239784420999|
| Gradient Boost                | 1.0        |                    |
| Ridge                         | N.A        | 0.007214250517408194|
| MLP                           | 0.9997     |                    |
| XGBoost                       | 1.0        |                    |
