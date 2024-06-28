# Cheese Type Classification

## Table of Contents

- [Goal](#goal)
- [Dataset](#dataset)
- [Description](#description)
- [What I Had Done](#what-i-had-done)
- [Installation](#installation)
- [Libraries Needed](#libraries-needed)
- [Exploratory Data Analysis Results](#exploratory-data-analysis-results)
- [Models and Results](#models-and-results)
- [Conclusion](#conclusion)
- [Contributing](#contributing)
- [Signature](#signature)

## Goal

To classify different types of cheese using various machine learning models.

## Dataset

Link: [Cheese Dataset](https://www.kaggle.com/datasets/jainaru/cheese-across-the-world)

## Description

* This folder contains the code and resources for classifying different types of cheese using various machine learning models.
* The classification is based on various features such as fat content, moisture content, texture, color, and aging time.

## What I Had Done

## Installation

* Clone the repository using the following command:
    ```bash
    git clone https://github.com/yourusername/cheese-type-classification.git
    cd cheese-type-classification
    ```

* To run the notebook and reproduce the results, you need to have Python installed along with the necessary libraries. You can install the required libraries using the following command:
    ```bash
    pip install -r requirements.txt
    ```

* Run the Jupyter notebook:
    ```bash
    jupyter notebook cheese-type-classification.ipynb
    ```

## Libraries Needed

* pandas==1.3.3
* numpy==1.21.2
* matplotlib==3.4.3
* seaborn==0.11.2
* scipy==1.7.1
* statsmodels==0.12.2
* sklearn==0.24.2
* xgboost==1.4.2
* lightgbm==3.2.1
* catboost==0.26.1
* tqdm==4.62.2
* optuna==2.9.1

## Exploratory Data Analysis Results

* ![Relationship Graphs](https://github.com/yourusername/cheese-type-classification/images/relationship_graphs.png)
* ![Cluster Graphs](https://github.com/yourusername/cheese-type-classification/images/cluster_graphs.png)
* ![Pearson Correlation Matrix](https://github.com/yourusername/cheese-type-classification/images/pearson_correlation_matrix.png)
* ![Spearman Correlation Matrix](https://github.com/yourusername/cheese-type-classification/images/spearman_correlation_matrix.png)
* ![Predictive Power Score](https://github.com/yourusername/cheese-type-classification/images/predictive_power_score.png)
* ![Line of Best Fit Graphs](https://github.com/yourusername/cheese-type-classification/images/line_of_best_fit_graphs.png)

## Models and Results

The project explores the following machine learning models to classify different types of cheese:

### 1. K-Nearest Neighbors

**Results**:
- Accuracy: 0.62

### 2. Logistic Regression

**Results**:
- Accuracy: 0.633

### 3. Decision Tree

**Results**:
- Accuracy: 0.713

### 4. Support Vector Machine

**Results**:
- Accuracy: 0.647

### 5. Random Forest

**Results**:
- Accuracy: 0.72

### 6. Gradient Boosting

**Results**:
- Accuracy: 0.767

### 7. AdaBoost

**Results**:
- Accuracy: 0.727

### 8. Extra Trees

**Results**:
- Accuracy: 0.70

### 9. Naive Bayes

**Results**:
- Accuracy: 0.64

### 10. XGBoost

**Results**:
- Accuracy: 0.727

### 11. CatBoost

**Results**:
- Accuracy: 0.74

## Conclusion

After evaluating various machine learning models, it is evident that ensemble methods such as Gradient Boosting, CatBoost, and Random Forest perform significantly better than single classifiers like K-Nearest Neighbors or Logistic Regression. These models effectively capture complex relationships within the data, leading to higher classification accuracy.

- **Best Performing Models:** Gradient Boosting and CatBoost achieved the highest accuracy scores, indicating robust predictive performance.
- **Important Features:** Features such as fat content, moisture content, and aging time were consistently found to be the most influential in classifying cheese types.

## Contributing

Contributions are welcome! Please read the contribution guidelines first.

## Signature

Aditya D
* GitHub: [adi271001](https://www.github.com/adi271001)
* LinkedIn: [Aditya D](https://www.linkedin.com/in/aditya-d-23453a179/)
* Topmate: [Aditya D](https://topmate.io/aditya_d/)
* Twitter: [@ADITYAD29257528](https://x.com/ADITYAD29257528)
