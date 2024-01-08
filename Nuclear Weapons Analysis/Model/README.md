# Nuclear Weapons Data Analysis and Modeling

## Overview

This project involves the analysis of datasets related to nuclear weapons, including exploratory data analysis (EDA) and the application of various machine learning models. The goal is to gain insights into trends over time, clustering patterns, and predictive modeling of nuclear weapons-related features.

## Exploratory Data Analysis (EDA)

### Nuclear Weapons Distribution Over Time (df1)

- Explored the distribution of nuclear weapons-related features over time.
- Conducted basic statistics, including mean, median, and standard deviation.
- Utilized K-Means clustering to identify potential patterns in the data.
- Applied the t-test to compare nuclear weapons stockpiles between different years.

### Relationship Between Features (df2)

- Examined the relationship between various features, including `number_nuclweap_consideration`, `number_nuclweap_pursuit`, and `number_nuclweap_possession`.
- Performed Principal Component Analysis (PCA) to reduce dimensionality.
- Applied the elbow method to find the optimal number of clusters for K-Means.
- Conducted K-Means clustering to group entities based on nuclear weapons-related features.

### Nuclear Weapons Stockpile Trend (df3)

- Analyzed the trend in nuclear weapons stockpiles over time.
- Applied basic statistics to understand the central tendency and dispersion of the data.
- Conducted K-Means clustering to identify potential clusters of countries based on their nuclear weapons stockpiles.

### Nuclear Weapons Tests Over Time (df4)

- Explored the distribution of nuclear weapons tests over time.
- Conducted the t-test to compare the number of nuclear weapons tests between different years.

## Machine Learning Models

### Model Selection

- Chose a variety of machine learning models, including Random Forest, Gradient Boosting, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Logistic Regression, Decision Tree, MLP, and a simple Neural Network using Keras.

### Evaluation and Prediction

- Trained each model on the respective training data and evaluated their performance on the test set.
- Saved the model predictions to CSV files for further analysis.

### Analysis of Model Performance

- Plotted and compared the accuracy of each model on both training and test sets to assess overfitting or underfitting.
- Provided classification reports for each model to understand precision, recall, and F1-score.

 1. ![Nuclear Weapon Proliferation Owid](https://github.com/adi271001/ML-Crate/blob/Nuclear-Weapons-Analysis/Nuclear-Weapons-Analysis-And-Classification/Images/nw18.PNG)
 2. ![Nuclear Weapon Proliferation Total Owid](https://github.com/adi271001/ML-Crate/blob/Nuclear-Weapons-Analysis/Nuclear-Weapons-Analysis-And-Classification/Images/nw19.PNG)
 3. ![Nuclear Weapon Stockpiles](https://github.com/adi271001/ML-Crate/blob/Nuclear-Weapons-Analysis/Nuclear-Weapons-Analysis-And-Classification/Images/nw20.PNG)
 4. ![Nuclear Weapon test states](https://github.com/adi271001/ML-Crate/blob/Nuclear-Weapons-Analysis/Nuclear-Weapons-Analysis-And-Classification/Images/nw21.PNG)

## Concluding Thoughts

- Consideration of features and their importance can guide the selection of predictive variables.
- Regular evaluation and comparison of models are essential to choose the most effective one.
- Models gave highly Accurate Results Ranging from 83.5%-99.96% acroos the 4 data files

## Usage

Feel free to clone or download this repository and adapt the code for your own datasets or analyses.

## Dependencies

- Python 3.x
- Required Python packages (specified in requirements.txt)

