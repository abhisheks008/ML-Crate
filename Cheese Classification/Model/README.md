# Cheese Type Classification - Models and Results

## Table of Contents

- [Models](#models)
- [Results](#results)
- [Conclusion](#conclusion)
- [Signature](#signature)

## Models

The project explores the following machine learning models to classify different types of cheese:

### 1. K-Nearest Neighbors (KNN)

**Description**: 
KNN is a simple, instance-based learning algorithm where classification is based on the majority vote of the nearest neighbors.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_1.png)

### 2. Logistic Regression

**Description**: 
Logistic Regression is a linear model for binary classification that uses a logistic function to model the probability of a certain class.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_2.png)

### 3. Decision Tree

**Description**: 
Decision Trees are non-parametric supervised learning methods used for classification. The model predicts the target variable by learning simple decision rules inferred from the data features.

![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_3.png)

### 4. Support Vector Machine (SVM)

**Description**: 
SVM is a supervised learning model that analyzes data for classification and regression analysis. It finds the hyperplane that best divides a dataset into classes
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_4.png)

### 5. Random Forest

**Description**: 
Random Forest is an ensemble learning method that operates by constructing multiple decision trees and outputting the class that is the mode of the classes of individual trees.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_5.png)

### 6. Gradient Boosting

**Description**: 
Gradient Boosting is an ensemble learning technique that builds models sequentially. Each new model attempts to correct errors made by the previous model.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___60_6.png)

### 7. AdaBoost

**Description**: 
AdaBoost is an ensemble learning method that combines multiple weak classifiers to create a strong classifier. It adjusts the weights of misclassified instances to focus on hard-to-classify cases.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_7.png)

### 8. Extra Trees

**Description**: 
Extra Trees is similar to Random Forest but with more randomness in node splitting, reducing variance and improving performance.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_8.png)

### 9. Naive Bayes

**Description**: 
Naive Bayes classifiers are probabilistic classifiers based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_9.png)

### 10. XGBoost

**Description**: 
XGBoost is an optimized gradient boosting framework that is efficient and performs well on structured data.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_10.png)

### 11. CatBoost

**Description**: 
CatBoost is a gradient boosting algorithm that handles categorical features automatically and efficiently, often providing high accuracy with minimal parameter tuning.
![Relationship Graphs](https://github.com/adi271001/ML-Crate/blob/cheese-classification/Cheese%20Classification/Images/__results___69_11.png)

## Results

The accuracy results for each model are as follows:

- **K-Nearest Neighbors**: 0.62
- **Logistic Regression**: 0.633
- **Decision Tree**: 0.713
- **Support Vector Machine**: 0.647
- **Random Forest**: 0.72
- **Gradient Boosting**: 0.767
- **AdaBoost**: 0.727
- **Extra Trees**: 0.70
- **Naive Bayes**: 0.64
- **XGBoost**: 0.727
- **CatBoost**: 0.74

## Conclusion

After evaluating various machine learning models, it is evident that ensemble methods such as Gradient Boosting, CatBoost, and Random Forest perform significantly better than single classifiers like K-Nearest Neighbors or Logistic Regression. These models effectively capture complex relationships within the data, leading to higher classification accuracy.

- **Best Performing Models:** Gradient Boosting and CatBoost achieved the highest accuracy scores, indicating robust predictive performance.
- **Important Features:** Features such as fat content, moisture content, and aging time were consistently found to be the most influential in classifying cheese types.

## Signature

Aditya D
* GitHub: [adi271001](https://www.github.com/adi271001)
* LinkedIn: [Aditya D](https://www.linkedin.com/in/aditya-d-23453a179/)
* Topmate: [Aditya D](https://topmate.io/aditya_d/)
* Twitter: [@ADITYAD29257528](https://x.com/ADITYAD29257528)
