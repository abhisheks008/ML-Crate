# Cement Strength Prediction

## Table of Contents

```
Goal
Dataset
Description
What I Had Done
Installation
Libraries
EDA Results
Models and Results
Conclusion
Contributing
Signature
```

## Goal

To predict compressive strength of concrete using various machine learning models


## Dataset

Link: https://www.kaggle.com/datasets/himalayaashish/cement-strength-dataset/data


## Description

* This Folder contains the code and resources for predicting the compressive strength of concrete using various machine learning models. 
* The prediction is based on the ingredients of concrete, such as cement, blast furnace slag, fly ash, water, superplasticizer, coarse aggregate, and fine aggregate.


## What I had done!
## Installation
* clone the repository using the following command

```
git clone https://github.com/yourusername/cement-strength-prediction.git
cd cement-strength-prediction
```

* To run the notebook and reproduce the results, you need to have Python installed along with the
necessary libraries. You can install the required libraries using the following command:

```
pip install -r requirements.txt
```

* run the jupyter notebook

```
jupyter notebook cement-strength-prediction.ipynb
```

## Libraries Needed

* pandas==1.3.3
* numpy==1.21.2
* matplotlib==3.4.3
* seaborn==0.11.2
* scipy==1.7.1
* statsmodels==0.12.2
* sklearn==0.24.2
* xgboost==1.4.2
* lightgbm==3.2.1
* catboost==0.26.1
* tqdm==4.62.2
* optuna==2.9.1

## Exploratory Data Analysis Results

* ![relationship graphs](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___8_0.png?raw=true)
* ![cluster graphs](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___9_0.png?raw=true)
* ![Pearson correlation Matrix](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___10_0.png?raw=true)
* ![spearman correlation matrix](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___11_0.png?raw=true)
* ![predictive power score](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___12_0.png?raw=true)
* ![line of best fit graphs](https://github.com/adi271001/ML-Crate/blob/cement-strength/Cement%20Strength%20Prediction/images/__results___13_0.png?raw=true)


## Models and Results

The project explores the following machine learning models to predict the compressive strength of concrete:

### 1. Decision Tree Regressor

#### Why this model : Decision trees are easy to interpret and can handle both numerical and categorical data. They can capture non-linear relationships in the data.

```
Results:
MAE Train: 0.0895
MAE Test: 4.2191
R² Train: 0.9959
R² Test: 0.8525
```
### 2. Random Forest Regressor

#### Why this model : Random forests improve on decision trees by reducing overfitting through ensemble learning. They are robust and handle large datasets well.

```
Results:
MAE Train: 1.2639
MAE Test: 3.6031
R² Train: 0.9854
R² Test: 0.9061
```
### 3. Extra Trees Regressor

#### Why this model :  Extra Trees Regressor, similar to Random Forest, but with more randomness in the splitting of nodes. It tends to reduce variance more than a random forest.

```
Results:
MAE Train: 1.2762
MAE Test: 3.5927
R² Train: 0.9852
R² Test: 0.9105
```
### 4. Gradient Boosting Regressor

#### Why this model : Gradient Boosting builds trees sequentially, with each tree trying to correct the errors of the previous one. It is powerful for many regression and classification tasks.

```
Results:
MAE Train: 2.7935
MAE Test: 3.7280
R² Train: 0.9491
R² Test: 0.9071
```
### 5. HistGradient Boosting Regressor

#### Why this model : HistGradient Boosting is a fast, scalable implementation of Gradient Boosting that works well with large datasets.

```
Results:
MAE Train: 1.3844
MAE Test: 3.0658
R² Train: 0.9822
R² Test: 0.9227
```
### 6. XGBoost Regressor

#### Why this model : XGBoost is an optimized implementation of gradient boosting that is efficient and performs well on structured data.

```
Results:
MAE Train: 0.3877
MAE Test: 3.0132
R² Train: 0.9951
R² Test: 0.9266
```
### 7. LGBM Regressor

#### Why this model : LightGBM is a gradient boosting framework that uses tree-based learning algorithms, designed to be distributed and efficient.

```
Results:
MAE Train: 1.3884
MAE Test: 3.0798
R² Train: 0.9822
R² Test: 0.9247
```
### 8. CatBoost Regressor

#### Why this model : CatBoost is a gradient boosting algorithm that handles categorical features automatically and efficiently, often providing high accuracy with minimal parameter tuning.

```
Results:
MAE Train: 1.2125
MAE Test: 2.6963
R² Train: 0.9870
R² Test: 0.9414
```

## Conclusion
After evaluating various machine learning models, it is evident that ensemble methods such as Random Forest, Extra Trees, and gradient boosting techniques like XGBoost, LGBM, and CatBoost perform significantly better than a single decision tree. These models effectively reduce overfitting and provide more accurate predictions due to their ability to capture complex relationships within the data.

- **Best Performing Models:** CatBoost and XGBoost achieved the lowest test MAE and highest R² scores, indicating robust predictive performance.
- **Important Features:** Features such as cement, water, and blast furnace slag were consistently found to be the most influential in predicting the compressive strength of concrete.

## Contributing

Contributions are welcome! Please read the contribution guidelines first.

## Signature
Aditya D
* Github: https://wwww.github.com/adi271001
* LInkedin: https://www.linkedin.com/in/aditya-d-23453a179/
* Topmate: https://topmate.io/aditya_d/
* Twitter: https://x.com/ADITYAD29257528


