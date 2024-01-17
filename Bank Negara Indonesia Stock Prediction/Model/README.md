
  

**BANK Negara Stock Prediction**

  

**GOAL**

  
To predict a the closing price of the bank stock prices from the dataset.
  

**DATASET**

  

https://www.kaggle.com/datasets/caesarmario/bank-negara-indonesia-stock-historical-price

  

**DESCRIPTION**

  

The main aim of the project is to make a model that helps to predict the closing price of the bank.

## Visualization and EDA of different attributes:

<img alt="graph" src="./Images/closevsopen.png">

<img alt="graph" src="./Images/stock.png">

<img alt="graph" src="./Images/bar graph of the dataset.png">

<img alt="graph" src="./Images/histrogram of the dataset.png">


**MODELS USED**

| Model                     | MAE_test | MSE_test  | R2_test   |
|---------------------------|----------|-----------|-----------|
| Random Forest Regression  | 19.47    | 866.65    | 0.99      |
| XG Boost Regression       | 24.92    | 1154.11   | 0.99      |
| Ridge Regression          | 20.81    | 701.38    | 0.99      |
| Decision Tree Regression  | 22.86    | 1374.32   | 0.99      |
| Lasso                     | 22.24    | 793.25    | 0.99      |
| SVR                       | 788.22   | 882792.81 | 0.014     |

  

**WORK DONE**

* Analyzed the data and found insights such as correlation, missing values etc.
* Selected the columns that have high correlation than other columns to be used as features. (Refer : `eda-banknote-dataset`)
* Next trained model with algorithms with default parameters:
	* Linear SVR
	* Lasso
	* Ridge
	* Decision Tree
	* Random Forest
	* XGBoost
* In this Linear SVR and performed the best with 90% accuracy.
  

**MODELS USED**

1. Logistic Regression : Logistic regression is easier to implement, interpret, and very efficient to train. It is **very fast at classifying unknown records**.
2. Linear SVM : SVM performs well on classification problems when size of dataset is not too large.
3. Random Forest : It **provides higher accuracy through cross validation**. Random forest classifier will handle the missing values and maintain the accuracy of a large proportion of data. If there are more trees, it won't allow over-fitting trees in the model.
4. XGBoost : XGBoost is **a library for developing fast and high performance gradient boosting tree models**. XGBoost achieves the best performance on a range of difficult machine learning tasks.
5. LightGBM : Light GBM is prefixed as Light because of its high speed. Light GBM can handle the large size of data and takes lower memory to run. it is so popular is because **it focuses on accuracy of results**.

**LIBRARIES NEEDED**

* Numpy
* Pandas
* Matplotlib
* scikit-learn
* xgboost
* seaborn
  
  

**CONCLUSION**

  

We investigated the data, checking for data unbalancing, visualizing the features, and understanding the relationship between different features. We then investigated two predictive models. The data was split into two parts, a train set, a test set. For the first five base models, we only used the train and test set.

We started with SVR, Decision Tree, Lasso, Ridge, Random Forrest Regressor and XGBoost Regressor for which we obtained an highest accuracy of 90%, when predicting the target for the test set.

  

**CONTRIBUTION BY**

*Pawas Pandey*
