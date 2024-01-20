<h1>Student Attendance based on Weather Conditions </h1>

**GOAL**

To build a machine learning model for predicting the Student Attendance based on Weather Conditions .

**DATASET**

https://www.kaggle.com/datasets/joshjohnson9596/student-attendance-and-weather-conditions

**DESCRIPTION**

To analyze the dataset of Students and build and train the model on the basis of different features and variables.

There are 3 features in the datasets:

- `weather`: It shows the different types of weather.
- `temperature`: It tells about the temperature.


### Visualization and EDA of different attributes:



<img alt="graph" src=".images/Weather Distribution.png">

<img alt="graph" src=".images/Student Attendance.png">

<img alt="graph" src=".images/Student Attendance on different Weather Conditions.png">

<img alt="graph" src=".images/Student Attendance on different Temperature.png">

**MODELS USED**

| Model                     | MSE_train | R2_train | MSE_test  | R2_test   |
|---------------------------|-----------|----------|-----------|-----------|
| Random Forest Regression  | 0.19      | 0.25     | .19       | 0.25      |
| XG Boost Regression       | 0.19      | 0.25     | 0.25      | -2.028    |
| Lasso Regression          | 0.25      | 0.0      | 0.25      | -2.028    |
| Ridge Regression          | .25       | 0.0      | .19       | -2.07     |
| Logistic Regression       | 0.29      | -0.18    | 0.29      | -0.6      |
| Decision Tree Regression  | 0.29      | -0.18    | .28       | -0.14     |
| MLP                       | 0.296     | -0.184   | 0.295     | -0.605    |
| Gradient Boosting         | 0.29      | -0.179   |0.284      | -0.136    |


**WHAT I HAD DONE**

* Load the dataset which contains 10000 entries in it and having 3 columns in it.
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

- Random Forest model show promising performance with lower MSE.

**YOUR NAME**

*Rajneesh Kabdwal*
