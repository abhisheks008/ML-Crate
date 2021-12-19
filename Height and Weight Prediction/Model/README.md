
  

# HEIGHT AND WEIGHT PREDICTION

  

## GOAL

  
Implementing regression models that will be used for predicting the weight of a person using their height.

  

## DATASET

  
http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights

The data was simulated based on a 1993 by a Growth Survey of 25,000 children from birth to 18 years of age recruited from Maternal and Child Health Centres (MCHC) and schools.

  

## DESCRIPTION
  
The aim is to build a predictive model for determining the weight of a person from their height.

## WORK DONE

* Analyzed the data, searched for missing values, plotted the relationship between variables, and detected outliers.
* Split the dataset into Train and Test data.
* Trained model with the following algorithms:
	* Linear Regression
	* GradientBoosting Regression
	* Support Vector Regression
	* KNN Regression
* Evaluated the accuracy of the model from the R squared scores and chose RMSE as an error metric.
* Linear Regression had the highest accuracy out of all the others. However, all the models roughly have the same accuracy.

  

## MODELS USED

1. **Linear Regression** - It is the simplest form of regression. However, it is based on the assumption that the relationship between dependent and independt variable is linear.
2. **GradientBoosting Regression** - Gradient boosting is one of the boosting algorithms which is used to minimize bias error of the model. GB regressor uses MSE as cost function.
3. **Support Vector Regression** - It is also a regression algorithm, but unlike other regression models that try to minimize the error between the actual and predicted value, SVR tries to fit the best line within a threshold value.
4. **K-nearest neighbors Regression** - It is a simple algorithm to understand and can be used for regression analysis. KNN algorithm uses feature similarity to predict the values of new datapoints which further means that the new data point will be assigned a value based on how closely it matches the points in the training set.

  
## LIBRARIES NEEDED

* Numpy
* Pandas
* Matplotlib
* scikit-learn

  

## ACCURACIES

| **Model** | Accuracy | 
| ---| --- |
|1. Linear Regression | 24% | 
|2. GradientBoosting Regression | 23.82% |
|3. Support Vector Regression | 23.95% | 
|4. KNN Regression| 23.45%|


## CONCLUSION

Finally, through this project, I learned how to apply various regression algorithms and analyse their performance by evaluating errors. This dataset can further be used to gain insights about several health parameters such as BMI, etc.

## CONTRIBUTED BY

*Shivangi Sehgal*
