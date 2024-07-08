# Gold Prices Prediction

## Overview :

This project focuses on predicting gold prices using machine learning models. Historical gold prices data, including features like Open, High, Low, and Close, are utilized. Various algorithms, such as Linear Regression,  Decision Trees, Random Forest, and Support Vector Machine (SVM), are employed for forecasting future gold prices.

## Goal :

The primary goal of this project is to leverage machine learning techniques for predicting gold prices based on historical data. By employing various algorithms such as Linear Regression, Decision Trees, Random Forest,  and Support Vector Machine (SVM), we aim to create accurate and reliable models for forecasting future gold prices.

## About the Dataset:

The dataset utilized in this project contains historical information about gold prices. It includes the following key features:

- **Date**: The timestamp when the price data was recorded.
- **Open**: The opening price of gold on a given day.
- **High**: The highest price of gold on a given day.
- **Low**: The lowest price of gold on a given day.
- **Close**: The closing price of gold on a given day.

### Data Source:

The dataset was sourced from https://www.kaggle.com/datasets/gvyshnya/gold-future-prices. It spans a specific time period, allowing for the analysis and prediction of gold prices based on historical trends.

### Data Exploration:

Before building predictive models, it's essential to explore and understand the characteristics of the dataset. The Jupyter Notebook (`gold_price_predictions.ipynb`) provides detailed exploratory data analysis, visualizations, and insights into the dataset.

## Visualizations:

Explore visual representations of the data and model performance. These visualizations provide insights into the trends in gold prices and the effectiveness of different machine learning models.

1. **Time Series Plot of Gold Prices:**

   ![Line Plot of Gold Prices Over Time](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/60dc79a7-6bae-43f3-b721-d9cc05958958)


   *Description:* A line plot depicting the historical trend of gold prices over time. This visualization helps identify patterns and seasonality in the data.

2. **Comparison of Predicted vs. Actual Gold Prices:**
    ![Scatter Plot of Predicted vs  Actual Values](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/f8287dd6-6cfc-4290-b96e-1f67f064d3bb)

   *Description:* Scatter plot comparing the predicted gold prices from the machine learning models against the actual prices. A strong alignment indicates accurate predictions.


3. **Rolling Average of Gold Close Prices:**
  ![Gold Close Price with 30-Day Rolling Average](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/e3f1d8e0-5318-4e24-bd0c-f5d7bbae494e)

   *Description:* Line chart displaying the rolling average of gold close prices over a specific window. This visualization smoothes out short-term fluctuations, revealing long-term trends.

4. **Distribution of Gold Price Attributes**:
   ![Histograms of Gold Price Attributes](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/970b7087-bd2d-4095-8d45-92dde2d78464)

   *Description*: Histograms providing a visual representation of the distribution of gold price attributes.

5. **Gold Price Candlestick Chart:**
   ![Gold Price Candlestick Chart](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/d01b2ae4-2f7c-4bee-a815-b79427da41c7)

   *Description*: Candlestick chart illustrating the open, high, low, and close prices of gold over a specific time period.

6. **Autocorrelation Plot of Gold Close Price**:
  ![Autocorrelation Plot of Gold Close Price](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/1ed6ba79-47f3-4314-a92b-071b996aad0b)

   *Description*: Autocorrelation plot displaying the correlation of gold close prices with their lagged values.

6. **Comparison of Algorithm Accuracy:**
   ![Comparison of Algorithm Accuracy](https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/9e96e0da-37bd-4c23-967a-a4e9222c51e1)

   *Description*: Bar chart comparing the accuracy of different machine learning algorithms based on mean squared error.

## Machine Learning Models and Implementations:

This project leverages various machine learning models to predict gold prices based on historical data. Each model serves a specific purpose in capturing different aspects of the underlying patterns in the dataset.

### 1. Linear Regression Model

- **Purpose:** Linear Regression is used for establishing a linear relationship between the features (e.g., Open, High, Low) and the target variable (Close) to predict gold prices.
  
- **Implementation:** The Linear Regression model is trained on historical data to learn the coefficients that best fit the linear equation. The trained model is saved as `linear_regression_model.pkl`.

  <img width="373" alt="m1" src="https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/c1ae21d8-14b7-4cff-9bfb-0886ff2c9a48">


### 2. Decision Tree Model

- **Purpose:** Decision Trees are employed to capture non-linear relationships and complex decision boundaries in the dataset.

- **Implementation:** The Decision Tree model is trained on features such as Open, High, Low, and historical gold prices. The trained model is saved as `decision_tree_model.pkl`.

<img width="333" alt="m2" src="https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/16b5f0e3-5a0b-442b-bd38-f5d7c8a10210">


### 3. Random Forest Model

- **Purpose:** Random Forest is an ensemble model that combines multiple Decision Trees to improve accuracy and robustness.

- **Implementation:** The Random Forest model is trained on the dataset, and the ensemble of trees collectively makes predictions. The trained model is saved as `random_forest_model.pkl`.

<img width="327" alt="m3" src="https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/f6e37857-593f-49e0-ad1f-19a50696ecc1">


### 4. Support Vector Machine (SVM) Model

- **Purpose:** Support Vector Machine is used to find the hyperplane that best separates different classes in a high-dimensional space.

- **Implementation:** The SVM model is trained on features to predict gold prices. The trained model is saved as `svm_model.pkl`.

  <img width="290" alt="m4" src="https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/7c12fae0-a283-4143-b540-f21cc292c55f">


### 5. Gradient Boosting Model

- **Purpose:** Gradient Boosting is employed to build an ensemble of weak learners (typically decision trees) sequentially, with each tree correcting the errors of its predecessor.
  
- **Implementation:** The Gradient Boosting model is trained on the dataset, and the weak learners are combined to create a strong predictive model. The trained model is saved as `gradient_boosting_model.pkl`.

<img width="350" alt="m5" src="https://github.com/Bayyana-kiran/ML-Crate/assets/99533113/cdf9f095-d338-4183-af86-57d16a3e7b82">

## Libraries Used

This project makes use of several Python libraries to analyze data, implement machine learning models, and create visualizations. Below is a list of the main libraries used:

1. **pandas**: A powerful data manipulation library for data analysis.
2. **numpy**: A library for numerical operations in Python.
3. **scikit-learn**: A machine learning library providing simple and efficient tools for data mining and data analysis.
4. **matplotlib**: A 2D plotting library for creating static, animated, and interactive visualizations in Python.
5. **seaborn**: A statistical data visualization library based on matplotlib.
6. **plotly**: A graphing library that makes interactive, publication-quality graphs online.
7. **jupyter**: An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.

## Conclusion

In conclusion, the Gold Prices Prediction project leverages machine learning algorithms to forecast gold prices based on historical data. The exploration and analysis of the dataset, along with the implementation of various algorithms, provide valuable insights into the trends and patterns of gold prices. This project serves as a practical demonstration of applying machine learning techniques to financial forecasting, contributing to a better understanding of market dynamics.

## Contributor: (Contributing under IWOC 2.0)

Sai Kiran B L S

https://github.com/Bayyana-kiran













