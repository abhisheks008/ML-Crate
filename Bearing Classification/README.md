# Bearing Classification using ML 

## PROJECT TITLE

Bearing Classification

## GOAL

To identify faulty and healthy bearing. 

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/datasets/zlemglsmklkaya/healthy-vs-faulty-bearings/data?select=Healthy-bearing.csv

## EDA:
![Alt text](Images/Input_Dataset.png)
![Alt text](Images/EDA1.png)
Shape: (1998,2)

## DESCRIPTION

This project aims to identify the faulty and helthy bearings.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the data to create valid features.
3. Model selection: XGBC,Random Forest,Logestic Regression,Gaussian Bayes,AdaBoost Classifier.
4. Comparative analysis: Compared the accuracy score of all the models.


## MODELS SUMMARY

- XGBC
- Logistic Regression
- Adaboost Classifier
- Random Forest Classifier
- Gaussian Bayes

## LIBRARIES NEEDED

The following libraries are required to run this project:

- matplotlib
- numpy
- pandas
- sklearn

## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 

It is shown using Confusion Matrix in the Images folder

## RESULTS
Results on Val dataset:
XGBC: 77.33%
Random Forest: 77.67%
Adaboost: 75%
Logistic Regression: 74%
Gaussian Bayes: 73.33%
DTC:77.33%
![Alt text](Images/Metrics.png)

## CONCLUSION
Based on results we can draw following conclusions:

1.The Random Forest worked the best