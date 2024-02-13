<h1>Top Foreign Language Analysis</h1>

**GOAL**

To build a machine learning model for predicting the Average Rainfall per month for a given atmospheric conditions like temperature, humidity , dewpoint, pressure, windspeed, etc.

**DATASET**

[https://www.kaggle.com/datasets/mastmustu/weather-analysis]

**DESCRIPTION**

To analyze the dataset of Weather Analysis and build and train the model on the basis of different features and variables.

The datasets have a csv file with 3902 entries, 22 columns.

- **columns_description**: Each CSV File contains the description of all the features.

  name: The name of the tutor.

  badge: Any badge or certification associated with the tutor.

  rating: The overall rating of the tutor.

  reviews_number: The number of reviews the tutor has received.

  usd_price: The price charged by the tutor for their services.

  language: The languages spoken by the tutor.

  active_students: The number of active students the tutor is currently teaching.

  lessons_number: The total number of lessons conducted by the tutor.

  speak: The languages spoken by the tutor.

  description: A brief description or snippet provided by the tutor.

  link: The link or URL to the tutor's profile.


### Visualization and EDA of different attributes:

<img alt="correlation" src="./Images/correlation between amount of lessons and price per lesson.png">

<img alt="graph" src="./Images/count of tutors.png">

<img alt="graph" src="./Images/distribution plot.png">




**MODELS USED**

| Model                     | MSE_train | R2_train | MSE_test  | R2_test   |
|---------------------------|-----------|----------|-----------|-----------|
| Random Forest Regression  | 7.03      | 0.93     | 57.90     | 0.51      |
| Linear Regression         | 17.09     | 0.84     | 60.72     | 0.49      |
| Ridge Regression          | 85.65     | 0.22     | 96.16     | 0.20      |
| Elastic Net Regression    | 105.0     | 0.04     | 114.7     | 0.047     |
| Decision Tree Regression  | 0.00      | 1.00     | 61.30     | 0.49      |
| Deep NN                   | 34.29     | 0.04     | 114.7     | 0.0471    |


**WHAT I HAD DONE**

* Load the dataset which is CSV format.
* It has 3902 entries(Rows), 22 columns.
* Checked for missing values and cleaned the data accordingly.
* Analyzed the data, found insights and visualized them accordingly.
* Plotting heatmap using correlation and checking the relation between different features.
* Found detailed insights of different columns with target variable using plotting libraries.
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

- Random Forest and XGBoost Regression models show promising performance with lower MSE and higher R-square values for both training set and dataset.
- Decision Tree Regression achieved perfect R-square on the training set but on the test set it's value is 0.6, indicating overfitting.
- Deep Neural Network (NN) has a high MSE and negative R-square on testing set, approximately zero on training set, suggesting poor performance on both training and test sets.


**YOUR NAME**

*Ghousiya Begum*

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ghousiya-begum-a9b634258/)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ghousiya47)
