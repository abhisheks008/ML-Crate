<h1>IELTS Success Stories Analysis and Prediction Model</h1>

**GOAL**

The aim of this project is to analyze and predict the success rates of IELTS.

**DATASET**

https://www.kaggle.com/datasets/zakirkhanaleemi/ielts-success-stories-dataset

**DESCRIPTION**

To analyze the IELTS Success Stories Dataset and build and train the model on the basis of different features and variables.


### Visualization and EDA of different attributes:

<img alt="heatmap" src="./Images/correlation_heatmap.png">

<img alt="graph" src="./Images/target_correlation.png">

<img alt="graph" src="./Images/Application Status_feature.png">

<img alt="graph" src="./Images/Location_feature.png">

<img alt="graph" src="./Images/Study Duration (months)_feature.png">


**MODELS USED**

| Model                       | MSE_train           | R2_train | MSE_test  | R2_test   |
|-----------------------------|---------------------|----------|-----------|-----------|
| Random Forest Regression    | 7.79e-03            | 0.977    | 0.0151    | 0.9257    |
| XG Boost Regression         | 1.42e-07            | 1.000    | 0.0165    | 0.919     |
| Decision Tree Regression    | 0.000               | 1.000    | 0.0208    | 0.8974    |
| Ridge Regression            | 6.44e-04            | 0.998    | 0.0723    | 0.6439    |
| Elastic Net Regression      | 9.25e-02            | 0.727    | 0.1335    | 0.3428    |
| Linear Regression           | 4.13e-30            | 1.000    | 0.154     | 0.2418    |
| KNN Regression              | 1.01e-01            | 0.703    | 0.1683    | 0.1713    |



**WHAT I HAD DONE**

* Load the dataset which contains 27 entries in it and having 23 features in it.
* Checked for missing values and cleaned the data accordingly.
* Analyzed the data, found insights and visualized them accordingly.
* Plotting heatmap using correlation and checking the relation between different features.
* Found detailed insights of different columns with target variable using plotting libraries and plot the box-plot to see the distribution of dataset correspond to target features.
* Split the dataset into training and testing dataset.
* Apply PCA to reduce the number of features.
* Apply different training models and get their accuracies and MSE and R2 scores.
* Train the datasets by different models and saves their accuracies into a dataframe.


**LIBRARIES NEEDED**

1. Pandas
2. Matplotlib
3. Sklearn
4. NumPy
5. XGBoost
6. Tensorflow
7. Keras
8. Sci-py
9. Seaborn


**CONCLUSION**

- Random Forest and XG Boost Regression models show promising performance with lower MSE and higher R2 values.
- Decision Tree Regression achieved perfect R2 on the training set but performed poorly on the test set, indicating overfitting.


**YOUR NAME**

*Avdhesh Varshney*

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/avdhesh-varshney/)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Avdhesh-Varshney)

