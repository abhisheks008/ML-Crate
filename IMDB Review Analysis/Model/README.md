
  

# IMDB Review Analysis

  

## GOAL

  
Perform Sentiment analysis on the data to see the statistics of what type of movie do users like. Sentiment analysis is the process of analysing the textual data and identifying the emotion of the user, Positive or Negative.


## DATASET

  
http://ai.stanford.edu/~amaas/data/sentiment/  

## DESCRIPTION
  
Perform Sentiment analysis on the data to see the statistics of what type of movie do users like. Sentiment analysis is the process of analysing the textual data and identifying the emotion of the user, Positive or Negative.

## WORK DONE

* Analyzed the data, searched for missing values, seperated categorical and continous data.
* Removed unnecessary columns
* Converting some column data to Meaning full numerical data
* Grouping and Dealing with lots of Object Type of Data
* Build Relation Between PolicyType with other Two Column
* Recreated BasePolicy Column and compared it with PolicyType and which bought some insightful results
* Provided Desired Values to Data which was available in Range.
* Performed Exploratory Data Analysis
* Split the dataset into Train and Test data.
* Trained model with the following algorithms:
	* Support Vector Classifier
	* Kernel RBF
	* KNN Classifier
* Also evaluated the performance of the model with highest accuracy.


## MODELS USED

1. **Support Vector Classifier** - Support vector machine is a representation of the training data as points in space separated into categories by a clear gap that is as wide as possible. New examples are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall. It is effective in high dimensional spaces and uses a subset of training points in the decision function, so it is also memory efficient.
2. **RBF** - Radial basis function (RBF) networks are a commonly used type of artificial neural network for function approximation problems. Radial basis function networks are distinguished from other neural networks due to their universal approximation and faster learning speed.
3. **K-nearest neighbors Classifier** - It is a simple algorithm to understand and can be used for classification analysis. Classification is computed from a simple majority vote of the K nearest neighbours of each point. This algorithm is simple to implement, robust to noisy training data, and effective if training data is large.



  
## LIBRARIES NEEDED

* Numpy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Plotly

  

## ACCURACIES

| **Model** | Accuracy | 
| --- | --- |
|1. SVM Classifier |54.791 % |
|2. Kernel RBF |60.22 % |
|3. K Nearest Neighbours|60.24 % |



## CONCLUSION

while using kernel as linear the accuracy has increased to 0.02% which is almost negligible. Accuracy attained by kernel RBF is 60.24%.

## CONTRIBUTED BY

*Shrikrushna Bhagwat*
