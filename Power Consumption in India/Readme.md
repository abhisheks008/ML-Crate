# Power Consumption of each state in India - A Predictive analysis

**GOAL**

Perform exploratory data analysis and Predictive Analysis on the power consumption dataset and analyse the power consumed per year and month basis of each state

**DATASET**
https://www.kaggle.com/datasets/twinkle0705/state-wise-power-consumption-in-india

## Description
The project is a collection of all the possible statistical applications and metrics to derieve useful insights and properly visualize the use of power of various states of India. Also perform a predictive analysis on the same using month as a parameter of prediction. Below are the actions performed on the dataset.
* First imported all the necessary libraries that are listed in the libraries section.
* Viewed the dataset's head and tail column.
* Extracted the general information of the two datasets.
* Described the statistical data.
* Extracted the column names.
* Took out all the unique categorical values from the dataset.
* Converted the first column to date-time type. Then extracted the year, month and day for each state
* Performed visualizations: 
    * Histogram
    * Heat Map
    * Pair Plot
    * Box plot
    * Normal Distribution
* Compared the columns with month, year as per usage other and view their result using histogram and box plots.
* Lastly checked and treated the outliers and implemented ML models like:
    * RandomForestRegressor
    * LinearRegression
    * KNeighborsRegressor
    * DecisionTreeRegressor
    
## Performed actions:
1. Data Cleaning: 
2. Data Preprocessing
3. Data visualization
4. Data type conversion of *Date* column
5. Detecting the outliers
6. Selecting the training and testing arrays
7. Training the model
8. Making Predictions
9. Evaluating the model using MSE, RMS and MAE as metrics.

### Libraries Needed
1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn

### IDE used: Jupyter Ntebooks

## Plots

### Heatmap of the dataset parameters
Heatmap states that there is no considerable corelation between the important metrics
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Heatmap%20of%20states.png"/>

### Andhra Pradesh Power Consumption plot
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Andhrapradesh%20box%20plot%20for%20two%20year%20power%20consumption.png"/>

### Distribution of States for overall power consumption
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Distplot%20for%20power%20consumption%20in%20states.png"/>

### Gujarat State power consumption of two years - box plot 
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Gujarat%20box%20plot%20for%20two%20year%20power%20consumption.png"/>

### Histogram for Andhra Pradesh State
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Histogram%20for%20power%20consumption%20for%20Andhra%20Pradesh.png"/>

### Karnataka state power consumption - box plot
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Karnataka%20box%20plot%20for%20two%20year%20power%20consumption.png"/>

## Prediction using Decision Tree Regression algorithm
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Power%20Consumption%20in%20India/Images/Decision%20Tree%20Regressor%20Prediction.png"/>

## CONCLUSION
Here we can conclude that the implementation of Decision Tree Regression Model has the highest training score and predicitons are quite good for power consumption in Mega Watts for each month of each state.

## Name
Project contributed by: Piyush Bhujbal
<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/https://www.linkedin.com/in/piyush-bhujbal-637a621a5/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/piyush-bhujbal-637a621a5/" height="30" width="40" /></a>
</p>





