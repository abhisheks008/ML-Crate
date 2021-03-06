## World Mortality Rate Analysis and Prediction
### Goal: Perform EDA and Predictive Analysis on the World Mortality datasets. 

### Datasets:
Download the dataset through given link: https://www.kaggle.com/datasets/navinmundhra/world-mortality

### Description
The datasets contain the mortality rates of Adults and Infants. Also they have a brief numbers about:
1. Maternal mortality rate.
2. Infant Mortality rate.
3. Neonatal mortality rates (babies that die within 28 days of birth).

### Techniques performed on the dataset:
1. First cleaned each dataset
2. Described the general information about ht
3. Then filtered information from the columns
4. Converted the datatype of each column necessary
5. Performed visualization like:
      1. Bar plot
      2. Normal distribution
      3. Scatter plot
      4. Box plot

6. Treated the outliers if necessary
8. Then encoded the categorical variables
9. Separated the training and test variables
10. Implemented the Regressor and Classifier models
11. Calculated the evaluation metrics
12. Vislualized the stability using Normal Distribution
13. Dumped the models with a high training score

> Prepared the EDA reports for each dataset
 
### Models used:
1. Linear Regression
2. Decision Tree Regresor
3. Random Forest Regressor
4. K-Nearest Neighbors Regressor
5. Decision Tree Classifier
6. Random Forest Classifier

### Visuals:
#### Heatmap
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/World%20Mortality%20Rate%20Analysis%20and%20Prediction/Images/Heatmap.png"/>

#### Normal distribution
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/World%20Mortality%20Rate%20Analysis%20and%20Prediction/Images/Per%20year%20distribution%20of%20mortality.png"/>

#### Box plot 
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/World%20Mortality%20Rate%20Analysis%20and%20Prediction/Images/Box%20plot.png"/>

#### Normal distribution to test model stability
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/World%20Mortality%20Rate%20Analysis%20and%20Prediction/Images/ML%20algorithm%20application%20distribution%20plot.png"/>


### Libraries used
1. Pandas: Data reading, filtering, analysis and modelling
2. Pandas Profiling: Prepare Exploratory Data Analysis Reports (https://anaconda.org/conda-forge/pandas-profiling)
3. Numpy: For scinetific computation
4. Scikit Learn: To implement various ML models
5. Seaborn: For advanced visualizations
6. Matplotlib: For linear and discrete visualizations

## Conclusion
### Conclusion for Adult Mortality:
#### Thus while implementing the model, we have derieved the following insights:
#### 1. The Linear Regression model's evaluation metrics are <u>very much irrelevant</u> as compared to other models.
#### 2. The RandomForestRegressor is the best fit model as the <u>*evaluation metrics and training score is excellent.*</u>
#### 3. Distribution plot also derieves the stability of the model. 
#### 4. From the predictions we can conclude that in the upcoming years the mortality rates of both the genders will reduce to a greater extent


### Conclusion for Maternal Mortality:
#### Thus while implementing the models, we have derieved the following insights:
#### 1. The KNeighbors Classifier model's evaluation metrics are <u>very much irrelevant</u> as compared to other models.
#### 2. The DecisionTree Regressor is the best fit model as the <u>*evaluation metrics and training score is excellent.*</u>
#### 3. Distribution plot also derieves the stability of each model. 
#### 4. From the predictions we can conclude that Maternal Mortality Ratio is getting low as compared to previous times. This is a good result.


### Conclusion for number of deaths in thousand:
#### Thus while implementing the models, we have derieved the following insights:
#### 1. The Random Forest regressor model's evaluation metrics are <u>very much irrelevant</u> but training score is good.
#### 2. The linear Regression is the best fit model for all three variables (Both genders infants (1-5), Both genders infants, neonatal deaths) as the <u>*evaluation metrics and training score is excellent.*</u>
#### 3. Distribution plots of Random forest are somewhat unstable while other two algorithms show a greater stability.
#### 4. From the predictions we can conclude that infants that are between 0 and 1 have shown a satisfactory survival capacity as compared to previous times. The neonatal deaths (per thousands) seem to have exceptionally decreased. 


### Conclusion for Probability of dying per thousand live births:
#### Thus while implementing the models, we have derieved the following insights:
#### 1. All the three models are best fit model for all three variables (Both genders infants (1-5), Both genders infants, neonatal deaths) as the <u>*evaluation metrics and training score is excellent.*</u>
#### 3. Distribution plots of Random forest are somewhat unstable while other two algorithms show a greater stability.
#### 4. From the predictions we can conclude that infants that are between 0 and 1 have shown a satisfactory survival capacity as compared to previous times. The neonatal deaths (per thousands) seem to have exceptionally decreased. 

> Through the predictive analysis can say that the mortality rates have linearly decreased with years of time. 








