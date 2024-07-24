# Bank Credit Analysis

## 🎯 Goal
The main goal of this project is to develop machine learning models to accurately predict the likelihood of a customer subscribing to a term deposit based on their banking information and demographic details.

## 🧵 Dataset
The dataset for this project is sourced fromm [Kaggle's Bank Marketing Dataset](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset/data).

## 🧾 Description
This project involves analyzing various features of bank customers and building machine learning models to predict whether a customer will subscribe to a term deposit. The project includes data preprocessing, exploratory data analysis (EDA), model development, and evaluation to find the most accurate predictive model.

## 🧮 What I had done!
1. **Data Collection and Preprocessing**:
   - Collected the dataset from Kaggle.
   - Preprocessed the data to handle missing values, encoded categorical variables, and split the dataset into training and testing sets.

2. **Exploratory Data Analysis (EDA)**:
   - Performed EDA to understand the distribution of data and identify any patterns or anomalies.
   - ![pair plot 1](https://github.com/adi271001/ML-Crate/blob/Bank-Credit-Analysis/Bank%20Credit%20Analysis/Images/__results___11_1.png?raw=true)
   - ![distribution graph](https://github.com/adi271001/ML-Crate/blob/Bank-Credit-Analysis/Bank%20Credit%20Analysis/Images/__results___13_0.png?raw=true)
   - ![boxplot](https://github.com/adi271001/ML-Crate/blob/Bank-Credit-Analysis/Bank%20Credit%20Analysis/Images/__results___15_0.png?raw=true)
   - ![waveplot](https://github.com/adi271001/ML-Crate/assets/67856422/f6e50edc-6cc9-475b-b3bb-82869b1cba8f)
   - ![bar plot](https://github.com/adi271001/ML-Crate/assets/67856422/55cebd86-4eec-4829-85d1-091f0ebfbc3d)
     
3. **Model Development**:
   - Implemented several machine learning models including Random Forest, XGBoost, Decision Tree, AdaBoost, CatBoost, Logistic Regression, Extra Trees, Gaussian Naive Bayes, K-Nearest Neighbors, and Support Vector Machine.
   - Used grid search for hyperparameter tuning and nested cross-validation to evaluate model performance.

4. **Model Evaluation**:
   - Evaluated the models based on accuracy scores on the training and testing datasets.

5. **Conclusion**:
   - Identified the best-performing model based on accuracy scores.

## 🚀 Models Implemented
- **Random Forest**: Chosen for its robustness and ability to handle large datasets with higher accuracy.
- **XGBoost**: Known for its performance and speed, making it suitable for complex datasets.
- **Decision Tree**: Simple to interpret and visualize, though prone to overfitting.
- **AdaBoost**: Effective in boosting the performance of weak classifiers.
- **CatBoost**: Handles categorical features well and provides high accuracy.
- **Logistic Regression**: Baseline model for classification tasks.
- **Extra Trees**: Similar to Random Forest but with some differences in the splitting of nodes.
- **Gaussian Naive Bayes**: Simple and effective, especially for smaller datasets.
- **K-Nearest Neighbors**: Simple and easy to implement, but can be computationally expensive.
- **Support Vector Machine**: Effective in high-dimensional spaces and suitable for classification tasks.

## 📚 Libraries Needed
- pandas
- numpy
- scikit-learn
- xgboost
- catboost

## 📊 Exploratory Data Analysis Results
*Include images of visualizations here*

## 📈 Performance of the Models based on the Accuracy Scores
| Model                   | Train Accuracy | CV Mean Accuracy | Test Accuracy |
|-------------------------|----------------|------------------|---------------|
| K Nearest Neighbors     | 81.81%         | 75.38%           | 75.19%        |
| Support Vector Machine  | 83.37%         | 82.92%           | 81.59%        |
| Random Forest           | 99.40%         | 85.79%           | 83.70%        |
| XGBoost                 | 100.00%        | 85.47%           | 84.42%        |
| Decision Tree           | 87.51%         | 81.92%           | 80.25%        |
| AdaBoost                | 84.04%         | 82.91%           | 82.58%        |
| CatBoost                | 90.36%         | 86.58%           | 85.89%        |
| Logistic Regression     | 82.55%         | 82.10%           | 81.68%        |
| Extra Trees             | 98.76%         | 83.38%           | 82.22%        |
| Gaussian Naive Bayes    | 73.92%         | 73.58%           | 74.56%        |

## 📢 Conclusion
The best-performing model in this project is CatBoost with a CV Mean Accuracy of 86.58% and Test Accuracy of 85.89%. This model provides a good balance between training and generalization performance, making it the most suitable for predicting customer subscription to a term deposit.

## ✒️ Your Signature
Aditya D

GitHub: [https://www.github.com/adi271001](https://www.github.com/adi271001)  
LinkedIn: [https://www.linkedin.com/in/aditya-d-23453a179/](https://www.linkedin.com/in/aditya-d-23453a179/)  
Topmate: [https://topmate.io/aditya_d/](https://topmate.io/aditya_d/)  
Twitter: [https://x.com/ADITYAD29257528](https://x.com/ADITYAD29257528)
