 **Greenhouse Gas Emissions Analysis**

## 🎯 **Goal**

The main goal of this project is to analyze and forecast greenhouse gas (GHG) emissions, including CH4, N2O, CO2, NOx, ODS, and SO2, using various machine learning algorithms and geospatial analysis. The purpose is to understand the trends in emissions and identify key factors contributing to these trends, ultimately aiding in the formulation of policies for emission reduction.

## 🧵 **Dataset**

The dataset used in this project is compiled from multiple sources including governmental and environmental organizations. The data includes emissions of different gases from various countries over multiple years. 

- [CH4 Emissions]
- [N2O Emissions]
- [CO2 Emissions]
- [NOx Emissions]
- [ODS Consumption]
- [SO2 Emissions]

## 🧾 **Description**

This project involves the collection, merging, and analysis of greenhouse gas emissions data from various sources. Machine learning models such as LSTM and ANN are implemented for time-series forecasting, while geospatial analysis is conducted to visualize the data. Principal Component Analysis (PCA) is used to reduce dimensionality and identify key patterns.

## 🧮 **What I Had Done!**

1. **Data Collection and Preprocessing:**
   - Collected data from various sources and cleaned it.
   - Normalized the data for better performance of machine learning models.

2. **Data Merging:**
   - Merged datasets on the basis of the 'Country' column.
   
3. **Exploratory Data Analysis (EDA):**
   - Performed EDA to visualize trends and patterns in the data.
   
4. **Feature Engineering:**
   - Conducted feature engineering to create relevant features for modeling.
   
5. **Modeling:**
   - Implemented LSTM and ANN for time-series forecasting.
   - Applied PCA for dimensionality reduction.
   - Conducted geospatial analysis to visualize emissions geographically.

6. **Model Evaluation:**
   - Evaluated the performance of the models using accuracy scores and other relevant metrics.

## 🚀 **Models Implemented**

- **LSTM (Long Short-Term Memory):** Chosen for its effectiveness in handling time-series data and capturing long-term dependencies.
- **ANN (Artificial Neural Network):** Used for its flexibility and ability to model complex relationships in the data.
- **Geospatial Analysis:** Implemented to visualize emissions data geographically and identify regional trends.
- **PCA (Principal Component Analysis):** Applied for dimensionality reduction and to identify the most important features in the dataset.

## 📚 **Libraries Needed**

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `tensorflow`
- `scikit-learn`
- `geopandas`
- `pysal`
- `libpysal`

## 📊 **Exploratory Data Analysis Results**

![EDA Results](https://github.com/minal2577/ML-Crate/blob/main/GLOBAL%20%20EMISSION%20ANALSIS/Images/global%20carbon%20emission%20anlysis.png)

*Include various images showcasing the EDA results here.*

## 📈 **Performance of the Models based on the Accuracy Scores**

- **LSTM:**
   - Mean Squared Error (MSE): 0.11771341085785052
   - Root Mean Squared Error (RMSE): 0.34309388053104434
   - Mean Absolute Error (MAE): 0.17082083003785606

- **ANN:**
  - Mean Squared Error (MSE): 0.001151512867330171
  - Root Mean Squared Error (RMSE): 0.03393394859620924
  - Mean Absolute Error (MAE): 0.02689476781745063

- **PCA:**
  - Explained Variance Ratio: [0.34, 0.17] 

## 📢 **Conclusion**

The project successfully analyzed and forecasted greenhouse gas emissions using various machine learning models and geospatial analysis. The ANN model performed slightly better than the LSTM model in terms of accuracy. The PCA analysis helped in identifying the key factors contributing to emissions. The geospatial analysis provided valuable insights into regional emission trends, which can aid in policy-making for emission reduction.

## ✒️ **Your Signature**

Minal Jain  
[LinkedIn](https://linkedin.com/in/minal-631400259) | [GitHub](https://github.com/minal2577)
