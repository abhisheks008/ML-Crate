# Federal Grants and Funding Analysis

## Overview
This comprehensive project involves the collection, analysis, and prediction of federal grants and funding opportunities from 2004 to 2024. The project covers a wide range of tasks, including data exploration, machine learning model development, and extensive visualization. The machine learning models implemented in the project have reported accuracies ranging from 71% to 93% for various tasks.

## Contents
1. [Dataset](#dataset)
2. [Features](#features)
3. [Use Case and Analysis Reference](#use-case-and-analysis-reference)
4. [Feature Description](#feature-description)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Machine Learning Models](#machine-learning-models)
7. [Model Evaluation](#model-evaluation)
8. [Visualization](#visualization)

## Dataset
The dataset includes a collection of federal grants and funding opportunities from 2004 to 2024, containing a total of 75,640 opportunities.

## Features
- `opportunity_id`: Primary key of the opportunity.
- `opportunity_title`: The opportunity title.
- `opportunity_number`: The opportunity number.
- `opportunity_category`: The opportunity category.
- `funding_instrument_type`: The funding instrument type.
- `category_of_funding_activity`: The category of funding activity.
- `cfda_numbers`: The Catalog of Federal Domestic Assistance number.
- `eligible_applicants`: The eligible applicants.
- `eligible_applicants_type`: The eligible applicants type.
- `agency_code`: The agency code.
- `agency_name`: The agency name (grant provider).
- `post_date`: The post date of the opportunity.
- `close_date`: The close date of the opportunity.
- `last_updated_date`: The last updated date.
- `archive_date`: The archive date of the opportunity.
- `award_ceiling`: The maximum amount of grant per award.
- `award_floor`: The minimum amount of grant per award.
- `estimated_total_program_funding`: The total grant amount of the program.
- `expected_number_of_awards`: The number of awards who can get the grant.
- `cost_sharing_or_matching_requirement`: Defines if a portion of the project’s cost is not paid by federal funds.
- `additional_information_url`: The additional information.

## Use Case and Analysis Reference
Refer to the notebook "Federal Grants and Funding Analysis" for a use case and analysis reference.

## Feature Description
For detailed descriptions of each feature, refer to the data dictionary provided.

## Exploratory Data Analysis (EDA)
The project involves an extensive Exploratory Data Analysis (EDA) to understand the dynamics of federal grants and funding opportunities. The analysis includes the use of various plots, heatmaps, and statistical measures.

## Machine Learning Models
The project includes the development and evaluation of the following machine learning models:
- Linear Regression (75%)
- Logistic Regression (Accuracy 76%)
- Decision Tree (Accuracy: 75%)
- Random Forest (Accuracy: 76%)
- Support Vector Machine (SVM) (Accuracy: 77%)
- Gradient Boosting (Accuracy: 78%)
- XGBoost (Accuracy: 79%)
- K-Nearest Neighbors (KNN) (Accuracy: 77%)

Each model is trained and evaluated for specific tasks related to federal grants and funding analysis.

![Graph for Accuracies](https://github.com/adi271001/ML-Crate/blob/Federal-Grants/Federal-Grants-and-Funding-Opportunities-Analysis/Images/__results___45_0.png)

## Visualization
Visualization plays a crucial role in understanding the trends and patterns in the data. The project includes the creation of various plots, including violin plots, heatmaps, and network analysis plots.

1. Correlation : ![correlation map](https://github.com/adi271001/ML-Crate/blob/Federal-Grants/Federal-Grants-and-Funding-Opportunities-Analysis/Images/__results___10_0.png)
2. Word Cloud : ![word cloud](https://github.com/adi271001/ML-Crate/blob/Federal-Grants/Federal-Grants-and-Funding-Opportunities-Analysis/Images/__results___12_0.png)
3. Missing Data : ![Missing Data](https://github.com/adi271001/ML-Crate/blob/Federal-Grants/Federal-Grants-and-Funding-Opportunities-Analysis/Images/__results___8_1.png)

