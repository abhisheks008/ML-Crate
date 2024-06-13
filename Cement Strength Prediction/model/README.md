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
Description: A non-parametric model that splits the data into subsets based on feature
values.
Results:
MAE Train: 0.
MAE Test: 4.
R² Train: 0.
R² Test: 0.
```
### 2. Random Forest Regressor

```
Description: An ensemble method that builds multiple decision trees and merges their
results.
Results:
MAE Train: 1.
MAE Test: 3.
R² Train: 0.
R² Test: 0.
```
### 3. Extra Trees Regressor

```
Description: An ensemble method that fits multiple decision trees on various sub-samples
of the dataset.
Results:
MAE Train: 1.
MAE Test: 3.
R² Train: 0.
```

```
R² Test: 0.
```
### 4. Gradient Boosting Regressor

```
Description: An ensemble technique that builds trees sequentially, correcting errors from
previous trees.
Results:
MAE Train: 2.
MAE Test: 3.
R² Train: 0.
R² Test: 0.
```
### 5. HistGradient Boosting Regressor

```
Description: A fast, histogram-based version of gradient boosting.
Results:
MAE Train: 1.
MAE Test: 3.
R² Train: 0.
R² Test: 0.
```
### 6. XGBoost Regressor

```
Description: An optimized implementation of gradient boosting.
Results:
MAE Train: 0.
MAE Test: 3.
R² Train: 0.
R² Test: 0.
```
### 7. LGBM Regressor

```
Description: A gradient boosting framework that uses tree-based learning algorithms.
Results:
MAE Train: 1.
MAE Test: 3.
R² Train: 0.
R² Test: 0.
```
### 8. CatBoost Regressor

```
Description: A gradient boosting algorithm that handles categorical features automatically
and efficiently.
Results:
MAE Train: 1.
```

```
MAE Test: 2.
R² Train: 0.
R² Test: 0.
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

![Alt text](url_to_image "Optional title")
![Alt text](url_to_image "Optional title")
![Alt text](url_to_image "Optional title")
![Alt text](url_to_image "Optional title")
![Alt text](url_to_image "Optional title")

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



