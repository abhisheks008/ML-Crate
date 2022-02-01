### Project Title
Advertisement Click Prediction
### Aim
Predict the clicks on the advertisement depending on different attributes and user inputs of the dataset.
### Dataset
https://www.kaggle.com/jahnveenarang/cvdcvd-vd
### Approach
Initially Exploratory Data Analysis and Data Visulaization is performed on the dataset. Then by applying various algorithms on the dataset, we are going to predict whether the user will click on the advertisement or not. Finally the accuracies of all algorithms are compared and found the best fitted model.
### Steps Involved
- All the necessary libraries are imported
- Performing EDA on the data to understand it
- Data Visualization to the visualize the data and get meaningful insights
- Correlation of all features are found to understand the relationship between each feature
- Categorical features are converted into numerical features using feature mapping
- The dataset is split into training and test data and scaled
- Model Building:
      We use four algorithms to build the models
     - XGBoost Classifier 
     - Random Forest Classifier
     - Gradient Boosting 
     - Multi Layer Perceptron
- After fitting these models, we analyze the confusion matrix and compare the accuracies of all algorithms.
### Accuracies
-	XGBoost Classifier - 92%
-	RandomForest - 90%
-	Gradient Boosting -	90%
-	Multi-Layer Perceptron - 87%
<img src
### Language Used - Python
### Libraries Used - pandas, seaborn, numpy, matplotlib
### Conclusion
Among all the models, XGBoost Classifier model gave almost 92% accuracy and it is the best fitted model.

Code contributed by SNEGA S

