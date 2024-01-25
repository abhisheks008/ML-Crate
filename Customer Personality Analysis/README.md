<h1>Customer Personality Analysis</h1>

**GOAL**

To build a machine learning model for predicting the customer's personality on the basis of his daily living.

**DATASET**

https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis

**DESCRIPTION**

To analyze the dataset of customer's personality and build and train the model on the basis of different features and variables.


### Visualization and EDA of different attributes:

<img alt="graph" src="./Images/histplot.png">

<img alt="graph" src="./Images/figure1.png">

<img alt="graph" src="./Images/figure.png">

<img alt="graph" src="./Images/expenses.png">

<img alt="graph" src="./Images/Images.png">

<img alt="graph" src="./Images/marital_status.png">


**MODEL USED**

| Model             | Shiloutte Score | V Score | Completeness |
|-------------------|-----------------|---------|--------------|
| K-Means           | 0.30            | 0.26    | 0.97         |
| Mean Shift        | 0.18            | 0.23    | 0.96         |
| Agglometric       | 0.19            | 0.21    | 0.98         |
| DBSCAN            | -0.33           | 0.26    | 0.97         |



**WHAT I HAD DONE**

* Load the dataset which contains 2240 entries in it and having 29 columns in it.
* Checked for missing values and cleaned the data accordingly.
* Analyzed the data, found insights and visualized them accordingly.
* Found detailed insights of different columns with target variable using plotting libraries.
* Train the datasets by different models and saves their accuracies into a dataframe.


**LIBRARIES NEEDED**

1. Pandas
2. Matplotlib
3. Sklearn
4. NumPy
5. Seaborn


**CONCLUSION**

Using different clustering models found out the silhouette score, v score and completeness score of the a particular column and the whole dataset.

**Pawas Pandey**

