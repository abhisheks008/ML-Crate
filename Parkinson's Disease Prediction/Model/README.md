**Parkinson's Disease Prediction**

**GOAL**

The aim of the project is to build a model which would predict whether a person has the parkinson's disease

**DATASET**

The dataset was taken from the UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/parkinsons

**DESCRIPTION**

In this project, we compare the accuracies of different models to predict the parkinson's disease

**WHAT I HAD DONE**

Steps followed:
* Downloaded the dataset from the UCI Repository
* Checked for null values and performed exploratory data analysis
* Built models using the following algorithms: XGboost, SVM, KNN, Random Forest
* Compared the accuracies
* Then performed cross validation on all the algorithms to see if the accuraries imrpove

**MODELS USED**

XGboost: XGBoost is an efficient and easy to use algorithm which delivers high performance and accuracy as compared to other algorithms. It prevents the model from overfitting and is much faster as it uses multiple CPU cores

SVM: SVM (Support Vector Machine) classifies the data using hyperplane which acts like a decision boundary between different classes, it is able to handle High dimensional data too and this proves to be a great help taking into account its usage and application

KNN: KNN is called Lazy Learner (Instance based learning). It does not learn anything in the training period,  stores the training dataset and learns from it only at the time of making real time predictions. This makes the KNN algorithm much faster than other algorithms that require training

Random Forest: Random Forest is a powerful algorithm in Machine Learning. It is based on the Ensemble Learning technique (bagging). It creates as many trees on the subset of the data and combines the output of all the trees. In this way it reduces overfitting problem in decision trees and also reduces the variance and therefore improves the accuracy.

**LIBRARIES NEEDED**

* Pandas
* Matplotlib
* Seaborn
* Numpy
* Sklearn
* xgboost


**ACCURACIES**

* XGboost: 94.87%
* SVM: 84.6%
* SVM with cross validation: 87.2%
* KNN: 84.6%
* KNN with cross validation: 92.3%
* Random Forest: 92.3%


**CONCLUSION**

From this project we conclude that XGboost has the highest accuracy among all the four algorithms, followed by Random forest and then SVM and KNN. We even used kfold cross validation to improve accuracies. XGboost and Random forest did not improve its accuracies but there was a significant improve in SVM and KNN (from 85% to 87% and 92% respectivey) 

**Contribution by**

Karishni Mehta
Github: https://github.com/karishni
