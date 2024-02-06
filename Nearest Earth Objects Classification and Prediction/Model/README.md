
# Nearest Earth Objects Classification and Prediction


## Goal

The goal of this project is to classify and predict the nearest earth objects from the NASA.
## Dataset
I have Downloaded this dataset from kaggle website. Here is the link: https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects.

## What Have I Done?

- Imported all the required libraries and dataset for this project.
- Exploratory Data Analysis and Visualizing different aspects of the dataset.
- Finding number of observations and outliers in the dataset.
- Plotting different attributes of the dataset.
- Building the machine learning model.

## Library used:
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. xgboost
6. sklearn

## Visualization and EDA of different attributes:

![download](https://user-images.githubusercontent.com/97960335/181153007-5e9f1168-5758-486a-bf7d-e82c0b4e7600.png)

![download](https://user-images.githubusercontent.com/97960335/181153016-b7613d43-be43-47e5-bb48-6564bf88f91d.png)

![download](https://user-images.githubusercontent.com/97960335/181153025-2c1b308a-325a-4c53-aa3c-6c142e285f66.png)

![download](https://user-images.githubusercontent.com/97960335/181153044-c5ea954c-a31c-43d4-bae2-115d966e51fa.png)

![download](https://user-images.githubusercontent.com/97960335/181153078-5b00ba2e-1a04-4ae0-910b-9beedbc5dec9.png)

![download](https://user-images.githubusercontent.com/97960335/181153098-d253f5f3-a0e7-4db6-8630-db69f59a61f5.png)

![download](https://user-images.githubusercontent.com/97960335/181153103-b5c1dcb8-0b58-4421-83fa-f4d5d5f7450c.png)

![download](https://user-images.githubusercontent.com/97960335/181153115-cda10641-498f-4878-bb7d-a06d11052ea8.png)

![download](https://user-images.githubusercontent.com/97960335/181153123-fcd19484-3f44-4d10-a8f2-e8dad2778ffe.png)

![download](https://user-images.githubusercontent.com/97960335/181153149-be2d0b5d-e6e9-4904-8b4c-17315eba3c7d.png)

![download](https://user-images.githubusercontent.com/97960335/181153171-170b95fb-2ab5-4ef3-b9e7-cad4a3717805.png)

![download](https://user-images.githubusercontent.com/97960335/181153185-57d4ab32-d5fb-4b6d-aa46-33b219db5832.png)

![download](https://user-images.githubusercontent.com/97960335/181153205-2f741514-4c04-46f1-abec-1ae6386893c1.png)


## Conclusion:

- Non-hazardousobjects are more than hazardous objects.
- Heatmap on Bivariate Correlation is shown.
- Univariate and Bivariate Analysis is done.
- For bivariate analysis,it seems that hazardous asteroids move slightly faster than non-hazardous ones and we also see that hazardous asteroids actually tend to be further away from earth, which is counter-intuitive.
- Four different types of Models are created.
- Overall, it is clear that both Random Forest classification and Gradient Boosted classification outperformed the Decision Tree and K Nearest Neighbors. They both had very high AUC, accuracy, and recall scores.
- The variable importance plots revealed that the diameter of an asteroid is the main predictor of its danger.
-  We also see from the variable importance plots that the year the asteroid was discovered does impact its hazard classification, possibly due to changing technology at NASA.

## Authors

- Created by [@Nirvik07](https://github.com/Nirvik07), HRSoc 2022

