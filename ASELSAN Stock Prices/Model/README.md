### ASELSAN Stock Price Prediction Project

### 🎯 **Goal**

The goal of this project is to develop a machine learning model capable of predicting the stock prices of ASELSAN, a leading defense technology company in Turkey.

### 🧵 **Dataset**

The dataset used in this project was sourced from Kaggle. You can access it [here](https://www.kaggle.com/datasets/zlemglsmklkaya/aselsan-stock-prices-20172022).

### 🧾 **Description**

This project involves the analysis and prediction of ASELSAN stock prices using historical stock price data from 2017 to 2022. The aim is to create an accurate predictive model by exploring the dataset, visualizing different aspects of the stock prices, and implementing various machine learning algorithms.

### 🧮 **What I Had Done!**

1. **Data Preprocessing**:
   - Imported necessary libraries and the dataset.
   - Deleted unnecessary columns to streamline the dataset.
   - Changed data types of relevant columns for accurate analysis.

2. **Exploratory Data Analysis and Visualization**:
   - Conducted exploratory data analysis (EDA) to understand the dataset.
   - Visualized different aspects of the dataset using plots and charts:
     - **Variation of Opening Price**: Plotted the variation of ASELSAN's opening price over time.
     - **Heatmap**: Created a heatmap to understand correlations between features.
     - **Closing Price Trends**: Analyzed trends in closing prices over the years.
     - **Volume Traded**: Visualized the volume of stocks traded over time.
     - **Price Distribution**: Examined the distribution of stock prices.
     - **Daily Returns**: Plotted daily returns to understand stock volatility.
     - **Yearly Trends**: Investigated yearly trends in stock prices.
     - **Correlation Matrix**: Displayed the correlation matrix to find relationships between variables.

3. **Model Development**:
   - Developed and applied various machine learning models for predicting ASELSAN stock prices.
   - Evaluated the performance of each model using appropriate metrics.

### 🚀 **Models Implemented**

- **Linear Regression**: Chosen for its simplicity and interpretability.
- **Lasso Regression**: Selected to prevent overfitting by adding L1 regularization.
- **Ridge Regression**: Utilized for L2 regularization, although it performed poorly.
- **Decision Tree Regressor**: Selected for its ability to model non-linear relationships.

### 📚 **Libraries Needed**

- **numpy**: For numerical computing.
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For creating visualizations.
- **seaborn**: For enhancing the aesthetics of plots.
- **sklearn**: For machine learning tasks.

### 📊 **Exploratory Data Analysis Results**

![Variation of Opening Price](https://user-images.githubusercontent.com/97960335/180611222-bcbf5e61-cc74-4ba7-9b90-89f2cfd2919f.png)
![Heatmap](https://user-images.githubusercontent.com/97960335/180611224-e1b325ff-605f-46dc-b5d5-c145a673c13c.png)
![Closing Price Trends](https://user-images.githubusercontent.com/97960335/180611225-f63eae85-7e3c-421a-8f40-241884ed2bf1.png)
![Volume Traded](https://user-images.githubusercontent.com/97960335/180611229-fefa8ec1-54bd-46fc-9e4b-746793dbf8fd.png)
![Price Distribution](https://user-images.githubusercontent.com/97960335/180611233-6f68df38-beb3-48bd-8c13-80e61d60ea09.png)
![Daily Returns](https://user-images.githubusercontent.com/97960335/180611235-a9ddbea7-2717-4032-bcfe-a2e8677ee461.png)
![Yearly Trends](https://user-images.githubusercontent.com/97960335/180611257-0ac8cc5c-6947-4dba-8547-0fc5342a281a.png)
![Correlation Matrix](https://user-images.githubusercontent.com/97960335/180611261-e80e1bf5-7805-44d3-aa8e-83686bbc454d.png)

### 📈 **Performance of the Models based on the Accuracy Scores**

- **Linear Regression**: 
  - Score (Train): 99.77%
  - Score (Test): 99.74%
- **Lasso Regression**: 
  - Score (Train): 99.75%
  - Score (Test): 99.61%
- **Ridge Regression**: 
  - Score (Train): 37.57%
  - Score (Test): -71.23%
- **Decision Tree Regressor**: 
  - Score (Train): 99.93%
  - Score (Test): 86.52%

### 📢 **Conclusion**

The Linear Regression model performed the best among all the models implemented, achieving a high train score of 99.77% and a test score of 99.74%. The Lasso Regression also performed well, with slightly lower accuracy but still very close to Linear Regression. The Decision Tree Regressor showed good performance on the training data but lower accuracy on the test data, indicating potential overfitting. Ridge Regression performed poorly and is not suitable for this dataset. This project demonstrates the application of various machine learning algorithms to predict stock prices, with Linear Regression providing the most accurate predictions for ASELSAN's stock prices.

### ✒️ **Your Signature**

Created by [Nirvik](https://github.com/nirvik07) as part of HRSoc 2022.
