# Lottery Prediction Model

This repository contains the code for a lottery prediction model. The model is trained on a dataset downloaded from Kaggle and uses various machine learning algorithms such as RandomForestRegressor, LogisticRegression, Support Vector Regression (SVR), and TensorFlow.

## Dataset

The dataset used for training the model can be found on Kaggle. It has undergone exploratory data analysis (EDA) to understand its structure and characteristics.
`https://www.kaggle.com/datasets/muhammadzain010/lottery-ticket-prediction-based-on-history`

## Model Training

The model is trained using the following algorithms:

- RandomForestRegressor: This algorithm is used to build a regression model based on random decision trees.
- LogisticRegression: This algorithm is used for binary classification tasks.
- SVR: Support Vector Regression is used to build a regression model based on support vector machines.
- TensorFlow: TensorFlow is used to build and train a deep learning model for lottery prediction.

## Usage

To use the lottery prediction model, follow these steps:

1. Clone the repository to your local machine.
   `git clone filepath`
2. Install the required dependencies mentioned in the `requirements.txt` file.
3. Run the appropriate script or notebook to train the model using the desired algorithm.
4. Once the model is trained, you can use it to make predictions on new lottery data.

## Conclusion

<br /> There were some `obj` columns which were converted to `int`.
<br /> For categorical feature the missing values were not large so can be replaced with most_frequent_ones or Median.
<br /> The project concluded with the use of the different models to predict the lottery.
