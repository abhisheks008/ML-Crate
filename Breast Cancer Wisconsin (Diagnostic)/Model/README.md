**Breast Cancer Wisconsin (Diagnostic)**

**GOAL**

To Determine which features of data (measurements) are most important for diagnosing breast cancer and find out if breast cancer occurs or not.

**DATASET**

https://www.kaggle.com/uciml/breast-cancer-wisconsin-data

**DESCRIPTION**
- Breast cancer is the most common cancer amongst women in the world. It accounts for 25% of all cancer cases, and affected over 2.1 Million people in 2015 alone. It starts when cells in the breast begin to grow out of control. These cells usually form tumors that can be seen via X-ray or felt as lumps in the breast area.
- Hence, we need to classify the dataset into whether the person will be having brest cancer or not.
- The goal of this project is to analyse the data and classify whether the person will be having brest cancer ot not and build a model accordingly.

**WHAT I HAD DONE**

-> Importing the libraries

-> Loaded the dataset

Preprocessing of the dataset:

-> Knowing some of the statistical measures information

-> Visualizing the data

-> Correlation

-> Splitting the dataset

-> Training the data 

-> Models used:
    - Random forest regressor
    - Logistic regression
    - Decision Trees

-> Evaluation of the model

-> Predicting the output of new data from the model having the high accuracy


**MODELS USED**
- Random forest regressor:

A random forest regressor. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting
- Logistic regression:

Logistic regression is the appropriate regression analysis to conduct when the dependent variable is dichotomous (binary).  Like all regression analyses, the logistic regression is a predictive analysis.  Logistic regression is used to describe data and to explain the relationship between one dependent binary variable and one or more nominal, ordinal, interval or ratio-level independent variables.
- Decision Trees:

Decision Trees are a type of Supervised Machine Learning (that is you explain what the input is and what the corresponding output is in the training data) where the data is continuously split according to a certain parameter.

**LIBRARIES NEEDED**

- pandas
- matplotlib
- seaborn
- sklearn

**ACCURACIES**
- Random forest regressor: 79.44695652173913
- Logistic regression: 63.29670329670329
- Decision Trees: 89.47368421052632


**CONCLUSION**

- Downloaded the dataset from kaggle, loading the required libraries, Data Pre-Processing, Splitting of data, building the models, testing thier accuracies and finilizing the model based on accuracy.
- I have used three models to train the data starting with Random forest regressor, then SLogistic regression and after that Decision Trees. I have finilized the Decision Trees which is having highest accuracy.
- Decision Trees is used to determine which features of data (measurements) are most important for diagnosing breast cancer and find out if breast cancer occurs or not  with an accuracy over 89%

**YOUR NAME**

Deepthi M

GitHub: https://github.com/deepthi1107

Linkedin: https://www.linkedin.com/in/deepthi-m-1107/
