
# Electric Motor Temperature Analysis


## Goal

The goal of this project is to analyse the Electric Motor Temperature and create a prediction model by which we can predict the temperature of the motors based on the particular parameters.
## Dataset
I have Downloaded this dataset from kaggle website. Here is the link: https://www.kaggle.com/datasets/wkirgsn/electric-motor-temperature

## What Have I Done?

- Imported all the required libraries and dataset for this project.
- Exploratory Data Analysis and Visualizing different aspects of the dataset.
- Finding number of observations and outliers in the dataset.
- Plotting different attributes of the dataset.
- 8 different Models are created for prediction of temperature.
## Library used:
1. numpy.
2. pandas.
3. matplotlib.
4. seaborn.
5. sklearn
6. xgboost
7. lightgbm
8. tensorflow
## Visualization and EDA of different attributes:

![download](https://user-images.githubusercontent.com/97960335/181936004-667a04ca-738a-46c4-a73b-61b03b9aac6f.png)

![download](https://user-images.githubusercontent.com/97960335/181936009-bd55cc3a-6fa8-4b14-9929-4953a0445bef.png)
![download](https://user-images.githubusercontent.com/97960335/181936014-04af0b3b-aedf-4591-946d-88400746b6ed.png)
![download](https://user-images.githubusercontent.com/97960335/181936017-f38e96b2-fbfe-4b6b-91c2-40102db9c71b.png)
![download](https://user-images.githubusercontent.com/97960335/181936020-6764247c-1a6b-4d31-aa21-398b93d42326.png)
![download](https://user-images.githubusercontent.com/97960335/181936024-6d67f016-3831-4a95-98e8-010cebacfeff.png)
![download](https://user-images.githubusercontent.com/97960335/181936027-fab00149-9dee-4c7f-a915-35830e74a468.png)
![download](https://user-images.githubusercontent.com/97960335/181936029-ba7df175-96f4-492a-bc55-52db74268eef.png)
![download](https://user-images.githubusercontent.com/97960335/181936032-cd8ab53d-e039-4298-bcd3-7b1c154a60c7.png)
![download](https://user-images.githubusercontent.com/97960335/181936033-5984671c-1504-43d0-a6b7-d0cbc1e63ccc.png)
![download](https://user-images.githubusercontent.com/97960335/181936034-c81f4e32-b8bc-4369-82e1-62f8e37654b9.png)
![download](https://user-images.githubusercontent.com/97960335/181936035-57d16a51-173b-4d7f-aba1-3ddf1db0a191.png)
![download](https://user-images.githubusercontent.com/97960335/181936036-77a2a222-0f80-4f70-b622-9512f3481625.png)
![download](https://user-images.githubusercontent.com/97960335/181936037-96c788d7-5448-48e0-bccf-7ab1a61c57db.png)

![download](https://user-images.githubusercontent.com/97960335/181936039-6578c352-1809-4402-90e6-be5379da0998.png)
![download](https://user-images.githubusercontent.com/97960335/181936041-dcf9c5dd-3db9-4f74-82d8-d2c810626e1c.png)
![download](https://user-images.githubusercontent.com/97960335/181936045-43046b6c-4f12-4eaa-af14-06c90ca6f4f5.png)
![download](https://user-images.githubusercontent.com/97960335/181936048-834f214e-05fb-4982-9169-d7eea4258eb6.png)
![download](https://user-images.githubusercontent.com/97960335/181936053-a1a8e3cd-761a-47e5-8538-7a294c22de00.png)
![download](https://user-images.githubusercontent.com/97960335/181936056-8771d6e3-d94a-496a-995a-a445d5d4a244.png)
![download](https://user-images.githubusercontent.com/97960335/181936061-7ec5253f-3904-407f-9ee6-14c97244bc6d.png)

![download](https://user-images.githubusercontent.com/97960335/181936064-ea59cc86-7c7e-4726-a174-4ade344ec97e.png)
![download](https://user-images.githubusercontent.com/97960335/181936070-30b6e2e1-17f5-4911-ad8d-8b169c7c1520.png)
![download](https://user-images.githubusercontent.com/97960335/181936072-5b347d62-d028-4bb9-a276-7eb03a89b4aa.png)

![download](https://user-images.githubusercontent.com/97960335/181936078-dd32e2f6-8fd5-43ca-a535-533ec5bc15e3.png)
![download](https://user-images.githubusercontent.com/97960335/181936082-358a0904-eb2a-489d-b795-bb60dc36aece.png)
![download](https://user-images.githubusercontent.com/97960335/181936088-22f0d9e5-6a7a-4007-beb1-054a2c913e63.png)
![download](https://user-images.githubusercontent.com/97960335/181936093-bee59592-5f3d-4ce2-8192-17151ae3927b.png)
![download](https://user-images.githubusercontent.com/97960335/181936098-aeca9c47-0180-40ef-bc17-974c4dfe5282.png)



## Conclusion:
- Highest frequency around (-10)-5 q-component of voltage.
- Highest frequency around 0-19 c Coolant temperature.
- Highest frequency around 60-70 C Stator winding temperature.
- Highest frequency around (-25)-0 Voltage d-component.
- Highest frequency around 40-50 C Stator tooth temperature.
- Highest frequency around 0-250 rpm Motor speed.
- Highest frequency around (-25)-0  Current d-component.
- Highest frequency around (-25)-0 Current q-component.
- Highest frequency around 60-70 C Permanent magnet temperature.
- Highest frequency around 30-40 C Stator yoke temperature.
- Highest frequency around 30-40 C Ambient temperature.
- Highest frequency around  25 Nm Motor torque.
- The eight following Models are created.
  - LinearRegression Algorithm
  - Lasso Regression Algorithm
  - Ridge Regression Algorithm
  - Decision Tree Regression Algorithm
  - K Neighbors Regression Algorithm
  - XGB Regression Algorithm
  - CatBoost Regression Algorithm
  - sequential Algorithm
- LinearRegression Algorithm and Ridge Regression Algorithm are the best fitted Model as they gave the best predicted score.
## Authors

- Created by [@Nirvik07](https://github.com/Nirvik07), HRSoc 2022

