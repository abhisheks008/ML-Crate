**Milk Quality Prediction**

**GOAL**

Prediction of milk quality, create a prediction model which will predict the goodness of the milk.

**DATASET**

https://www.kaggle.com/datasets/cpluzshrijayan/milkquali

**DESCRIPTION**

This dataset is manually collected from observations. It helps us to build machine learning models to predict the quality of milk.
This dataset consists of 7 independent variables ie pH, Temperature, Taste, Odor, Fat, Turbidity, and Color.
Generally, the Grade or Quality of the milk depends on these parameters. These parameters play a vital role in the predictive analysis of the milk.

**WHAT I HAD DONE**

-> Importing the libraries

-> Loaded the dataset

Preprocessing of the dataset:

-> Changed the Grade quality using Excel to create all numeric values.


-> Knowing some of the statistical measures information

-> Visualizing the data

-> Correlation

-> Splitting the dataset

-> Training the data

-> Models used: - SVM- Decision Tree- Naive Bayes

-> Evaluation of the model

-> Predicting the output of new data from the model having the high accuracy

**MODELS USED**

SVC: The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a "best fit" hyperplane that divides, or categorizes, your data. From there, after getting the hyperplane, you can then feed some features to your classifier to see what the "predicted" class is.
Decision Tree: Decision Tree is the most powerful and popular tool for classification and prediction. A Decision tree is a flowchart-like tree structure, where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node (terminal node) holds a class label. 
Naive Bayes: Naïve Bayes algorithm is a supervised learning algorithm, which is based on Bayes theorem and used for solving classification problems.
It is mainly used in text classification that includes a high-dimensional training dataset.
Naïve Bayes Classifier is one of the simple and most effective Classification algorithms which helps in building the fast machine learning models that can make quick predictions.
It is a probabilistic classifier, which means it predicts on the basis of the probability of an object.
Some popular examples of Naïve Bayes Algorithm are spam filtration, Sentimental analysis, and classifying articles.


**LIBRARIES NEEDED**

pandas
matplotlib
seaborn
sklearn

**Exploaratory Data Analysis**

![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/1.JPG)
![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/2.JPG)
![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/3.JPG)
![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/4.JPG)
![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/5.JPG)
![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/6.JPG)
![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/7.JPG)

Correlation:

![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/Correlation_Matrix.JPG)


**ACCURACIES**

SVC:
Accuracy: 91.17%


![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/SVM_Result.JPG)


Decision Tree: 83.8%

![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/Decision%20Tree_Result.JPG)


Naive Bayes: 67%


![alt text](https://github.com/shubhammore45/ML-Crate/blob/main/Milk%20Quality%20Prediction/Images/Naive%20Bayes_Result.JPG)


CONCLUSION

Downloaded the dataset from kaggle, loading the required libraries, Data Pre-Processing, Splitting of data, building the models, testing thier accuracies and finilizing the model based on accuracy.
I have used three models to train the data starting with SVC, then Decision treer and after that Naive Bayes. 
SVC is used to predict the milk quality with an accuracy over 90%

**YOUR NAME**

Shubham More

GitHub: https://github.com/shubhammore45
