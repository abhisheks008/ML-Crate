# Health Insurance Cross Sell Prediction-Model

## 📝 Description
This folder contains the pre-trained machine learning models and scripts used for predicting whether a customer will buy a vehicle insurance policy. The goal is to automatically categorize customers based on the likelihood of purchasing the insurance, helping to target potential buyers effectively.

## 📂 Contents
- Health_Insurance_Cross_Sell_Prediction.ipynb: Jupyter Notebook containing the complete process of data preprocessing, model training, evaluation, and visualization.
- model.pkl: Pre-trained model used for prediction.
- scaler.pkl: Pre-Fitted Scaler for data fitting.
- README.md: This document.

## 🎯 Goal
The goal of this prediction project is to enhance understanding of customer behavior by organizing and analyzing data on various features. By automatically classifying customers based on their likelihood of purchasing insurance, the project aims to provide insights into potential buyers and improve targeting strategies.

## 🧮 What I Did
In this prediction project, various models were evaluated to find the most effective one for classifying customers. The models evaluated include:

- Logistic Regression
```
Description: A linear model used for binary classification. It estimates probabilities using a logistic function.
Performance: Achieved an accuracy of 88%.
```

- XGBoost
```
Description: An implementation of gradient boosted decision trees designed for speed and performance.
Performance: Achieved an accuracy of 88%.
```

- Naive Bayes
```
Description: A probabilistic classifier based on Bayes' theorem with strong independence assumptions.
Performance: Achieved an accuracy of 64%.
```
- LightGBM
```
Description: A Light Gradient Boosting Machine (LightGBM) was trained for high performance and efficiency with large datasets.
Performance: Achieved an accuracy of 88%.
```
- Neural Network
```
Description: A basic feedforward neural network used for classification tasks.
Performance: Achieved an accuracy of 88%.
```
- Ridge Classifier
```
Description: A linear classifier with L2 regularization to avoid overfitting.
Performance: Achieved an accuracy of 88%.
```
- Stochastic Gradient Descent (SGD) Classifier
```
Description: A linear classifier optimized using stochastic gradient descent.
Performance: Achieved an accuracy of 88%.
```

## Data Preprocessing and Feature Engineering
- Data Cleaning: Normalized data, removed missing values, and handled duplicates.
- Feature Engineering: Created new features such as interaction terms, and performed encoding for categorical variables.
- Data Scaling: Standardized numerical features to ensure consistent scaling.


## Model Performance Analysis
- Training and Validation: Evaluated models based on accuracy, precision, recall, and F1 score to select the best-performing model.
Best Model
- The best-performing model, LightGBM, has been saved as model.pkl and is ready for deployment.

## 📈 Performance of the Models Based on Accuracy Scores
- Logistic Regression: Accuracy: 88%
- XGBoost: Accuracy: 88%
- Naive Bayes: Accuracy: 64%
- LightGBM: Accuracy: 88%
- Neural Network: Accuracy: 88%
- Ridge Classifier: Accuracy: 88%
- SGD Classifier: Accuracy: 88%

## 📢 Conclusion
The Health Insurance Cross Sell Prediction project demonstrates the effectiveness of machine learning models, particularly LightGBM, in accurately predicting customer behavior. The models help in organizing and prioritizing customer data, providing valuable insights for stakeholders.

## ✒️ Your Signature
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)