# GPU Price Prediction Project

## Goal
The goal of this project is to predict the prices of GPUs based on various features such as HDMI support, boost clock, VRAM, and memory clock. Accurate price predictions can help consumers make informed decisions and manufacturers optimize pricing strategies.

## Dataset
The dataset used for this project is sourced from [GPUData.csv](https://www.kaggle.com/datasets/username/gpu-prices), which includes columns like:
- `Name`: GPU model name
- `Producer`: GPU producer
- `HDMI`: HDMI support
- `Boost.Clock`: Boost clock speed
- `Vram`: VRAM size
- `Memory.Clock`: Memory clock speed

## Description
The dataset is preprocessed to handle missing values and encode categorical variables. Several machine learning models are used to predict the price of GPUs, and their performances are evaluated based on metrics such as RMSE and R2 score.

## What I Had Done
1. **Data Preprocessing**: Cleaned and preprocessed the dataset by handling missing values, encoding categorical variables, and scaling features.
2. **Model Training and Evaluation**: Trained multiple regression models and evaluated their performance using RMSE and R2 scores.
3. **Results Visualization**: Plotted model performance metrics to compare their effectiveness.

## Models Implemented
1. **Linear Regression**
2. **Ridge Regression**
3. **Lasso Regression**
4. **Decision Tree Regressor**
5. **Random Forest Regressor**
6. **Gradient Boosting Regressor**
7. **XGBoost Regressor**
8. **CatBoost Regressor**
9. **Support Vector Regressor**
10. **K-Nearest Neighbors Regressor**
11. **Extra Trees Regressor**

## Libraries Needed
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `xgboost`
- `lightgbm`
- `catboost`

## EDA Results
Preprocessing steps included cleaning missing values, encoding categorical features, and scaling numerical features. The features used for model training include `HDMI`, `Boost.Clock`, `Vram`, and `Memory.Clock`.

## Performance of the Models based on Accuracy Scores

| Model                       | Train RMSE         | Test RMSE          | Train R2           | Test R2            |
|-----------------------------|---------------------|---------------------|---------------------|---------------------|
| Linear Regression           | 17.65               | 302016927576.74     | 0.9991              | -1.9900E+017        |
| Ridge Regression            | 123.93              | 300.17              | 0.9580              | 0.8034              |
| Lasso Regression            | 134.90              | 333.59              | 0.9502              | 0.7572              |
| Decision Tree Regressor     | 17.65               | 302.87              | 0.9991              | 0.7999              |
| Random Forest Regressor     | 151.01              | 353.12              | 0.9376              | 0.7280              |
| Gradient Boosting Regressor | 105.99              | 307.28              | 0.9693              | 0.7940              |
| XGBoost Regressor           | 38.36               | 328.19              | 0.9960              | 0.7650              |
| CatBoost Regressor          | 81.89               | 330.35              | 0.9817              | 0.7619              |
| Support Vector Regressor    | 626.45              | 696.85              | -0.0733             | -0.0594             |
| K-Nearest Neighbors Regressor| 290.01              | 364.72              | 0.7700              | 0.7098              |
| Extra Trees Regressor       | 17.65               | 359.22              | 0.9991              | 0.7185              |

## Conclusion
The models were evaluated based on RMSE and R2 scores. Linear Regression and Decision Tree Regressor showed the lowest RMSE values, while Support Vector Regressor had the lowest R2 scores. XGBoost and Gradient Boosting Regressor performed well in terms of R2 score, indicating strong predictive capabilities.

## Signature
- **Name:** Aditya D
- **Github:** [https://www.github.com/adi271001](https://www.github.com/adi271001)
- **LinkedIn:** [https://www.linkedin.com/in/aditya-d-23453a179/](https://www.linkedin.com/in/aditya-d-23453a179/)
- **Topmate:** [https://topmate.io/aditya_d/](https://topmate.io/aditya_d/)
- **Twitter:** [https://x.com/ADITYAD29257528](https://x.com/ADITYAD29257528)
