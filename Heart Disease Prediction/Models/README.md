
  

# HEART DISEASE PREDICTION

  

## GOAL

  
Implementing classification models that can be used to predict the likelihood of a heart disease.


## DATASET

  
https://www.kaggle.com/rishidamarla/heart-disease-prediction

This data comes from the University of California Irvine's Machine Learning Repository.
  

## DESCRIPTION
  
The aim is to use this dataset to predict which patients are most likely to suffer from a heart disease in the near future using the features given.

## WORK DONE

* Analyzed the data, searched for missing values, seperated categorical and continous data.
* Performed Exploratory Data Analysis, wherein, I plotted count plots for categorical data and bar plots and distribution plot for continuous data with respect to values of Heart Disease ('Presence' or 'Absence'). Apart from that, a correlation heatmap was also plotted.
* Encoded categorical data and scaled continuous data.
* Split the dataset into Train and Test data.
* Trained model with the following algorithms:
	* Logistic Regression
	* Naive Bayes Classifier
	* Support Vector Classifier
	* KNN Classifier
        * Decision Tree Classifier
        * Random Forest Classifier
        * XGBoost Classifier
* Evaluated the accuracies of models, visualised them and stored them in a dataframe.
* Also evaluated the performance of the model with highest accuracy using confusion matrix and classification report.
  

## MODELS USED

1. **Logistic Regression** - Logistic regression is a machine learning algorithm for classification. In this algorithm, the probabilities describing the possible outcomes of a single trial are modelled using a logistic function. It is most useful for understanding the influence of several independent variables on a single outcome variable.
2. **Naive Bayes Classifier** - Naive Bayes algorithm based on Bayes’ theorem with the assumption of independence between every pair of features. This algorithm requires a small amount of training data to estimate the necessary parameters. Naive Bayes classifiers are extremely fast compared to more sophisticated methods.
3. **Support Vector Classifier** - Support vector machine is a representation of the training data as points in space separated into categories by a clear gap that is as wide as possible. New examples are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall. It is effective in high dimensional spaces and uses a subset of training points in the decision function, so it is also memory efficient.
4. **K-nearest neighbors Classifier** - It is a simple algorithm to understand and can be used for classification analysis. Classification is computed from a simple majority vote of the K nearest neighbours of each point. This algorithm is simple to implement, robust to noisy training data, and effective if training data is large.
5. **Decision Tree Classifier** - Given a data of attributes together with its classes, a decision tree produces a sequence of rules that can be used to classify the data. Decision Tree is simple to understand and visualise, requires little data preparation, and can handle both numerical and categorical data.
6. **Random Forest Classifier** - Random forest classifier fits a number of decision trees on various sub-samples of datasets and uses average to improve the predictive accuracy of the model and controls over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement.  It results in reduction in over-fitting and random forest classifier is more accurate than decision trees in most cases.
7. **XGBoost Classifier** - XGBoost is a popular gradient-boosting library for GPU training, distributed computing, and parallelization. It’s precise, it adapts well to all types of data and problems, it has excellent documentation, and overall it’s very easy to use. 



  
## LIBRARIES NEEDED

* Numpy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn

  

## ACCURACIES

| **Model** | Accuracy | 
| --- | --- |
|1. Logistic Regression | 83.950617 % | 
|2. Naive Bayes |82.716049 % |
|3. Support Vector|79.012346 %|
|4. K Nearest Neighbours|83.950617 % |
|5. Decision Tree|80.246914 % |
|6. Random Forest |85.185185 % |
|7. XGBoost |80.246914 % |



## CONCLUSION

Random Forest Classifier had the highest accuracy out of all the others, followed by KNN and Logistic Regression. Through this project, I learned how to apply various classification algorithms and analyse their performance by using confusion matrix and classification report.
Heart disease is one of the leadinng causes of death in the world. This dataset and model can be used and further improved by healthcare industry to prevent the risks of of having a heart attack or stroke.

## CONTRIBUTED BY

*Shivangi Sehgal*
