# Fictional Character Battle Outcome Prediction Project

## Goal
The goal of this project is to predict the outcomes of battles between fictional characters using various machine learning models.

## Dataset
The dataset used for this project is the ["Fictional Character Battle Outcome Prediction"](https://www.kaggle.com/datasets/rabieelkharoua/fictional-character-battle-outcome-prediction/data) dataset from Kaggle.

## Description
The dataset contains features related to fictional characters and the outcomes of their battles. The features include attributes such as strength, intelligence, speed, durability, power, and combat skills of the characters. The target variable is the outcome of the battle.

## What I Had Done
1. **Data Preprocessing**:
    - Loaded the dataset.
    - Handled missing values.
    - Encoded categorical variables.
    - Split the data into training and testing sets.

2. **Exploratory Data Analysis (EDA)**:
    - Visualized the distribution of features.
    - Analyzed the correlation between features.
    - Examined the class distribution of the target variable.

3. **Model Training and Evaluation**:
    - Trained multiple machine learning models.
    - Evaluated the performance of each model using accuracy, precision, recall, and F1 score.
    - Implemented a stacking classifier as an ensemble method.

## Models Implemented
The following machine learning models were implemented and evaluated in this project:

1. **Random Forest**:
    - A versatile ensemble learning method that operates by constructing multiple decision trees during training and outputs the mode of the classes for classification.

2. **Support Vector Classifier (SVC)**:
    - A supervised learning model that analyzes data for classification by finding the hyperplane that best separates the classes.

3. **Logistic Regression**:
    - A statistical model that in its basic form uses a logistic function to model a binary dependent variable.

4. **Decision Tree**:
    - A decision support tool that uses a tree-like graph of decisions and their possible consequences.

5. **K-Nearest Neighbors (KNN)**:
    - A simple, instance-based learning algorithm that assigns a class to a sample based on the majority class among its k-nearest neighbors.

6. **Gradient Boosting**:
    - An ensemble technique that builds models sequentially, each new model correcting errors made by previous models.

7. **AdaBoost**:
    - A boosting algorithm that combines the predictions of several base estimators to improve robustness over a single estimator.

8. **CatBoost**:
    - A high-performance library for gradient boosting on decision trees, especially well-suited for categorical data.

9. **Extra Trees**:
    - An ensemble learning method similar to Random Forest but with more randomness in the splitting of nodes.

10. **XGBoost**:
    - An optimized distributed gradient boosting library designed to be highly efficient, flexible, and portable.

11. **Bagging Classifier**:
    - An ensemble meta-estimator that fits base classifiers each on random subsets of the original dataset and then aggregates their predictions.

12. **Stacking Classifier**:
    - An ensemble learning technique that combines multiple base classifiers via a meta-classifier. The base classifiers are trained on the training dataset, and the meta-classifier is trained on the outputs of the base classifiers.

## Libraries Needed
The following libraries were used in this project:
- pandas
- numpy
- matplotlib
- scikit-learn
- xgboost
- catboost
- mlxtend

## EDA Results
- Visualizations of feature distributions showed that most features are normally distributed.
- Correlation analysis indicated that certain features like strength and power have a high correlation.
- The target variable was found to be balanced, with a nearly equal distribution of battle outcomes.

![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___13_0.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___14_0.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___15_1.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___15_3.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___15_5.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___16_1.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___17_0.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___18_0.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___19_0.png?raw=true)
![eda-1](https://github.com/adi271001/ML-Crate/blob/Fictional-Character-Battle/Fictional%20Character%20Battle%20Outcome%20Prediction/Images/__results___20_0.png?raw=true)

## Performance of the Models based on Accuracy Scores

| Model                   | Accuracy | Precision | Recall | F1 Score |
|-------------------------|----------|-----------|--------|----------|
| Random Forest           | 0.752665 | 0.686600  | 0.662923 | 0.671616 |
| Support Vector Classifier | 0.773987 | 0.721856  | 0.665816 | 0.681222 |
| Logistic Regression     | 0.763326 | 0.702406  | 0.663184 | 0.675493 |
| Decision Tree           | 0.710021 | 0.638167  | 0.638167 | 0.638167 |
| K-Nearest Neighbors     | 0.735608 | 0.661683  | 0.639267 | 0.646975 |
| Gradient Boosting       | 0.773987 | 0.717072  | 0.689528 | 0.699925 |
| AdaBoost                | 0.782516 | 0.728192  | 0.712026 | 0.718984 |
| CatBoost                | 0.761194 | 0.699333  | 0.683050 | 0.689800 |
| Extra Trees             | 0.733475 | 0.658311  | 0.635421 | 0.643107 |
| XGBoost                 | 0.727079 | 0.656931  | 0.652337 | 0.654464 |
| Bagging Classifier      | 0.739872 | 0.667861  | 0.644588 | 0.652669 |
| Stacking Classifier     | 0.752665 | 0.687412  | 0.670036 | 0.676997 |

## Conclusion
Among the models evaluated, **AdaBoost** achieved the highest accuracy of 78.25%. This model is the best performer due to its ability to adaptively adjust the weights of misclassified instances, leading to improved performance in the prediction task. AdaBoost’s strong performance across multiple metrics, including precision, recall, and F1 score, highlights its effectiveness in handling this classification problem.

## Signature
- **Name:** Aditya D
- **Github:** [https://www.github.com/adi271001](https://www.github.com/adi271001)
- **LinkedIn:** [https://www.linkedin.com/in/aditya-d-23453a179/](https://www.linkedin.com/in/aditya-d-23453a179/)
- **Topmate:** [https://topmate.io/aditya_d/](https://topmate.io/aditya_d/)
- **Twitter:** [https://x.com/ADITYAD29257528](https://x.com/ADITYAD29257528)
