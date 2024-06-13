# Models Overview and Analysis

This folder contains the code and resources for the various machine learning models used to
predict the compressive strength of concrete. Each model is evaluated based on its performance
metrics and visualizations.

## Table of Contents

```
Models
Performance Metrics
Visualizations
Conclusion
```
## Models

### 1. Decision Tree Regressor

```
Results:
MAE Train: 0.0895
MAE Test: 4.2191
R² Train: 0.9959
R² Test: 0.8525
```
### 2. Random Forest Regressor

```
Results:
MAE Train: 1.2639
MAE Test: 3.6031
R² Train: 0.9854
R² Test: 0.9061
```
### 3. Extra Trees Regressor

```
Results:
MAE Train: 1.2762
MAE Test: 3.5927
R² Train: 0.9852
R² Test: 0.9105
```
### 4. Gradient Boosting Regressor

```
Results:
MAE Train: 2.7935
MAE Test: 3.7280
R² Train: 0.9491
R² Test: 0.9071
```
### 5. HistGradient Boosting Regressor

```
Results:
MAE Train: 1.3844
MAE Test: 3.0658
R² Train: 0.9822
R² Test: 0.9227
```
### 6. XGBoost Regressor

```
Results:
MAE Train: 0.3877
MAE Test: 3.0132
R² Train: 0.9951
R² Test: 0.9266
```
### 7. LGBM Regressor

```
Results:
MAE Train: 1.3884
MAE Test: 3.0798
R² Train: 0.9822
R² Test: 0.9247
```
### 8. CatBoost Regressor

```
Results:
MAE Train: 1.2125
MAE Test: 2.6963
R² Train: 0.9870
R² Test: 0.9414
```
## Performance Metrics

The models were evaluated using the following metrics:

```
Mean Absolute Error (MAE): Measures the average magnitude of errors in predictions.
R² Score: Indicates the proportion of variance in the dependent variable predictable from
the independent variables.
```
## Visualizations

The notebook includes several plots to visualize the performance of the models, such as:

```
Feature Importance: Highlights the most influential features for each model.
Prediction vs Actual: Compares predicted compressive strengths with actual values.
Residuals Plot: Shows the residual errors for each model.
```

![Prediciton vs Actual](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___25_0.png?raw=true)
![Residuals](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___26_0.png?raw=true)
![Tuned-Predicted vs Actual](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___32_0.png?raw=true)
![Tuned-Residuals](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___33_0.png?raw=true)

### Feature Importance

Feature importance visualizations highlight the significant features affecting the compressive
strength predictions for each model.

### Prediction vs Actual

These plots compare the predicted values against the actual values, providing insight into the
models' accuracy.

### Residuals Plot

Residuals plots show the errors of predictions, helping to identify any patterns that the models
may have missed.

## Conclusion

The models demonstrate varying levels of eff ectiveness in predicting concrete strength.
Ensemble methods like Random Forest, Extra Trees, and Gradient Boosting generally provide
better performance compared to individual models like Decision Tree Regressor. CatBoost and
XGBoost show competitive performance with superior accuracy. The results highlight the
importance of feature selection and model tuning in achieving optimal predictive accuracy.



