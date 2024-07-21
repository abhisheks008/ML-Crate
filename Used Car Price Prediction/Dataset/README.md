# Car Price Prediction Dataset

## 📝 Description
Explore the intricate details of car prices with our comprehensive dataset. This dataset captures various attributes of cars, each labeled with its respective price. By analyzing this dataset, you will gain valuable insights into the factors that influence car prices, aiding in accurate and efficient price prediction.

## Key Features
- **Diverse Car Attributes:** Understand the impact of various attributes on car prices, including brand, model, model year, mileage, fuel type, engine type, transmission type, exterior color, interior color, accident history, and title status.
- **High-Quality Data:** Each car is represented with detailed attributes, ensuring that all relevant factors are captured for thorough analysis.
- **Balanced Representation:** While some attributes may have more variations than others, the dataset provides a balanced overview of different car features, facilitating effective training and testing of regression models.

## Data Collection
The data has been meticulously collected and labeled based on actual car listings. This structured approach ensures that each car is accurately described, providing a reliable dataset for training machine learning models.

## Data Attributes
The dataset contains the following attributes for each car:

- **id:** Unique identifier for each car
- **brand:** The brand of the car
- **model:** The specific model of the car
- **model_year:** The year the car model was manufactured
- **milage:** The total mileage of the car in kilometers
- **fuel_type:** The type of fuel used by the car (e.g., Petrol, Diesel, Electric)
- **engine:** The engine type of the car (e.g., V6, V8, Electric)
- **transmission:** The type of transmission in the car (e.g., Automatic, Manual)
- **ext_col:** The exterior color of the car
- **int_col:** The interior color of the car
- **accident:** Indicates whether the car has been in an accident (Yes/No)
- **clean_title:** Indicates whether the car has a clean title (Yes/No)
- **price:** The price of the car (target variable)

## Sample Data
Here are a few sample entries from the dataset:

| id | brand  | model | model_year | milage | fuel_type | engine | transmission | ext_col | int_col | accident | clean_title | price |
|----|--------|-------|------------|--------|-----------|--------|--------------|---------|---------|----------|-------------|-------|
| 1  | Toyota | Camry | 2015       | 60000  | Petrol    | V6     | Automatic    | Black   | Grey    | No       | Yes         | 15000 |
| 2  | Ford   | F-150 | 2018       | 40000  | Diesel    | V8     | Manual       | White   | Black   | Yes      | No          | 22000 |
| 3  | Tesla  | Model S | 2020     | 20000  | Electric  | Electric | Automatic  | Red     | White   | No       | Yes         | 75000 |

## How to Use the Dataset
To use this dataset for training machine learning models, follow these steps:

1. **Download the Dataset:**
   The dataset can be downloaded from the relevant directory within this project.[Kaggle](https://www.kaggle.com/datasets/zeeshanlatif/used-car-price-prediction-dataset/data?select=train.csv)

2. **Data Preprocessing:**
   - Convert categorical columns to category dtype.
   - Apply standard scaling for numerical features.
   - Apply one-hot encoding for categorical features.
   - Split the data into training and test sets for model evaluation.

3. **Model Training:**
   Train various machine learning models on the dataset to predict car prices based on the provided attributes.

## 📢 Conclusion
The car price prediction dataset provides a comprehensive and well-structured collection of car attributes and prices, facilitating the development of accurate and robust prediction models. By leveraging this dataset, you can gain valuable insights into the factors that influence car prices and improve your predictive modeling capabilities.

