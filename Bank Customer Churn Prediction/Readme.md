# Bank Customer Churn Prediction Model

## Overview
This repository contains code for a machine learning model that predicts customer churn for a bank. Customer churn refers to the phenomenon where customers stop doing business with a company. In the context of a bank, it means customers closing their accounts or ceasing to use banking services.

The model is built using [Python](https://www.python.org/) and popular machine learning libraries such as [scikit-learn](https://scikit-learn.org/) and classification algorithms like Logistic regression , Random forest , Decision tree , Gradient boosting and ADAboost . It leverages historical customer data to predict the likelihood of a customer churning in the future.

## Dataset

The model is trained on a dataset containing historical information about bank customers. The dataset includes various features such as customer demographics, transaction history, account balances, etc. Each entry in the dataset is labeled with whether the customer churned or not.

### Features

1. **id**: A unique identifier for each record.
2. **CustomerId**: A unique identifier for each customer.
3. **Surname**: The surname of the customer.
4. **CreditScore**: The credit score of the customer, which indicates their creditworthiness.
5. **Geography**: The geographical location of the customer.
6. **Gender**: The gender of the customer.
7. **Age**: The age of the customer.
8. **Tenure**: The number of years the customer has been with the bank.
9. **Balance**: The account balance of the customer.
10. **NumOfProducts**: The number of bank products the customer uses.
11. **HasCrCard**: Whether the customer has a credit card (1 if yes, 0 if no).
12. **IsActiveMember**: Whether the customer is an active member of the bank (1 if yes, 0 if no).
13. **EstimatedSalary**: The estimated salary of the customer.
14. **Exited**: Whether the customer has churned (1 if yes, 0 if no).

This dataset can be used to train machine learning models to predict customer churn based on the provided features. The goal is to build a model that can accurately identify customers who are likely to churn, allowing the bank to take proactive measures to retain them.

## Visualizations 
Here are some visualizations generated from the dataset:

![Visualization 1](images/visualization1.png)
*Description of Visualization 1*

![Visualization 2](images/visualization2.png)
*Description of Visualization 2*

## Model
The model is a binary classification model that predicts whether a customer will churn or not. It is trained using supervised learning techniques on the provided dataset. The performance of the model is evaluated using appropriate metrics such as accuracy, precision, recall, and F1-score.

## Usage
To use the model, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the provided Jupyter notebook or Python script to train the model on your dataset.
4. Once trained, you can use the model to make predictions on new data by providing the relevant features as input.

## Evaluation
The model's performance can be evaluated using various metrics such as accuracy, precision, recall, and F1-score. Additionally, you can visualize the model's performance using techniques such as confusion matrices and ROC curves.

## Contributors
- [Your Name](https://github.com/yourusername) - Role/Contribution

## License
This project is licensed under the [MIT License](LICENSE).
