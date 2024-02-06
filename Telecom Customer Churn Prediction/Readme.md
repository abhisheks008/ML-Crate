## Telecom Companies Customer Analysis and Prediction
### Goal: To analyze the behavior of cutomers why they leave the company and then make predicitons for specific reasons for a clear idea
### Dataset link: 
https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics

### Techniques used:
1. Data Cleaning
2. Data preprocessing
3. Data filtering
4. Data Visualization
5. Model building 
6. Pickling the models

## Libraries used:
1. Pandas - for data wrangling
2. Pandas-profiling - To prepare the EDA reports
3. Pickle: To pickle/store the ML models
4. Numpy - for numerical computations 
5. Scikit learn - used to implement Machine Learning models
6. Seaborn - used for advanced data visualizations
7. Matplotlib - for plotting the mean differences and small plots
8. Warnings - To supress and unnecessary warnings

### Plot types for dataset:
1. Histogram
2. Box plot
3. Distribution
4. Heatmap

## ML models implemented:
1. Linear regression
2. Decision tree Regressor
3. Random forest Regressor
4. Decision Tree Classifier
5. Random Forest Classifier

### Visualizations for the model
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Telecom%20Customer%20Churn%20Prediction/Images/Screenshot%20(39).png"/>
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Telecom%20Customer%20Churn%20Prediction/Images/Screenshot%20(40).png"/>
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Telecom%20Customer%20Churn%20Prediction/Images/Screenshot%20(41).png"/>
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Telecom%20Customer%20Churn%20Prediction/Images/Screenshot%20(42).png"/>
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Telecom%20Customer%20Churn%20Prediction/Images/Screenshot%20(43).png"/>
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Telecom%20Customer%20Churn%20Prediction/Images/Screenshot%20(44).png"/>

## Conclusion obtained
#### The analysis of the whole dataset with respect to some parameters says that customers who left the telecom service show a very close similarity for the three reasons that we analyzed. When we plot the distribution of the reasons and predictions then we can say that customers are likely to show disagreements from companies that have
#### 1. A high extra data charges
#### 2. Slower download and upload speeds 
#### 3. Competitor company preoviding a better sevice. 

### Best models:
#### For the reason 1 analysis: The Decision Tree Regressor model is the best fit model as it gives the minimum errors as well as very high accuracy.
#### For the reason 2 analysis: Decision Tree Regressor as well as Random Forest Regressor both show the optimum growth towards the predictive analysis as the training scores and evaluation metrics are giving desireable insight.
#### For the reason 3 analysis: Random Forest Classofoer and Decision Tree classifier are the best fit models due to their high accuracy and low error values in evaluation metrics.
