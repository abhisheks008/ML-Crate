<h1>Top Foreign Language Analysis</h1>

**GOAL**

To build a machine learning model for predicting the usd_price per lesson for a given language and other feature.

**DATASET**

[https://www.kaggle.com/datasets/margaritakholostova/support-ii-dataset-with-critically-ill-patients](https://www.kaggle.com/datasets/timmofeyy/top-foreign-languages-preply-tutors)

**DESCRIPTION**

To analyze the dataset of Top Foreign Language and build and train the model on the basis of different features and variables.

The data includes the main languages and the most popular among students. The datasets have 8 csv files for 8 different top foreign languages.

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

<img alt="correlation" src="./Images/
correlation between amount of lessons and price per lesson.png">

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

* Load the dataset which is in zip file format unzipped it and than concatenated all 8 CSV files.
* After Concatenation it contains 34442 entries in it and having 47 columns in it.
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
10. missingno
11. plotly


**CONCLUSION**

- Random Forest and Linear Regression models show promising performance with lower MSE and higher R2 values.
- Decision Tree Regression achieved perfect R2 on the training set but performed poorly on the test set, indicating overfitting.
- Deep Neural Network (NN) has a high MSE and approximately zero R2, suggesting poor performance on both training and test sets.


**YOUR NAME**

*Ghousiya Begum*

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ghousiya-begum-a9b634258/)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ghousiya47)

