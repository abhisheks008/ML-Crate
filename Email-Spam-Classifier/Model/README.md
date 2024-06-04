# Email Spam Classifier 
The Email Spam Classifier is a machine learning model designed to classify emails as either spam or non-spam (ham). It is trained on a dataset containing email messages along with their corresponding labels indicating whether they are spam or not. 


![interface](https://github.com/codewithpiyushh/ML-Crate/assets/154052068/5260f688-fae9-4bfc-8263-20e06c50e56c)

## Overview

Email spam remains a persistent issue in modern communication, with spam emails often inundating inboxes and posing security risks to users. The Email Spam Classifier aims to mitigate this problem by automatically identifying and filtering out spam emails, thereby enhancing the efficiency of email management and reducing the risk of falling victim to phishing attacks or malicious content.


## Data Preprocessing

Prepare data for analysis: handle missing values, encode categorical data, scale features, perform feature engineering, split into train-test sets, and normalize data. Ensure data is in a suitable format for machine learning algorithms.

## Libraries Used

- scikit-learn: Machine learning library for model training and evaluation.
- pandas: Data manipulation library for preprocessing and data handling.
- numpy: Numerical computing library for mathematical operations.
- matplotlib, seaborn, plotly: Visualization libraries for data exploration and analysis.


## Model Details
### Hyperparameter Tuning Results

- *Logistic Regression*:
  - Best Parameters: {'C': 10, 'penalty': 'l2'}
  - Accuracy: 0.973
  - Precision: 0.973

- *K-Neighbors Classifier*:
  - Best Parameters: {'n_neighbors': 3}
  - Accuracy: 0.999
  - Precision: 0.906

- *Naive bayes*:
  - Best Parameters: {'min_samples_split': 5, 'max_depth': 20}
  - Accuracy: 0.977
  - Precision: 0.977

- *Decision Tree Classifier*:
  - Best Parameters: {'max_depth': 7}
  - Accuracy: 0.937
  - Precision: 0.933

- *Support Vector Machine*:
  - Best Parameters: {'gamma': 0.1, 'kernel': 'linear'}  
  - Accuracy: 0.978
  - Precision: 0.978

### Accuracy Score

The accuracy score is a metric used to measure the overall performance of the email spam classifier model. It represents the proportion of correctly predicted instances (emails) out of the total instances. In the context of the email spam classifier model, the accuracy score indicates the percentage of correctly predicted spam and non-spam (ham) emails. A higher accuracy score indicates that the classifier effectively distinguishes between spam and legitimate emails.

#### Determining the Best Model
To determine the best model among the trained classifiers for the email spam classifier, we consider both the accuracy score and the precision.

Accuracy Score: We evaluate the models based on their accuracy scores on the test dataset. A higher accuracy score indicates that the model predicts spam and non-spam emails more accurately.

AUC-ROC: Additionally, we assess the models using the Area Under the Receiver Operating Characteristic curve (AUC-ROC) value. A higher AUC-ROC value signifies better overall performance in distinguishing between spam and non-spam emails, considering both sensitivity and specificity.

By comparing the accuracy scores and AUC-ROC values of different models, we can identify the most effective model for classifying emails as spam or non-spam. Typically, the model with the highest accuracy score and AUC-ROC value is selected as the best-performing model for deployment.
