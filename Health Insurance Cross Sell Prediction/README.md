# Health Insurance Cross Sell Prediction
Dive into the intricacies of predicting which customers are likely to purchase additional health insurance based on their profiles. This project utilizes various machine learning models to analyze customer data and provide insights that can help insurance companies tailor their marketing strategies and improve customer engagement.
<img width="922" alt="webapp" src="https://github.com/user-attachments/assets/f5de12fa-0144-4f3f-92dd-94c652f6e49c">

## 📝 Abstract
Health Insurance Cross Sell Prediction involves using machine learning algorithms to predict whether a customer will purchase additional health insurance. This analysis provides valuable insights into customer behavior and helps insurance companies make informed decisions to optimize their marketing and sales strategies.

## 🔍 Methodology
**Importing Libraries**

- Libraries such as NumPy, Pandas, Scikit-Learn, LightGBM, XGBoost, and others are imported for data manipulation, visualization, and machine learning model building.

**Loading the Dataset**

- The dataset contains customer information with various features such as Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium, Policy_Sales_Channel, Vintage, and Response.

**Data Preprocessing**

- prepare data for analysis: handle missing values, encode categorical data, scale features, perform feature engineering, split into train-test sets, and normalize data. Ensure data is in a suitable format for machine learning algorithms.

**Training the Models**

- Each model is trained on the training dataset and evaluated using metrics such as accuracy, precision, recall, and F1 score. The models used include:
Logistic Regression
XGBoost
Naive Bayes
LightGBM
Neural Network
Ridge Classifier
SGD Classifier

**Model Performance Analysis**

- Training and validation loss and accuracy are plotted to visualize the models' performance.

**Model Prediction**

- The model is given a test dataset to check the accuracy and precision of the predictions.

**Deploy**

- Using the Streamlit library, the model is deployed for real-time prediction of customer cross-sell potential.

## Project Directory Structure
```bash
Health Insurance Cross Sell Prediction
|- Dataset
  |- dataset_view.csv
  |- dataset_review.csv
  |- README.md
|- Model
  |- Health_Insurance_Cross_Sell_Prediction.ipynb
  |- README.md
  |- model.pkl
  |- scaler.pkl
|- Web App
  |- app.py
  |- README.md
|- Images
  |- correlation.png
  |- dis_age.png
  |- distribution_response.png
  |- f1_cmp.png
  |- gender_response.png
  |- gender.png
  |- histogram.png
  |- model_cmp.png
  |- precision.png
  |- recall_cmp.png
  |- README.md
  |- webapp_run.mp4
|- requirements.txt
|- README.md
```
### How to Use
**Requirements**
- Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the `requirements.txt` file.

**Download Data**
- Download the train.csv and test.csv datasets from Kaggle or any other source mentioned in the dataset section of the project.[Kaggle](https://www.kaggle.com/competitions/playground-series-s4e7/data)

**Run the Jupyter Notebook**
- Open the provided Jupyter Notebook file and run each cell sequentially. Make sure to update any file paths or configurations as needed for your environment.

**Training and Evaluation**
- Train the models using the provided data and evaluate their performance using metrics such as accuracy, precision, recall, and F1 score.

**Interpret Results**
- Analyze the model's performance using the visualizations and metrics provided in the notebook.

## Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
