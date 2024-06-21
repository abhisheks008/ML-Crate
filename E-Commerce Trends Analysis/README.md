# E-commerce Product Trends Analysis

## Table of Contents

```
* Goal 
* Dataset
* Description 
* What I Had Done 
* Installation 
* Libraries 
* EDA Results
* Models and Results 
* Conclusion 
* Contributing 
* Signature
```
## Goal

#### To analyze e-commerce product trends and predict sales using various machine learning models.

## Dataset

#### Link: The dataset is provided within the notebook and contains various e-commerce product

#### details.

## Description

#### This folder contains the code and resources for analyzing e-commerce product trends and

#### predicting sales using various machine learning models.

#### The analysis is based on product details such as product name, category, price, rating,

#### number of reviews, stock quantity, discount, and sales.

## What I Had Done

## Installation

#### Clone the repository using the following command:

```
git clone https://github.com/yourusername/ecommerce-product-trends.git cd
ecommerce-product-trends
```
#### To run the notebook and reproduce the results, you need to have Python installed along

#### with the necessary libraries. You can install the required libraries using the following

#### command:

```
pip install -r requirements.txt
```
#### Run the Jupyter notebook:

```
jupyter notebook ecommerce-trends-eda-models.ipynb
```
## Libraries Needed

#### pandas

#### numpy

#### matplotlib

#### seaborn

#### plotly

#### scikit-learn

#### warnings

## Exploratory Data Analysis Results

#### The dataset contains a wide range of product categories with varying prices, ratings, number

#### of reviews, stock quantities, discounts, and sales.

#### Initial visualizations indicate significant trends and correlations among these features.

### Graphs and Analysis

#### 1. Relationship Graphs

#### relationship graphs

#### Insights: There are clear trends between price and sales, rating and sales, and discount

#### and sales.

#### 2. Cluster Graphs

#### cluster graphs

#### Insights: Products are clustered into different groups based on their features, which

#### helps in segmenting the data.

#### 3. Correlation Matrix

#### Pearson correlation Matrix

#### Insights: The Pearson correlation matrix shows the linear correlation between different

#### features.

#### 4. Predictive Power Score

#### predictive power score

#### Insights: This score helps in identifying the predictive power of different features for

#### the target variable.

#### 5. Line of Best Fit Graphs

#### line of best fit graphs

#### Insights: These graphs show the trends and best fit lines for key relationships in the

* ![description of dataset](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___7_1.png?raw=true)
* ![Distribution of ratings](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___8_1.png?raw=true)
* ![Distribution of other features](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___9_1.png?raw=true)
* ![correlation matrix](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___13_0.png?raw=true)
* ![Top 10 Products](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___15_0.png?raw=true)
* ![price vs sales clustering graph](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___17_0.png?raw=true)
* ![pairplot of numerical features](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___18_2.png?raw=true)
* ![Word Cloud](https://github.com/adi271001/ML-Crate/blob/ecommerce-trends/E-Commerce%20Trends%20Analysis/Images/__results___31_1.png?raw=true)   

#### data.

## Models and Results

#### The project explores the following machine learning models to predict sales:

### 1. Linear Regression

```
Results: RMSE: 593.23 R² Score: -0.0170
```
### 2. Decision Tree Regressor

```
Results: RMSE: 855.12 R² Score: -1.1131
```
### 3. Random Forest Regressor

```
Results: RMSE: 621.81 R² Score: -0.1173
```
### 4. Gradient Boosting Regressor

```
Results: RMSE: 609.70 R² Score: -0.0742
```
### 5. Support Vector Regressor (SVR)

```
Results: RMSE: 588.42 R² Score: -0.0006
```
### 6. Logistic Regression

```
Results: Accuracy: 0.495
```
## Conclusion

#### Based on the evaluation of various machine learning models, the Support Vector Regressor (SVR)

#### emerged as the best-performing model with the lowest RMSE (588.42) and the least negative R²

#### score (-0.001), indicating it provides the most accurate predictions among the tested models.

#### Best Performing Model: Support Vector Regressor (SVR) due to its lowest RMSE and R²

#### scores.

#### Next Steps: Verify the data processing steps and re-evaluate the models to identify any

#### issues. Consider tuning model hyperparameters and exploring other algorithms for

#### improved performance.

#### Important Features: Features such as price, rating, and discount were expected to be

#### influential in predicting sales.

## Contributing

#### Contributions are welcome! Please read the contribution guidelines first.

## Signature

#### Aditya D

#### Github: https://www.github.com/adi271001

#### LinkedIn: https://www.linkedin.com/in/aditya-d-23453a179/

#### Topmate: https://topmate.io/aditya_d/

#### Twitter: https://x.com/ADITYAD29257528
