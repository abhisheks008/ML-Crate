# E-commerce Shipping Analysis

## Goal
The goal of this project is to analyze and predict whether an e-commerce shipment will reach on time based on various features. Different data preprocessing techniques and machine learning models were used to find the best performing model.

## Dataset
The dataset used in this project involves e-commerce shipment details with the target variable `Reached.on.Time_Y_N`.

## Description
This project involves training and evaluating 10 different machine learning models on four different preprocessed datasets. The models' performance is assessed using confusion matrices and accuracy scores.

## What I Had Done
1. Preprocessed the data using different techniques:
   - Non-PCA and outliers deleted data.
   - Non-PCA and winsorized data.
   - PCA and outliers deleted data.
   - PCA and winsorized data.
2. Trained 10 different machine learning models on each preprocessed dataset.
3. Evaluated the models using confusion matrices and accuracy scores.
4. Visualized the results using bar plots for accuracy scores and heatmaps for confusion matrices.
5. Saved the predictions to CSV files for further analysis.

## Models Implemented
1. Random Forest
2. Logistic Regression
3. Gradient Boosting
4. AdaBoost
5. CatBoost
6. LightGBM
7. XGBoost
8. Extra Trees
9. K-Nearest Neighbors
10. Decision Tree

## Libraries Needed
- `matplotlib`
- `seaborn`
- `pandas`
- `sklearn`
- `catboost`
- `lightgbm`
- `xgboost`

## EDA Results
- We can see that most of our shipments is not on time (on time: 4436, not on time: 6563). In mode of shipment, ship is dominating that category so we can interpret this probably most of our 
  not on time shipment is coming from "ship" because they are slower than other methods.
- Customer who had 6 or 7 times customer care calls has more delivery on time probability.
- Customer who had 4-6 times prior purchases has more delivery on time probability.
- Customers who received a discount of more than 10 dollars did not receive on time delivery. This feature will be important for us for prediction.
- 2000 - 4000 and 6000+ gram products are not delivered on time every time.
- Delivered on time products' weights changing between 1000-2000 and 4000-6000 grams.
- Correllation matrix shows relationships among features. We interpreted that if we give more than 10 dollar discount to our customer, this order probably will not be on time.
- As you can see there is a correalation between reached on time and discount offered. When discount offered is going up, reaching on time going down. That might be seems wrong to you but as 
  you know 1: NOT reached on time, 0: Reached on time.
- Cost of product and customer care calls have more strong relationship compared to other relationships. That means if our costumer pays more money for product, they have tendecy to have more 
  customer care callls.
- It seems like we have a lot of outliers for discount offered but we might have some outliers for other features as well. Let's find them with z_score!
-  the most number of outliers in "discount_offered" column. I will use 2 method to handle with outliers; First, I will drop them from our data. Also, I will try to solve that problem with 
   winsorize so we can compare at the end which data set giving better results for prediction.

![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___6_0.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___6_10.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___6_2.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___6_4.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___6_6.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___6_8.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___8_1.png?raw=true)
![eda imag 1](https://github.com/adi271001/ML-Crate/blob/e-commerce-shipping/E-commerce%20Shipping%20Data%20Analysis/Images/__results___16_1.png?raw=true)


## Performance of the Models based on Accuracy Scores

### Non-PCA and Outliers Deleted Data
- **Random Forest**
  - Confusion Matrix:
    ```plaintext
    [[ 814, 1014]
     [ 131, 1318]]
    ```
  - Train Accuracy: `0.7036`
  - Test Accuracy: `0.6506`

- **Logistic Regression**
  - Confusion Matrix:
    ```plaintext
    [[1172,  656]
     [ 615,  834]]
    ```
  - Train Accuracy: `0.5954`
  - Test Accuracy: `0.6121`

- **Gradient Boosting**
  - Confusion Matrix:
    ```plaintext
    [[ 844,  984]
     [ 152, 1297]]
    ```
  - Train Accuracy: `0.6958`
  - Test Accuracy: `0.6533`

- **AdaBoost**
  - Confusion Matrix:
    ```plaintext
    [[ 978,  850]
     [ 325, 1124]]
    ```
  - Train Accuracy: `0.6555`
  - Test Accuracy: `0.6414`

- **CatBoost**
  - Confusion Matrix:
    ```plaintext
    [[ 996,  832]
     [ 362, 1087]]
    ```
  - Train Accuracy: `0.8320`
  - Test Accuracy: `0.6356`

- **LightGBM**
  - Confusion Matrix:
    ```plaintext
    [[1009,  819]
     [ 376, 1073]]
    ```
  - Train Accuracy: `0.8444`
  - Test Accuracy: `0.6353`

- **XGBoost**
  - Confusion Matrix:
    ```plaintext
    [[1106,  722]
     [ 541,  908]]
    ```
  - Train Accuracy: `0.9137`
  - Test Accuracy: `0.6146`

- **Extra Trees**
  - Confusion Matrix:
    ```plaintext
    [[1144,  684]
     [ 595,  854]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6097`

- **K-Nearest Neighbors**
  - Confusion Matrix:
    ```plaintext
    [[1135,  693]
     [ 570,  879]]
    ```
  - Train Accuracy: `0.7518`
  - Test Accuracy: `0.6146`

- **Decision Tree**
  - Confusion Matrix:
    ```plaintext
    [[1164,  664]
     [ 642,  807]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6015`

### Non-PCA and Winsorized Data
- **Random Forest**
  - Confusion Matrix:
    ```plaintext
    [[1181,  982]
     [ 128, 1339]]
    ```
  - Train Accuracy: `0.7181`
  - Test Accuracy: `0.6942`

- **Logistic Regression**
  - Confusion Matrix:
    ```plaintext
    [[1489,  674]
     [ 638,  829]]
    ```
  - Train Accuracy: `0.6336`
  - Test Accuracy: `0.6386`

- **Gradient Boosting**
  - Confusion Matrix:
    ```plaintext
    [[1245,  918]
     [ 206, 1261]]
    ```
  - Train Accuracy: `0.7210`
  - Test Accuracy: `0.6904`

- **AdaBoost**
  - Confusion Matrix:
    ```plaintext
    [[1346,  817]
     [ 328, 1139]]
    ```
  - Train Accuracy: `0.6882`
  - Test Accuracy: `0.6846`

- **CatBoost**
  - Confusion Matrix:
    ```plaintext
    [[1361,  802]
     [ 419, 1048]]
    ```
  - Train Accuracy: `0.8590`
  - Test Accuracy: `0.6636`

- **LightGBM**
  - Confusion Matrix:
    ```plaintext
    [[1372,  791]
     [ 423, 1044]]
    ```
  - Train Accuracy: `0.8685`
  - Test Accuracy: `0.6656`

- **XGBoost**
  - Confusion Matrix:
    ```plaintext
    [[1480,  683]
     [ 523,  944]]
    ```
  - Train Accuracy: `0.9343`
  - Test Accuracy: `0.6678`

- **Extra Trees**
  - Confusion Matrix:
    ```plaintext
    [[1469,  694]
     [ 615,  852]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6394`

- **K-Nearest Neighbors**
  - Confusion Matrix:
    ```plaintext
    [[1483,  680]
     [ 579,  888]]
    ```
  - Train Accuracy: `0.7780`
  - Test Accuracy: `0.6532`

- **Decision Tree**
  - Confusion Matrix:
    ```plaintext
    [[1562,  601]
     [ 713,  754]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6380`

### PCA and Outliers Deleted Data
- **Random Forest**
  - Confusion Matrix:
    ```plaintext
    [[ 982,  846]
     [ 393, 1056]]
    ```
  - Train Accuracy: `0.7075`
  - Test Accuracy: `0.6219`

- **Logistic Regression**
  - Confusion Matrix:
    ```plaintext
    [[1181,  647]
     [ 637,  812]]
    ```
  - Train Accuracy: `0.6039`
  - Test Accuracy: `0.6082`

- **Gradient Boosting**
  - Confusion Matrix:
    ```plaintext
    [[ 965,  863]
     [ 339, 1110]]
    ```
  - Train Accuracy: `0.6958`
  - Test Accuracy: `0.6332`

- **AdaBoost**
  - Confusion Matrix:
    ```plaintext
    [[1018,  810]
     [ 449, 1000]]
    ```
  - Train Accuracy: `0.6489`
  - Test Accuracy: `0.6158`

- **CatBoost**
  - Confusion Matrix:
    ```plaintext
    [[1044,  784]
     [ 441, 1008]]
    ```
  - Train Accuracy: `0.8112`
  - Test Accuracy: `0.6262`

- **LightGBM**
  - Confusion Matrix:
    ```plaintext
    [[1046,  782]
     [ 457,  992]]
    ```
  - Train Accuracy: `0.8199`
  - Test Accuracy: `0.6219`

- **XGBoost**
  - Confusion Matrix:
    ```plaintext
    [[1119,  709]
     [ 565,  884]]
    ```
  - Train Accuracy: `0.8997`
  - Test Accuracy: `0.6112`

- **Extra Trees**
  - Confusion Matrix:
    ```plaintext
    [[1186,  642]
     [ 663,  786]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6096`

- **K-Nearest Neighbors**
  - Confusion Matrix:
    ```plaintext
    [[1170,  693]
     [ 644,  782]]
    ```
  - Train Accuracy: `0.7460`
  - Test Accuracy: `0.6104`

- **Decision Tree**
  - Confusion Matrix:
    ```plaintext
    [[1145,  657]
     [ 663,  786]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6018`

### PCA and Winsorized Data
- **Random Forest**
  - Confusion Matrix:
    ```plaintext
    [[1196,  815]
     [ 489, 1012]]
    ```
  - Train Accuracy: `0.7172`
  - Test Accuracy: `0.6752`

- **Logistic Regression**
  - Confusion Matrix:
    ```plaintext
    [[1184,  701]
     [ 634,  849]]
    ```
  - Train Accuracy: `0.6039`
  - Test Accuracy: `0.6096`

- **Gradient Boosting**
  - Confusion Matrix:
    ```plaintext
    [[1142,  742]
     [ 457, 1050]]
    ```
  - Train Accuracy: `0.6983`
  - Test Accuracy: `0.6806`

- **AdaBoost**
  - Confusion Matrix:
    ```plaintext
    [[1210,  698]
     [ 447, 1042]]
    ```
  - Train Accuracy: `0.6688`
  - Test Accuracy: `0.6702`

- **CatBoost**
  - Confusion Matrix:
    ```plaintext
    [[1196,  769]
     [ 542,  935]]
    ```
  - Train Accuracy: `0.8554`
  - Test Accuracy: `0.6888`

- **LightGBM**
  - Confusion Matrix:
    ```plaintext
    [[1210,  787]
     [ 503,  974]]
    ```
  - Train Accuracy: `0.8706`
  - Test Accuracy: `0.6938`

- **XGBoost**
  - Confusion Matrix:
    ```plaintext
    [[1225,  740]
     [ 518,  959]]
    ```
  - Train Accuracy: `0.9093`
  - Test Accuracy: `0.6612`

- **Extra Trees**
  - Confusion Matrix:
    ```plaintext
    [[1182,  701]
     [ 644,  757]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.5996`

- **K-Nearest Neighbors**
  - Confusion Matrix:
    ```plaintext
    [[1132,  785]
     [ 548,  839]]
    ```
  - Train Accuracy: `0.7567`
  - Test Accuracy: `0.6260`

- **Decision Tree**
  - Confusion Matrix:
    ```plaintext
    [[1224,  687]
     [ 651,  788]]
    ```
  - Train Accuracy: `1.0000`
  - Test Accuracy: `0.6040`
 
## Conclusion
The analysis of various machine learning models on different preprocessed datasets shows that models like XGBoost and CatBoost generally performed better in terms of accuracy. However, it's important to consider both training and test accuracy, as high training accuracy with low test accuracy could indicate overfitting. The project demonstrates the impact of different preprocessing techniques on model performance, providing valuable insights for future enhancements and improvements in e-commerce shipping predictions.

## Signature
Aditya D
* Github: [https://www.github.com/adi271001](https://www.github.com/adi271001)
* LinkedIn: [https://www.linkedin.com/in/aditya-d-23453a179/](https://www.linkedin.com/in/aditya-d-23453a179/)
* Topmate: [https://topmate.io/aditya_d/](https://topmate.io/aditya_d/)
* Twitter: [https://x.com/ADITYAD29257528](https://x.com/ADITYAD29257528)

