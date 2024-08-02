# New York City Airbnb Price Prediction: Models

## Models Implemented
- Linear Regression (LR)
- Ridge Regression (Ridge)
- Lasso Regression (Lasso)
- ElasticNet Regression (ElasticNet)
- K-Nearest Neighbors Regression (KNN)
- Decision Tree Regression (CART)
- Random Forest Regression (RF)
- Gradient Boosting Machine (GBM)
- XGBoost
- LightGBM
- CatBoost

## Performance of the Models Based on Accuracy Scores
- **Linear Regression (LR):**
    - RMSE: 70.0431
    - R² Score: 0.6656
    - MAE: 42.088
    - MSE: 4906.0328
    - Execution Time: 0.04 seconds

- **Ridge Regression (Ridge):**
    - Best parameters: {'alpha': 1.0}
    - RMSE: 70.0438
    - R² Score: 0.6656
    - MAE: 42.0872
    - MSE: 4906.1288
    - Execution Time: 2.1 seconds

- **Lasso Regression (Lasso):**
    - Best parameters: {'alpha': 0.1}
    - RMSE: 70.1052
    - R² Score: 0.665
    - MAE: 42.0402
    - MSE: 4914.7403
    - Execution Time: 1.76 seconds

- **ElasticNet Regression (ElasticNet):**
    - Best parameters: {'alpha': 0.1, 'l1_ratio': 0.9}
    - RMSE: 70.3563
    - R² Score: 0.6626
    - MAE: 42.0211
    - MSE: 4950.0056
    - Execution Time: 3.94 seconds

- **K-Nearest Neighbors Regression (KNN):**
    - Best parameters: {'n_neighbors': 5}
    - RMSE: 39.7241
    - R² Score: 0.8924
    - MAE: 22.0858
    - MSE: 1578.0056
    - Execution Time: 6.23 seconds

- **Decision Tree Regression (CART):**
    - Best parameters: {'max_depth': None, 'min_samples_leaf': 1}
    - RMSE: 10.2621
    - R² Score: 0.9928
    - MAE: 1.1928
    - MSE: 105.3113
    - Execution Time: 3.15 seconds

- **Random Forest Regression (RF):**
    - Best parameters: {'max_depth': None, 'n_estimators': 50}
    - RMSE: 6.9945
    - R² Score: 0.9967
    - MAE: 0.915
    - MSE: 48.9226
    - Execution Time: 65.45 seconds

- **Gradient Boosting Machine (GBM):**
    - Best parameters: {'learning_rate': 0.1, 'n_estimators': 50}
    - RMSE: 34.4356
    - R² Score: 0.9192
    - MAE: 19.4025
    - MSE: 1185.8113
    - Execution Time: 25.74 seconds

- **XGBoost:**
    - Best parameters: {'learning_rate': 0.1, 'n_estimators': 50}
    - RMSE: 8.4594
    - R² Score: 0.9951
    - MAE: 4.6483
    - MSE: 71.5611
    - Execution Time: 3.74 seconds

- **LightGBM:**
    - Best parameters: {'learning_rate': 0.1, 'n_estimators': 50}
    - RMSE: 8.9302
    - R² Score: 0.9946
    - MAE: 4.7429
    - MSE: 79.7482
    - Execution Time: 9.23 seconds

- **CatBoost:**
    - Best parameters: {'depth': 6, 'iterations': 50, 'learning_rate': 0.1}
    - RMSE: 22.0192
    - R² Score: 0.967
    - MAE: 13.5157
    - MSE: 484.847
    - Execution Time: 11.29 seconds

![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___102_1.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___102_2.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___102_3.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___102_4.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___102_5.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___104_1.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___104_2.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___104_3.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___104_4.png?raw=true)
![RESULT](https://github.com/adi271001/ML-Crate/blob/airbnb-price/New%20York%20City%20Airbnb%20Price%20Detection/Images/__results___104_5.png?raw=true)

## Conclusion
From the results, we observe that Random Forest Regression (RF) performed the best in terms of RMSE, R² score, MAE, and MSE. It achieved an RMSE of 6.9945, R² score of 0.9967, MAE of 0.915, and MSE of 48.9226, albeit with a longer execution time compared to other models. K-Nearest Neighbors (KNN) and XGBoost also performed well with respectable accuracy and execution times.

## Signature
- **Name:** Aditya D
- **Github:** [https://www.github.com/adi271001](https://www.github.com/adi271001)
- **LinkedIn:** [https://www.linkedin.com/in/aditya-d-23453a179/](https://www.linkedin.com/in/aditya-d-23453a179/)
- **Topmate:** [https://topmate.io/aditya_d/](https://topmate.io/aditya_d/)
- **Twitter:** [https://x.com/ADITYAD29257528](https://x.com/ADITYAD29257528)
