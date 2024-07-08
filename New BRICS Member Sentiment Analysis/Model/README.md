# BRICS Sentiment Analysis - Model
## 📝 Description
This folder contains the pre-trained machine learning models and scripts used for sentiment analysis on the BRICS expansion dataset. The goal is to automatically categorize public comments into positive or negative sentiments, helping to understand public perceptions of the inclusion of new member nations in the BRICS alliance.

## 📂 Contents
  -**BRICS_Sentiment_Analysis.ipynb**: Jupyter Notebook containing the complete process of data preprocessing, model training, evaluation, and visualization. 
  
  -**lgb_model.pkl**: Pre-trained LightGBM model used for sentiment prediction.
  
  -**README.md**: This document.
## 🎯 Goal
The goal of this sentiment analysis project is to enhance understanding of public perceptions by organizing and analyzing comments on the inclusion of new member nations into the BRICS alliance. By automatically classifying these comments as positive or negative, the project aims to provide insights into public opinion trends.

## 🧮 What I Did
In this sentiment analysis project, various models were evaluated to find the most effective one for classifying public comments. The models evaluated include:

  *LSTM Model*
    -Long Short-Term Memory (LSTM) networks were used to capture the sequential dependencies in the text data.
    -The model was trained on padded sequences of tokenized text data.
    
  *Simple Neural Network*
    -A basic feedforward neural network was implemented using BERT embeddings.
    -The model included dense layers with ReLU activation and a final sigmoid activation for binary classification.
    
  *Stacking Classifier*
    -Stacking ensemble learning method combining multiple base classifiers such as RandomForest, ExtraTrees, and GradientBoosting, with a LogisticRegression meta-model.

  *LightGBM Classifier*
    -A Light Gradient Boosting Machine (LightGBM) was trained on BERT embeddings.Known for its efficiency and high performance with large datasets.
 
  *Multi-Layer Perceptron (MLP)*
  -An MLP was used with one hidden layer to classify sentiments based on BERT embeddings.
  
  *Advanced Stacking Classifier*
    -An advanced stacking ensemble that combines five base models: RandomForest, ExtraTrees, GradientBoosting, XGBoost, and LightGBM, with a LogisticRegression meta-model.

    
**Data Preprocessing and Augmentation**
Data Cleaning: Normalized text, removed missing values, and duplicates.
Tokenization and Lemmatization: Processed text data to remove stop words and perform lemmatization.
Synonym Replacement: Performed data augmentation by replacing words with their synonyms to enhance the training dataset.
Encoding Text Using BERT
BERT Tokenizer and Model: Used the BERT tokenizer to encode the text data and obtain embeddings for model input.

## 🚀 Models Implemented

**LSTM Model**

    -Architecture: Used embedding layers, LSTM layers, dropout layers, and dense layers.
    -Performance: Achieved an accuracy of 75.8%
    
**Simple Neural Network**

    -Architecture: Included dense layers with ReLU activation and sigmoid output.
    -Performance: Achieved an accuracy of 73.5%.

**Stacking Classifier**

    -Base Models: RandomForest, ExtraTrees, GradientBoosting.
    -Meta-Model: LogisticRegression.
    -Performance: Achieved an accuracy of 72.9%.

**LightGBM Classifier**

    -Algorithm: Light Gradient Boosting Machine.
    -Performance: Achieved an accuracy of 78.2%.

**Multi-Layer Perceptron (MLP)**

    -Architecture: Single hidden layer with dense connections.
    -Performance: Achieved an accuracy of 72.9%.

**Advanced Stacking Classifier**

    -Base Models: RandomForest, ExtraTrees, GradientBoosting, XGBoost, LightGBM.
    -Meta-Model: LogisticRegression.
    -Performance: Achieved an accuracy of 74.1%.

**Model Performance Analysis**
Training and Validation: Evaluated models based on accuracy, precision, and loss to select the best-performing model.

**Best Model**
The best-performing model, LightGBM, has been saved as lgb_model.pkl and is ready for deployment using Streamlit.

## 📈 Performance of the Models Based on Accuracy Scores
LSTM Model: Accuracy: 75.8%

Simple Neural Network: Accuracy: 73.5%

Stacking Classifier: Accuracy: 72.9%

LightGBM Classifier: Accuracy: 78.2%

Multi-Layer Perceptron (MLP): Accuracy: 72.9%

Advanced Stacking Classifier: Accuracy: 74.1%


## 📢 Conclusion
The BRICS sentiment analysis project demonstrates the effectiveness of machine learning models, particularly LightGBM, in accurately predicting public sentiment. The models help in organizing and prioritizing public comments, providing valuable insights for stakeholders.

## ✒️ Your Signature
Tanuj Saxena(https://linkedin.com/in/tanuj-saxena-970271252/) 
