# 🧠 End to End Email Spam Classifier

![interface](https://github.com/codewithpiyushh/ML-Crate/assets/154052068/db86a574-6e9c-47ee-bdbf-5966b8c81773)

## 📝 Abstract

Email spam classification involves automatically identifying and sorting emails into two categories: spam (unwanted messages) and ham (legitimate messages). Techniques like analyzing email content, user behavior, and machine learning models help achieve this. The goal is to keep spam out of your inbox and ensure you receive important emails .


## 🔍 Methodology

1. **Importing Libraries:**  
   - Libraries such as NumPy, Pandas, Sklearn, and others are imported for data manipulation, visualization, and Machine learning model building.

2. **Loading the Dataset:**
   - The dataset containing the multiple rows of spam or not spam message

3. **Data Preprocessing:**
   Prepare data for analysis: handle missing values, encode categorical data, scale features, perform feature engineering, split into train-test sets, and normalize data. Ensure data is in a suitable format for machine learning algorithms.

4. **Training the Models:**
   - Each model is compiled using the Support vector machines
   - The models are trained on the training dataset and evaluation is done.

5. **Model Performance Analysis:**
   - Training and validation loss and accuracy are plotted to visualize the models' performance.

6. **Model prediction:**
   - The model is then given a test dataset to check the accuracy and precision of the model with

7. **Deploy:**
   - By using the streamlit library the model is deployed


**Data and Model File Download:**
the Dataset used int the project is taken from kaggle spam Dataset
[https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset]


### Project Directory Structure

End to End Email Spam Classifier
|- Dataset
  |- spam.csv
  |- README.md
|- Images
  |- graphs
  |- interface
  |- model live recording
  |- model accuracy
  |- model precision
  |- worldcloud-1
  |- worldcloud-2
|- Model
  |- Email_Spam_Classifier2.ipynb
  |- README.md
  |- model.pkl
  |- vectorizer.pkl
|- Web App
  |- openapp.py
  |- README.md
|- requirements.txt

## 🙌 Acknowledgments

The authors would like to acknowledge the contributions of the research community in the field of Email Spam Classifier using machine learning. The open-source datasets and repositories have been instrumental in the development of this project

Citations:
[1] [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset]
[2] [https://scikit-learn.org/stable/modules/naive_bayes.html]
[3] [https://scikit-learn.org/stable/modules/svm.html]
[4] [https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html]
[5] [https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html]
[6] [https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html]


## How to Use
Requirements: Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the requirements.txt file.

Download Data: Download the spam.csv Dataset from Kaggle mentioned in the dataset section of the project.

Run the Jupyter Notebook: Open the provided Jupyter Notebook file and run each cell sequentially. Make sure to update any file paths or configurations as needed for your environment.

Training and Evaluation: Train the models using the provided data and evaluate their performance using metrics such as accuracy and loss.

Interpret Results: Analyze the model's performance using the visualizations and metrics provided in the notebook.

Feel free to reach out if you encounter any issues or need further assistance with running the notebook.
