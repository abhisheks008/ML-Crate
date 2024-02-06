<p align="center">
  <img src="https://storage.googleapis.com/kaggle-competitions/kaggle/3342/media/salary%20prediction%20engine%20v2.png">
</p>


# Salary Prediction Project
## Define problem
In job posting websites like Glassdoor, LinkedIn, and Indeed, each post lists its required skills, education, qualification, experience, ..., and of course, salary. 
* For applicants, instead of accepting the salary employer proposed, having an estimator predicting the salary based on job requirements or skills acquired gives confidence of their worth for further negotiation. 
* For employer, an salary estimator suggests a market standard so employers can propose a reasonable salary to attract more applicates. 

The goal of this project is to create a model that estimates a salary given jobs with various of requirements.

## Deliverables
- SalaryPredictions.zip: contains data files

- ML_approach/: contains files using machine learning approach
- ML_approach/Salary_Prediction_Analysis.ipynb: notebook includes detailed data extraction, data loading, data wrangling, data analysis, feature engineering, and model training.
- ML_approach/salary_prediction_final_code.py: cleaned code in Python
- ML_approach/test_salaries_prediction.csv: salary prediction of test dataset

- DNN_approach/: contains files using deep neural network approach
- DNN_approach/salary_prediction_nn.py: cleaned code in Python
- DNN_approach/test_salaries_prediction_dnn.csv: salary prediction of test dataset
- DNN_approach/best-weight-batch_size_1000-epochs_###.hdf5: weight of the best model with least loss
- DNN_approach/loss-batch_size_1000-epochs_###.png: plot of history of loss and validation loss during training

## Approach
1. Data loading
    * train_features.csv file contains training set features
    * train_salaries.csv file contains training set target, salary
    * test_features.csv file contains testing set features

2. Data scrubbing
    * Remove incomplete instances
    * Remove duplicated instances
    * Remove invalid instnaces
        * Salary <= 0
        * yearsExperience < 0
        * milesFromMetropolis < 0

3. Exploratory Data Analysis (EDA)

Explore data, find distribution of each features and categories, and visualize data to find embedded pattern(s).

<img src="images/eda_boxplots.png">

4. Encoding

Convert categories to distinguishable numerical values using category average salary
<img src="images/encoder_corr_matrix.png">

5. Feature engineering

Not all features are independent, thus adding interaction features provides more information on dependencies between features. Generate new features based on IQR rule, including group min, first quantile, median, mean, third quantile, upper bound for outliers, and max.
<img src="images/feat_eng_corr_matrix.png">

6. Modeling

For mechine learning approach: use default 5-fold cross validate and MSE to select best model.
  * Establish baseline: use average salary for each industry as baseline model and measure MSE
      Model | MSE
      ------------ | -------------
      Baseline | 1367.123
      
  * Try vanilla models (use default hyperparameter values) and select couple good models. In this case I selected:
  
      Model | MSE
      ------------ | -------------
      LinearRegression | 351.652
      RandomForestRegressor | 337.152
      GradientBoostingRegressor | 328.327
      ExtraTreeRegressor | 343.122

  * Try training with standardized data: no obvious improvement
  
      Model | MSE
      ------------ | -------------
      Scaled LinearRegression | 351.652
      Scaled RandomForestRegressor | 337.228
      Scaled GradientBoostingRegressor | 328.327
      Scaled ExtraTreeRegressor | 343.046
      
  * Tune model: tune best 2 models
  
      Model | Hyperparameter | Best MSE
      ------------ | ------------- | -------------
      RandomForestRegressor | n_estimators=200, max_depth=15, max_features=8 | 313.741
      GradientBoostingRegressor | n_estimators=100, loss='ls', max_depth=8 | 306.792

For neural network approach: use simple Dense layers and tune network topology. The best result is MSE = 313

The best model is GradientBoostingRegressor(n_estimators=100, loss='ls', max_depth=8) and the feature importance is:

Feature | Feature Importance
------------ | -------------
companyId | 0.000221
jobType | 0.003601
degree | 0.002906
major | 0.001065
industry | 0.002077
**yearsExperience** | **0.151995**
**milesFromMetropolis** | **0.104973**
CJDMI_min | 0.008940
CJDMI_Q1 | 0.032568
**CJDMI_mean** | **0.658095**
CJDMI_median | 0.006771
CJDMI_Q3 | 0.008138
CJDMI_upper | 0.001924
CJDMI_max | 0.016725

7. Deploying

Use best model to predict test set.
