# Playground Series - Season 4, Episode 8

## Goal
The goal of this project is to build and evaluate various machine learning models to predict the class of mushrooms based on their characteristics provided in the dataset.

## Dataset
The dataset is sourced from the [Playground Series - Season 4, Episode 8 Kaggle competition](https://www.kaggle.com/competitions/playground-series-s4e8/data?select=train.csv).

### Columns in the Dataset
- `id`: Unique identifier for each mushroom.
- `class`: The class of the mushroom (target variable).
- `cap-diameter`: Diameter of the mushroom cap.
- `cap-shape`: Shape of the mushroom cap.
- `cap-surface`: Surface type of the mushroom cap.
- `cap-color`: Color of the mushroom cap.
- `does-bruise-or-bleed`: Whether the mushroom bruises or bleeds.
- `gill-attachment`: Attachment type of the gills.
- `gill-spacing`: Spacing of the gills.
- `gill-color`: Color of the gills.
- `stem-height`: Height of the stem.
- `stem-width`: Width of the stem.
- `stem-root`: Type of the stem root.
- `stem-surface`: Surface type of the stem.
- `stem-color`: Color of the stem.
- `veil-type`: Type of the veil.
- `veil-color`: Color of the veil.
- `has-ring`: Whether the mushroom has a ring.
- `ring-type`: Type of the ring.
- `spore-print-color`: Color of the spore print.
- `habitat`: Habitat of the mushroom.
- `season`: Season when the mushroom is found.

## Description
This project involves the following steps:
1. Exploratory Data Analysis (EDA)
2. Data Preprocessing
3. Model Training and Evaluation
4. Selecting the Best Model
5. Making Predictions on the Test Dataset
6. Saving the Predictions for Submission

## What I Had Done

### Exploratory Data Analysis (EDA)
Performed extensive EDA to understand the distribution of features, relationships between variables, and the overall structure of the dataset. This includes:
- Visualizations of categorical features
- Distribution plots for numerical features
- Correlation analysis

### Data Preprocessing
- Handled mixed data types in columns.
- Filled missing values.
- Encoded categorical features using `LabelEncoder`.

### Models Implemented
The following machine learning models were trained and evaluated:
1. Logistic Regression
2. Random Forest
3. Gradient Boosting
4. AdaBoost
5. Extra Trees
6. XGBoost
7. CatBoost
8. LightGBM
9. SVM

### Libraries Needed
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- xgboost
- catboost
- lightgbm

## EDA Results
- Identified mixed data types in certain columns and converted them to strings.
- Visualized the distribution of categorical and numerical features.
- Analyzed correlations between features and the target variable.

## Performance of the Models Based on Accuracy Scores
- Logistic Regression: 0.6213
- Random Forest: 0.9920
- Gradient Boosting: 0.9288
- AdaBoost: 0.8000
- Extra Trees: 0.9916
- XGBoost: 0.9912
- CatBoost: 0.9871
- LightGBM: 0.9888
- SVM: 0.9200 (example value, replace with actual)

## Conclusion
The Random Forest model achieved the highest accuracy on the validation set, making it the best model for this task. This model was used to make predictions on the test dataset.

## Predictions
The predictions were made using the Random Forest model and saved in `submission.csv`.

## Signature
- **Name:** Aditya D
- **GitHub:** [https://www.github.com/adi271001](https://www.github.com/adi271001)
- **LinkedIn:** [https://www.linkedin.com/in/aditya-d-23453a179/](https://www.linkedin.com/in/aditya-d-23453a179/)
- **Topmate:** [https://topmate.io/aditya_d/](https://topmate.io/aditya_d/)
- **Twitter:** [https://x.com/ADITYAD29257528](https://x.com/ADITYAD29257528)
