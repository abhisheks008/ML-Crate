# Used Car Price Prediction
Explore the world of used car price prediction using various machine learning models to accurately estimate car prices based on their attributes. This project focuses on predicting car prices by analyzing attributes such as brand, model, mileage, fuel type, and more.
<img width="920" alt="webapp1" src="https://github.com/user-attachments/assets/37d15871-c6fe-4042-a360-d10b6b816e15">
<img width="922" alt="webapp2" src="https://github.com/user-attachments/assets/93e44e0a-3a8d-4041-82c2-7bbf2ee1f85e">
## 📝 Abstract
The Used Car Price Prediction project aims to estimate the price of used cars based on multiple features. By applying various machine learning models, including regression techniques and ensemble methods, the project seeks to build a robust model for predicting car prices and provide insights into the factors influencing car values.

## 🔍 Methodology
1. **Importing Libraries**

Essential libraries such as NumPy, Pandas, Scikit-Learn, and XGBoost are imported for data manipulation, preprocessing, model training, and evaluation.

2. **Loading the Dataset**

The dataset contains information about used cars, including features such as brand, model, mileage, fuel type, engine type, transmission type, and more. This dataset is used to train and evaluate the prediction models.

3. **Data Preprocessing**

The preprocessing steps include handling missing values, encoding categorical variables, scaling numerical features, and splitting the dataset into training and testing sets.

4. **Training the Models**

Multiple models are implemented, including Linear Regression, Ridge Regression, Lasso Regression, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting Regressor, Support Vector Regressor, Extra Trees Regressor, K-Nearest Neighbors Regressor, and XGBoost Regressor. Each model is trained and evaluated to identify the most effective approach for predicting car prices.

5. **Model Evaluation**

The performance of each model is evaluated using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R2). Visualization of results helps in comparing the effectiveness of different models.

6. **Web Application**

A Streamlit web application is developed to allow users to input car attributes and get predictions on car prices in real-time. This application utilizes the pre-trained model to provide instant price estimates.


### 📂 Project Directory Structure

```bash
Used Car Price Prediction
|- Dataset
  |- train.csv
  |- README.md

|- Model
  |- used_car_price_prediction.ipynb
  |- README.md
  |- model.pkl
  |- preprocessor.pkl
  |- unique.pkl

|- Web App
  |- app.py
  |- README.md

|- Images
  |- MAE_cmp.png
  |- MSE_cmp.png
  |- RMSE_cmp.png
  |- R2_cmp.png
  |- car_price_distribution.png
  |- correlation_matrix.png
  |- mileage_vs_price.png
  |- README.md

|- requirements.txt
|- README.md
```
## How to Use
1. **Install Requirements**

Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the requirements.txt file.
```bash
pip install -r requirements.txt
```
2. **Download Data**

Ensure you have the car_prices.csv dataset in the Dataset folder. [Kaggle](https://www.kaggle.com/datasets/zeeshanlatif/used-car-price-prediction-dataset/data?select=train.csv)

3. **Run the Jupyter Notebook**

Open the provided Jupyter Notebook file (used_car_price_prediction.ipynb) and run each cell sequentially. Update any file paths or configurations as needed for your environment.

4. **Training and Evaluation**

Train the models and evaluate their performance using the provided data. Analyze the results to determine the best-performing model.

5. **Run the Web Application**

Navigate to the Web App directory and run the Streamlit application to start predicting car prices using the pre-trained model.
```bash
streamlit run app.py
```
6. **Interpret Results**

Use the provided visualizations and metrics to interpret the model’s performance and insights from the data.

Feel free to reach out if you encounter any issues or need further assistance with running the notebook or web application.

## Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
