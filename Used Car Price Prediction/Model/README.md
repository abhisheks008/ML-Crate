# Car Price Prediction - Model

## 📝 Description
This folder contains the pre-trained machine learning models and scripts used for predicting car prices based on various attributes. The aim is to accurately estimate the price of a car given its features.

## 📂 Contents
- **used-car-price-prediction.ipynb:** Jupyter Notebook containing the complete process of data preprocessing, model training, evaluation, and visualization.
- **README.md:** This document.
- **ridgemodel.pkl:** Pre-trained Ridge Regression model used for car price prediction.
- **preprocessor.pkl:** Pre-trained data preprocessor.
- **unique_values.pkl:** Precomputed unique values for categorical columns.

## 🎯 Goal
The goal of this car price prediction project is to accurately predict car prices using various machine learning models based on attributes such as brand, model, model year, mileage, fuel type, engine type, transmission type, exterior color, interior color, accident history, and title status.

## 🧮 What I Did
In this car price prediction project, various models were evaluated to find the most effective one for predicting car prices. The models evaluated include:

## Models Used
- **Linear Regression:** A basic linear approach to modeling the relationship between the dependent variable and one or more independent variables.
- **Ridge Regression:** A linear regression model with L2 regularization to prevent overfitting.
- **Lasso Regression:** A linear regression model with L1 regularization to perform feature selection.
- **Decision Tree:** A model that splits the data into subsets based on feature values, creating a tree-like structure for regression.
- **Gradient Boosting:** An ensemble learning method that builds models sequentially to correct errors of previous models.

- **K-Nearest Neighbors Regressor (KNN):** An instance-based learning algorithm that predicts a sample's value based on the average value of its k-nearest neighbors.
- **XGBoost Regressor:** An optimized gradient boosting library designed for speed and performance.

## Data Preprocessing and Augmentation
- **Image Resizing and Normalization:** Not applicable for this dataset.
- **Feature Engineering:** Applied standard scaling for numerical features and one-hot encoding for categorical features.
- **Data Splitting:** Divided data into training and test sets for robust model evaluation.

## 🚀 Models Implemented
- **Linear Regression:** Basic linear approach.
- **Ridge Regression:** Regularized linear regression.
- **Lasso Regression:** Regularized linear regression with feature selection.
- **Decision Tree:** Non-linear tree structure.
- **Gradient Boosting:** Sequential ensemble learning.
- **K-Nearest Neighbors Regressor (KNN):** Instance-based learning.
- **XGBoost Regressor:** Optimized gradient boosting.

## 📈 Performance of the Models
The models were evaluated using mean absolute error (MAE), mean squared error (MSE), root mean squared error (RMSE), and R-squared (R2) score. Detailed performance metrics for each model are included in the Jupyter Notebook.

<img width="146" alt="RMSE_cmp" src="https://github.com/user-attachments/assets/b80bd458-93d5-4108-a447-c9dfa7ef75ee">
<img width="150" alt="R2_cmp" src="https://github.com/user-attachments/assets/c9d3824f-6c49-437d-9a42-333206f30800">
<img width="139" alt="MSE_cmp" src="https://github.com/user-attachments/assets/e2dc0348-2baa-490b-be7a-09be09f15ffc">
<img width="154" alt="MAE_cmp" src="https://github.com/user-attachments/assets/aba3bab7-6000-4ec0-943f-7788d03d1efd">

## 📢 Conclusion
The car price prediction project demonstrates that various machine learning models can accurately estimate car prices based on their features. Ridge Regression was chosen as the final model for deployment in the web app.

## ✒️ Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
