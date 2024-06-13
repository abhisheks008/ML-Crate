# Cement Strength Prediction

This Folder contains the code and resources for predicting the compressive strength of
concrete using various machine learning models. The prediction is based on the ingredients of
concrete, such as cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate,
and fine aggregate.

## Table of Contents

```
Installation
Models and Results
Contributing
```
## Installation

To run the notebook and reproduce the results, you need to have Python installed along with the
necessary libraries. You can install the required libraries using the following command:

```
pip install -r requirements.txt
```

## Models and Results

The project explores the following machine learning models to predict the compressive strength
of concrete:

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
## Contributing

Contributions are welcome! Please read the contribution guidelines first.




