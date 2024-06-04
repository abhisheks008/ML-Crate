# Email Spam Classifier 
The Email Spam Classifier is a machine learning model designed to classify emails as either spam or non-spam (ham). It is trained on a dataset containing email messages along with their corresponding labels indicating whether they are spam or not. 

## Overview

Email spam remains a persistent issue in modern communication, with spam emails often inundating inboxes and posing security risks to users. The Email Spam Classifier aims to mitigate this problem by automatically identifying and filtering out spam emails, thereby enhancing the efficiency of email management and reducing the risk of falling victim to phishing attacks or malicious content.


## Data Preprocessing

Prepare data for analysis: handle missing values, encode categorical data, scale features, perform feature engineering, split into train-test sets, and normalize data. Ensure data is in a suitable format for machine learning algorithms.

The following steps outline the data preprocessing procedure:

1. **Convert to Lowercase:** The text is converted to lowercase to ensure consistency in text processing.

2. **Tokenization:** The text is tokenized into individual words using the NLTK `word_tokenize` function.

3. **Remove Punctuation:** Punctuation marks are removed from the tokenized text to focus on meaningful words.

4. **Remove Stopwords:** Common stopwords, such as "is," "the," and "and," are removed from the text using NLTK's list of English stopwords.

5. **Stemming:** The remaining words are stemmed to their root form using the Porter stemming algorithm provided by NLTK's `PorterStemmer`.

6. **Join Tokens:** Finally, the preprocessed tokens are joined back into a single string, ready to be passed into the `transform_text` function for further transformation.

By following these preprocessing steps, the text data is cleaned and prepared for the subsequent transformation process, enabling effective analysis and modeling.

![graphs](https://github.com/codewithpiyushh/ML-Crate/assets/154052068/d66c0f06-6f8c-46e1-a203-6d3fb75bdaac)


## Word cloud 
![wordcloud-1](https://github.com/codewithpiyushh/ML-Crate/assets/154052068/c19e32b1-8126-45ac-a5d2-396c958b4821)
![wordcloud-2](https://github.com/codewithpiyushh/ML-Crate/assets/154052068/57c8e07f-30f9-4cf9-8bb4-a59486b25f5d)


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

![model-accuracy](https://github.com/codewithpiyushh/ML-Crate/assets/154052068/6363471b-e024-4c4f-8b32-f5a610b21199)

#### Determining the Best Model
To determine the best model among the trained classifiers for the email spam classifier, we consider both the accuracy score and the precision.

Accuracy Score: We evaluate the models based on their accuracy scores on the test dataset. A higher accuracy score indicates that the model predicts spam and non-spam emails more accurately.

AUC-ROC: Additionally, we assess the models using the Area Under the Receiver Operating Characteristic curve (AUC-ROC) value. A higher AUC-ROC value signifies better overall performance in distinguishing between spam and non-spam emails, considering both sensitivity and specificity.

By comparing the accuracy scores and AUC-ROC values of different models, we can identify the most effective model for classifying emails as spam or non-spam. Typically, the model with the highest accuracy score and AUC-ROC value is selected as the best-performing model for deployment.
