# Salary Predictions of Data Professionals

## 🎯 Goal
The main goal of this project is to predict the salaries of data professionals based on various factors such as experience, job role, and performance ratings. The purpose is to provide a reliable and accurate prediction model that can be used by individuals and organizations to estimate salary expectations.

## 🧵 Dataset
The dataset used in this project can be found in the `Dataset` folder. 

## 🧾 Description
This project includes data analysis, feature engineering, machine learning model development, and deployment of the predictive model as a web application. The model predicts the salary based on input features such as job role, experience, age, and ratings.

## 🧮 What I had done!
1. **Data Collection:** Loaded the dataset and performed initial cleaning.
2. **Exploratory Data Analysis (EDA):** Analyzed the data to understand distributions and correlations.
3. **Feature Engineering:** Created new features and handled missing values.
4. **Model Development:** Trained multiple machine learning models.
5. **Model Evaluation:** Evaluated models using performance metrics.
6. **Deployment:** Deployed the best model as a web application using Flask.

## 🚀 Models Implemented
- **Linear Regression:** Chosen for its simplicity and interpretability.
- **Decision Tree Regressor:** Used to capture non-linear relationships.
- **Random Forest Regressor:** Employed for its robustness and ability to handle large datasets.
- **Gradient Boosting Regressor:** Selected for its high performance on various prediction tasks.

## 📚 Libraries Needed
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `joblib`
- `flask`
- `plotly`

## 📊 Exploratory Data Analysis Results
### Correlation Heatmap
<img src="Images/.eda/correlation_heatmap.png" alt="Correlation Heatmap">
### Distribution of Salary
<img src="Images/.eda/distribution_of_salary.png" alt="Distribution of Salary">
### Salary vs. Age
<img src="Images/.eda/salary_vs_age.png" alt="Salary vs. Age">
### Salary by Designation
<img src="Images/.eda/salary_by_designation.png" alt="Salary by Designation">


## 📈 Performance of the Models based on the Accuracy Scores
- **Linear Regression:**
  - Mean Absolute Error (MAE): 10.50
  - Mean Squared Error (MSE): 150.75
  - R-squared (R2): 0.82
- **Decision Tree Regressor:**
  - Mean Absolute Error (MAE): 12.30
  - Mean Squared Error (MSE): 180.45
  - R-squared (R2): 0.76
- **Random Forest Regressor:**
  - Mean Absolute Error (MAE): 8.90
  - Mean Squared Error (MSE): 125.60
  - R-squared (R2): 0.86
- **Gradient Boosting Regressor:**
  - Mean Absolute Error (MAE): 8.45
  - Mean Squared Error (MSE): 120.30
  - R-squared (R2): 0.87

## 📢 Conclusion
The Gradient Boosting Regressor outperformed all other models with the highest R-squared value of 0.87 and the lowest Mean Absolute Error of 8.45. This model was selected for deployment due to its superior accuracy and robustness.

✒️ **Your Name**
- GitHub: [Harshit-code-tech](https://github.com/Harshit-code-tech)
- LinkedIn: [Harshit Ghosh](www.linkedin.com/in/harshit-ghosh-026622272)
