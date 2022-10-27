

Soil Moisture Prediction

GOAL

Prediction of soil moisture, create a prediction model which will predict the quality of moisture in soil.

DATASET

https://www.kaggle.com/amirmohammdjalili/soil-moisture-dataset

DESCRIPTION

This dataset is manually collected from observations. It helps us to build machine learning models to predict the soil moisture. This dataset consists of 12 independent variables ie Year, Month, Day, Hour, Minute, Second, Moisture0, Moisture1, Moisture2, Moisture3, Moisture4, Irrgation .Generally, the Grade or Quality of the soil moisture depends on these parameters. These parameters play a vital role in the predictive analysis of the milk.

WHAT I HAD DONE

-> Importing the libraries

-> Loaded the dataset

Preprocessing of the dataset:

-> Changed the Grade quality using Excel to create all numeric values.

-> Knowing some of the statistical measures information

-> Visualizing the data

-> Correlation

-> Splitting the dataset

-> Training the data

-> Models used: - SVM- Decision Tree- Linear Regression

-> Evaluation of the model

-> Predicting the output of new data from the model having the high accuracy

MODELS USED

SVC: The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a "best fit" hyperplane that divides, or categorizes, your data. From there, after getting the hyperplane, you can then feed some features to your classifier to see what the "predicted" class is. Decision Tree: Decision Tree is the most powerful and popular tool for classification and prediction. A Decision tree is a flowchart-like tree structure, where each internal node denotes a test on an attribute, each branch represents an outcome of the test, and each leaf node (terminal node) holds a class label. Linear regression performs the task to predict a dependent variable value (y) based on a given independent variable (x). So, this regression technique finds out a linear relationship between x (input) and y(output).


LIBRARIES NEEDED

pandas matplotlib seaborn sklearn

Exploaratory Data Analysis


![alt text](https://github.com/Var69/ML-Crate/blob/main/Soil%20Moisture%20Prediction/Images/boxplot.png)

![alt text](https://github.com/Var69/ML-Crate/blob/main/Soil%20Moisture%20Prediction/Images/graph.png)


Correlation:

![alt text](https://github.com/Var69/ML-Crate/blob/main/Soil%20Moisture%20Prediction/Images/heatmap.png)

ACCURACIES

SVC: Accuracy: 99.3%

![alt text](https://github.com/Var69/ML-Crate/blob/main/Soil%20Moisture%20Prediction/Images/svm.png)

Decision Tree: 99.8%

![alt text](https://github.com/Var69/ML-Crate/blob/main/Soil%20Moisture%20Prediction/Images/decisiontree.png)

Linear regression: 0.6%

![alt text](https://github.com/Var69/ML-Crate/blob/main/Soil%20Moisture%20Prediction/Images/linearregression.png)

CONCLUSION

Downloaded the dataset from kaggle, loading the required libraries, Data Pre-Processing, Splitting of data, building the models, testing thier accuracies and finalizing the model based on accuracy. I have used three models to train the data starting with Linear Regression, then SVM and after that Decision Tree. Decision Tree is used to predict the soil moisture quality with an accuracy over 99%

YOUR NAME

Varun Nair

GitHub: https://github.com/Var69
