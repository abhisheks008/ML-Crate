**Wine Quality Prediction**

**GOAL**

Prediction of wine quality, the quality is predicted in order to maintain the health of the consumers and also maintai the health rate of the world/ country

**DATASET**

https://archive.ics.uci.edu/ml/datasets/wine+quality

**DESCRIPTION**

This datasets is related to red variants of the Portuguese "Vinho Verde" wine.The dataset describes the amount of various chemicals present in wine and their effect on it's quality. The datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).Your task is to predict the quality of wine using the given data.

**WHAT I HAD DONE**

-> Importing the libraries

-> Loaded the dataset

Preprocessing of the dataset:

-> Knowing some of the statistical measures information

-> Visualizing the data

-> Correlation

-> Splitting the dataset

-> Training the data 

-> Models used:
    - Random forest classifier
    - SGD classifier
    - SVC

-> Evaluation of the model

-> Predicting the output of new data from the model having the high accuracy


**MODELS USED**
- Random forest classifier: Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset.
- SGD classifier: Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fitting linear classifiers and regressors under convex loss functions such as (linear) Support Vector Machines and Logistic Regression.
- SVC: The objective of a Linear SVC (Support Vector Classifier) is to fit to the data you provide, returning a "best fit" hyperplane that divides, or categorizes, your data. From there, after getting the hyperplane, you can then feed some features to your classifier to see what the "predicted" class is.

**LIBRARIES NEEDED**

- pandas
- matplotlib
- seaborn
- sklearn

**ACCURACIES**
- Random forest classifier: 
- Before GridSearchCV: 88%

![image](https://user-images.githubusercontent.com/79050917/146384139-378002f4-f973-43d2-81b7-79ab116e81c1.png)

- After GridSearchCV: 90% 

![image](https://user-images.githubusercontent.com/79050917/146384557-6a032ac8-b30a-41c8-852f-db65e4629a3a.png)

- SGD classifier: 84%

![image](https://user-images.githubusercontent.com/79050917/146384197-76f17146-3598-4226-845e-442aac633521.png)

- SVC: 88%

![image](https://user-images.githubusercontent.com/79050917/146384279-0152c343-0163-4f64-866a-28cf0bbff3bf.png)


**CONCLUSION**

- Downloaded the dataset from kaggle, loading the required libraries, Data Pre-Processing, Splitting of data, building the models, testing thier accuracies and finilizing the model based on accuracy.
- I have used three models to train the data starting with Randomm forest classifier, then SGD classifier and after that SVC. I have tuned the data using GirdSearchCV after that the accuracy of random forest classifier increased, this lead to finilize the random forest classifier which is having highest accuracy.
- Random forest classifier is used to predict the wine quality with an accuracy over 90%

**YOUR NAME**

Deepthi M

GitHub: https://github.com/deepthi1107

Linkedin: https://www.linkedin.com/in/deepthi-m-1107/
