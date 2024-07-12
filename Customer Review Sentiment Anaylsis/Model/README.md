# Customer Review Sentiment Analysis - Model
## 📝 Description
This folder contains the pre-trained machine learning models and scripts used for sentiment analysis on the customer review dataset. The goal is to automatically categorize customer reviews into positive, neutral, or negative sentiments, helping to understand public perceptions of products.

## 📂 Contents
  -**customer-review-sentiment-analysis.ipynb:** Jupyter Notebook containing the complete process of data preprocessing, model training, evaluation, and visualization.
  
  -**model.pkl**: Pre-trained Logistic Regression model used for sentiment prediction.

  -**tfidf_vectorizer.pkl:** Pre-trained TF-IDF vectorizer used for transforming text data.

  -**README.md**: This document.

## 🎯 Goal
The goal of this sentiment analysis project is to enhance understanding of customer perceptions by organizing and analyzing reviews. By automatically classifying these reviews as positive, neutral, or negative, the project aims to provide insights into public opinion trends.

## 🧮 What I Did
In this sentiment analysis project, various models were evaluated to find the most effective one for classifying customer reviews. The models evaluated include:

### Logistic Regression

A simple linear model for binary and multi-class classification.
Achieved a high accuracy and balanced precision-recall performance.
### LightGBM Classifier

A Light Gradient Boosting Machine known for its efficiency and performance with large datasets.
Achieved competitive accuracy and was used as one of the benchmark models.
### XGBoost Classifier

An implementation of gradient-boosted decision trees designed for speed and performance.
Achieved competitive accuracy and served as another benchmark model.
### AdaBoost Classifier

An ensemble method that combines multiple weak classifiers to create a strong classifier.
Achieved good performance, particularly in precision and recall.

### Data Preprocessing and Augmentation

**Data Cleaning:** Normalized text, removed missing values, and duplicates.

**Tokenization:** Processed text data to remove stop words and perform lemmatization.

**TF-IDF Vectorization:** Converted text data into numerical features using TF-IDF.


## 🚀 Models Implemented

**Logistic Regression Model**

    -Achieved an accuracy of 90.0%.
    -Precision: 0.89, Recall: 0.90,
    -F1-score: 0.89 (weighted average).

    
**XGBoost Classifier**

    -Achieved an accuracy of 89.0%.
    -Precision: 0.88, Recall: 0.89
    -F1-score: 0.87 (weighted average).

**AdaBoost Classification**

    -Achieved an accuracy of 88.0%.
    -Precision: 0.86, Recall: 0.88
    -F1-score: 0.86 (weighted average).

**LightGBM Classifier**

    -chieved an accuracy of 89.0%.
    -Precision: 0.88, Recall: 0.89
    -F1-score: 0.88 (weighted average).

**Multi-Layer Perceptron (MLP)**

    -Achieved an accuracy of 90.0%.
    -Precision: 0.89, Recall: 0.90,
    -F1-score: 0.89 (weighted average).


**Model Performance Analysis**
Training and Validation: Evaluated models based on accuracy, precision, and loss to select the best-performing model.


**Best Model**
The best-performing model, Logistic, has been saved as model.pkl and is ready for deployment using Streamlit.

## 📢 Conclusion
The customer review sentiment analysis project demonstrates the effectiveness of machine learning models, particularly Logistic Regression, in accurately predicting customer sentiment. The models help in organizing and prioritizing customer reviews, providing valuable insights for stakeholders.

## ✒️ Your Signature
Tanuj Saxena[LinkedIn](https://linkedin.com/in/tanuj-saxena-970271252/) 
