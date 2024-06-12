## **Automobile Sales Data Analysis and Prediction**

### 🎯 **Goal**

The aim of this project is to create a machine learning model to predict the sales of the automobiles and prepare a data analysis of the same.

### 🧵 **Dataset**

https://www.kaggle.com/datasets/ddosad/auto-sales-data

### 🧮 **What I had done!**

1. Data Cleaning and Preprocessing

- **Load the dataset**: Import the data into a pandas DataFrame for manipulation and analysis.
- **Convert date columns to datetime format**: Ensure date columns are in datetime format for time series analysis.
- **Handle missing values**: Impute missing numerical values with mean/median and categorical values with mode to maintain dataset integrity.
- **Ensure appropriate data formats**: Verify that all columns have the correct data types (e.g., integers, floats, strings).
- **Remove duplicates**: Identify and eliminate duplicate rows to avoid skewed analysis results.

2. Exploratory Data Analysis (EDA)

- **Summarize the dataset with descriptive statistics**: Get an overview of the data distribution using mean, median, and standard deviation.
- **Plot distributions**: Use histograms and boxplots to visualize the distribution of numerical variables and identify outliers.
- **Analyze relationships**: Create a correlation matrix to examine relationships between variables and use scatter and bar plots to explore these relationships further.

3. Feature Selection and Engineering

- **Identify relevant features**: Use domain knowledge and statistical methods (like correlation) to select features that impact sales.
- **Create new features if needed**: Develop aggregate or interaction features that could provide additional insights.
- **Encode categorical variables**: Apply One-Hot Encoding for nominal categories and Label Encoding for ordinal categories to convert them into numerical format.
- **Scale numerical features**: Use StandardScaler or MinMaxScaler to normalize the numerical data, ensuring consistent input ranges for models.

4. Model Selection and Training

- **Split data into training and testing sets**: Divide the dataset into training (e.g., 80%) and testing (e.g., 20%) subsets to evaluate model performance.
- **Choose regression algorithms**: Select models like Random Forest Regressor and Gradient Boosting Regressor for their effectiveness in handling regression tasks.
- **Train models and perform hyperparameter tuning**: Fit the models on the training data and use cross-validation or grid search for hyperparameter optimization.

5. Model Evaluation

- **Evaluate performance using metrics**: Assess models using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R²) to understand their accuracy.
- **Compare model performance**: Analyze and compare the evaluation metrics to select the best-performing model.

6. Interpretation and Insights

- **Extract insights from model results**: Use feature importance scores and partial dependence plots to understand which features most influence sales.
- **Analyze the impact of features on sales**: Draw conclusions about how different car features and economic conditions affect sales performance.

7. Visualization

- **Visualize actual vs. predicted sales**: Create line plots for time series data and scatter plots for predicted vs. actual sales values to assess model accuracy.
- **Use bar plots and residual plots**: Display feature importances with bar plots and check model accuracy with residual plots, highlighting areas for improvement.

### 🚀 **Models Implemented**

1. Simple Dense Model
2. Bidirectional LSTM
3. Convolutional Neural Network
4. Random Forest Regressor
5. Temporal Convolutional Network

### 📚 **Libraries Needed**

1. numpy
2. pandas
3. matplotlib
4. scikit-learn

### 📊 **Exploratory Data Analysis Results**

<img src = "https://github.com/why-aditi/ML-Crate/blob/main/Automobile%20Sales%20Data%20Analysis%20and%20Prediction/Images/Dealsize_bar.png"/>
<img src = "https://github.com/why-aditi/ML-Crate/blob/main/Automobile%20Sales%20Data%20Analysis%20and%20Prediction/Images/Dealsize_pie.png"/>
<img src = "https://github.com/why-aditi/ML-Crate/blob/main/Automobile%20Sales%20Data%20Analysis%20and%20Prediction/Images/Productline_bar.png"/>
<img src = "https://github.com/why-aditi/ML-Crate/blob/main/Automobile%20Sales%20Data%20Analysis%20and%20Prediction/Images/Productline_pie.png"/>
<img src = "https://github.com/why-aditi/ML-Crate/blob/main/Automobile%20Sales%20Data%20Analysis%20and%20Prediction/Images/Status_bar.png"/>
<img src = "https://github.com/why-aditi/ML-Crate/blob/main/Automobile%20Sales%20Data%20Analysis%20and%20Prediction/Images/Status_pie.png"/>

### 📈 **Performance of the Models based on the Accuracy Scores**

`MAE was used as the performance metric.

1. Simple Dense model: 575.88
2. Bidirectional LSTM: 9.149645e+02
3. Convolutional Neural Network: 9.461755e+02
4. Random Forest Regressor: 610.215271
5. Temporal Convolutional Network: 698.471619`

### 📢 **Conclusion**

`**Best Performing Model**: Model 1 now has the lowest MAE (575.88), MSE (551668.13), RMSE (742.74), and MAPE (20.27), indicating that it has the lowest overall errors among the five models.

**Second Best**: Model 4, which previously was the best performer, now comes in second with slightly higher MAE (610.22), MSE (610762.19), RMSE (781.51), and MAPE (22.02) compared to Model 1.

**Models 2 and 3**: These models continue to have significantly higher errors across all metrics, making them the least preferred models.

**Model 5**: This model performs moderately but not as well as Models 1 and 4. Its errors are higher in all metrics compared to Model 1 and Model 4.`

### ✒️ **Your Signature**

`Aditi Kala`
