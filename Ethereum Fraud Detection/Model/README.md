
## Project Title - Ethereum Fraud Detection

**Aim of the Project**  

This project will Create a ML model which will detect the real/fake transactions of Eth..

**Dataset**  

https://www.kaggle.com/vagifa/ethereum-frauddetection-dataset

**Approach**

Performed Exploratory Data Analysis on the dataset and Used 3-4 Classification Algorithmns to implement the models and Compared all the algorithms to find out the best fitted one.

**Steps Involved**

- Import Required libraries.
- Load the dataset.
- Performing EDA on the data like Outlier Treatment, Handling Missing values.
- Identifying Input and Target columns from the dataset.
- Separating Numerical and Categorical columns.
- Scaling the numeric columns and Encoding the categorical columns.
- Splitting the Data into Training and Testing dataset.
- Performed PCA for Dimensionality Reduction.
- Model Building: We use four algorithms to build the models.
    - Logistic Regression
    - Decision Tree Classifier
    - Random Forest Classifier
    - GradientBoostingClassifier
- Predicting on Test Data. 
After fitting these models with the data, we analyze the model using metric accuracy_score and compare with all of the algorithms listed above.

**Data Visualization**   

_Distribution of Data in Flag Column._

![](https://github.com/jahnavibattu02/ML-Crate/blob/main/Ethereum%20Fraud%20Detection/Images/flag.png)

_totalTransactions Vs ReceivedTnx_

![](https://github.com/jahnavibattu02/ML-Crate/blob/main/Ethereum%20Fraud%20Detection/Images/totalTransactions-ReceivedTnx.png)

_Correlation plot of the data._

![](https://github.com/jahnavibattu02/ML-Crate/blob/main/Ethereum%20Fraud%20Detection/Images/correlation.png)

_Confusion Matrix (Gradient Boosting Classifier as model)_ 

![](https://github.com/jahnavibattu02/ML-Crate/blob/main/Ethereum%20Fraud%20Detection/Images/confusion%20matrix.png)

**Accuracy Scores**

- Logistic Regression  =  0.9852
- Decision Tree Classifier  = 0.9807
- Random Forest Classifier  = 0.9847
- GradientBoostingClassifier = 0.9862

**Conclusion:**

Among all the models listed above, we can see that GradientBoostingClassifierr have more Accuray Score of ```98.6%```. We can conclude that it is the best fitted model.

**Language and Libraries Used:**

Python Programmming is used.
Libraries like Numpy, Pandas, Seaborn, Matplotlib, Scikit-Learn are used.

#
Code Contributed by Jahnavi Pravaleeka Battu
