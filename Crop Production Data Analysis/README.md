
  

**CROP PRODUCTION DATA ANALYSIS**

  

**GOAL**

  
To predict a the rice yield (Kg per ha) from the dataset or to predict any crop yield.
  

**DATASET**

  

https://www.kaggle.com/datasets/zsinghrahulk/crop-production-data
  

**DESCRIPTION**

  

The main aim of the project is to make a model that helps to predict the rice yield of the state, dist by given rice field area, production (per 1000 ha).

## Visualization and EDA of different attributes:

<img alt="graph" src="./Images/statename vs Rice production.png">

<img alt="graph" src="./Images/year vs Rice production.png">

<img alt="graph" src="./Images/Rice Area vs Rice production.png">

<img alt="graph" src="./Images/Rice Area vs Rice production 3.png">


**MODELS USED**

| Model                     | MAE_test | MSE_test  | R2_test   | RMSE_test  |
|---------------------------|----------|-----------|-----------|------------|
| Random Forest Regression  | 53.82    | 15314.65  | 0.98      | 123.75     |
| XG Boost Regression       | 68.61    | 11153.18  | 0.98      | 105.60     |
| Ridge Regression          | 539.03   | 515922.37 | 0.46      | 718.27     |
| Decision Tree Regression  | 81.75    | 29353.39  | 0.96      | 171.32     |
| Lasso                     | 539.03   | 11153.18  | 0.46      | 718.27     |
| SVR                       | 729.82   | 817852.71 | 0.15      | 904.35     |
| LightGBM                  | 70.22    | 12811.94  | 0.98      | 113.18     |

  

**WORK DONE**

* Analyzed the data and found insights such as correlation, missing values etc.
* Selected the columns that have high correlation than other columns to be used as features.
* Next trained model with algorithms with default parameters:
	* Linear SVR
	* Lasso
	* Ridge
	* Decision Tree
	* Random Forest
	* XGBoost
	* LightGBM
	* SDRegressor
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
