# E-commerce Product Sales Prediction

# Models

## Table of Contents

```
* Goal 
* Dataset 
* Description 
* Libraries 
* Models and Results 
* Conclusion
```
## Goal

#### To predict sales of e-commerce products using various machine learning models.

## Dataset

#### Link: The dataset is provided within the notebook and contains various e-commerce product details.

## Description

#### * This folder contains the code and resources for predicting sales of e-commerce products using various machine learning models.

#### * The prediction is based on product details such as product name, category, price, rating, number of reviews, stock quantity, discount, and sales.

## Libraries Needed

#### * pandas

#### * numpy

#### * matplotlib

#### * seaborn

#### * plotly

#### * scikit-learn

## Models and Results

#### The project explores the following machine learning models to predict sales:

## 1. Linear Regression

#### Linear Regression is a basic and commonly used predictive analysis model. The model attempts to find the linear relationship between the input features and the target variable (sales).

```
Results: RMSE: 593.23 R² Score: -0.0170
```
### 2. Decision Tree Regressor

#### Decision Tree Regressor builds a model in the form of a tree structure. It breaks down the dataset into smaller subsets while at the same time an associated decision tree is incrementally

#### developed.

```
Results: RMSE: 855.12 R² Score: -1.1131
```
### 3. Random Forest Regressor

#### Random Forest Regressor improves the performance of decision trees by building multiple trees and combining their predictions. It reduces overfitting and improves accuracy.

```
Results: RMSE: 621.81 R² Score: -0.1173
```
### 4. Gradient Boosting Regressor

#### Gradient Boosting Regressor builds an ensemble of trees in a sequential manner, where each tree attempts to correct the errors of the previous one. This model is powerful and effective for regression tasks.

```
Results: RMSE: 609.70 R² Score: -0.0742
```
### 5. Support Vector Regressor (SVR)

#### Support Vector Regressor uses Support Vector Machines for regression tasks. It aims to fit the best line within a threshold value (epsilon) and is effective in high-dimensional spaces.

```
Results: RMSE: 588.42 R² Score: -0.0006
```

### 6. Logistic Regression

#### Logistic Regression is typically used for classification tasks, but here it was included for comparative purposes. Its performance indicates it is not suitable for regression tasks like sales prediction.

```
Results: Accuracy: 0.495
```

* ![Accuracy Comparison](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___42_0.png?raw=true)   
* ![Logistic REgression Accuracy](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___43_0.png?raw=true)   


## Conclusion

#### * Among the models tested, the Support Vector Regressor (SVR) performed the best with the lowest RMSE (588.42) and the least negative R² score (-0.001), making it the most accurate model
for predicting e-commerce product sales in this analysis.

#### * Best Performing Model: Support Vector Regressor (SVR)

#### * Next Steps: Consider tuning hyperparameters and exploring other algorithms for potentially better performance.
