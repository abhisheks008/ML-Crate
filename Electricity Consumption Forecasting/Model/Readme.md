Electricity Consumption Forecasting

GOAL

Implementtion of different algorithms like LSTM and SVM to see which gives better accuracy.

DATASET

https://drive.google.com/file/d/1DNRvzpGNdZxpbsB99bOFYmCxc1tcCnP3/view

DESCRIPTION

The main aim of the project is to make a model that helps to predict Electricity consumption prediction based on the given dataset.

WORK DONE

Analyzed the data and found insights such as correlation, missing values etc.
Selected the columns that have high correlation than other columns to be used as features.
Next trained model with algorithms with default parameters:
SVM
LSTM


SVM : SVM performs well on classification problems when size of dataset is not too large.

LIBRARIES NEEDED

Numpy
Pandas
Matplotlib
scikit-learn
xgboost
skopt
lightgbm
seaborn
ACCURACIES

Model Accuracies - LSTM- 76, SVM- 68

CONCLUSION

We investigated the data, checking for data unbalancing, visualizing the features, and understanding the relationship between different features. We then investigated two predictive models. The data was split into three parts, a train set, a validation set, and a test set. For the first five base models, we only used the train and test set.

We started with LSTM, SVM for which we obtained an accuracies of 99.90,99.94,99.95,99.94 and 99.95% respectively, when predicting the target for the test set.

We followed with an LSTM and optimizing it using Bayesian optimization and achieved AUC score (76.8) for the prediction of the test set target values.

CONTRIBUTION BY

Karan Shelke


