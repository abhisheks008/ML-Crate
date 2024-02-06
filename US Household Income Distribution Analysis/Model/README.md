 **Project Title**

US Household Income Distribution Analysis

**Aim of the Project**  
This project will analyze the distribution of the income data of the households of US.  

**Dataset**  
https://www.kaggle.com/yamqwe/2018-w3-u-s-household-income-distribution-by-stae  

**Approach**  
Performed Exploratory Data Analysis on the dataset and Used 3-4 Regression Algorithmns to implement the models and Compared all the algorithms to find out the best fitted one.  
**Steps Involved**  
1. Import Required libraries.  
2. Load the dataset.  
3. Performing EDA on the data like Outlier Treatment, Handling Missing values.  
4. Identifying Input and Target columns from the dataset.
5. Separating Numerical and Categorical columns. 
6. Scaling the numeric columns and Encoding the categorical columns.
7. Splitting the Data into Training and Testing dataset.
8.  Model Building: We use four algorithms to build the models   
      - LinearRegression   
      - DecisionTreeRegressor   
      - RandomForestRegressor   
      - Ridge Regression
      - XGBRegressor 
9. After fitting these models with the data, we analyze the model using metric ```mean_squared_error``` and compare the correlation coefficient ```r2_score``` of all algorithms.

**Data Visualization**    

### Correlation Plot 

![correlation](https://github.com/jahnavibattu02/ML-Crate/blob/main/US%20Household%20Income%20Distribution%20Analysis/Images/correlation.png)  

### Percent of Total

![PercentofTotal](https://github.com/jahnavibattu02/ML-Crate/blob/main/US%20Household%20Income%20Distribution%20Analysis/Images/PerccentofTotal.png)  

### Number of Households  

![](https://github.com/jahnavibattu02/ML-Crate/blob/main/US%20Household%20Income%20Distribution%20Analysis/Images/NumberofHouseholds.png)   

### Pairplot 

![Pairplot](https://github.com/jahnavibattu02/ML-Crate/blob/main/US%20Household%20Income%20Distribution%20Analysis/Images/pairplot.png)  

**RMSE**
- Linear Regression  = 0.012629
- DecisionTreeRegression = 0.003997
- RandomForestRegressor = 0.003098
- Ridge Regression = 0.012628	
- XGBRegressor = 0.010661	
**Conclusion:** 
_Among all the models listed above, we can see that RandomForestRegressor have least RMSE of ```0.003098```. We can conclude that it is the best fitted model._      

**Language and Libraries Used:**
- Python Programmming is used.  
- Libraries like Numpy, Pandas, Seaborn, Matplotlib, Scikit-Learn are used.

## 
  Code Contributed by Jahnavi Pravaleeka Battu
