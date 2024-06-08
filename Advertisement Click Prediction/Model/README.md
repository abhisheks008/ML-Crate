## **Advertisement Click Prediction**

### 🎯 **Goal**
The objective is to predict whether a user will click on an advertisement based on various attributes and user inputs from the dataset. By analyzing these features, the aim is to develop a model that accurately forecasts user behavior in response to advertisements.

### 🧵 **Dataset**
Link for the dataset used in the project: [`https://www.kaggle.com/jahnveenarang/cvdcvd-vd`](https://www.kaggle.com/jahnveenarang/cvdcvd-vd)

### 🧾 **Description**
We start with *Exploratory Data Analysis (EDA)* and *Data Visualization* to gain insights from the dataset. Then, we apply various machine learning algorithms to predict whether a user will click on an advertisement. Finally, we compare the accuracies of these algorithms to identify the best-performing model.

### 🧮 **What I had done!**
- Imported essential libraries for data manipulation and machine learning.
- Conducted Exploratory Data Analysis (EDA) to comprehend the dataset.
- Visualized data to extract meaningful patterns and insights.
- Assessed feature correlations to understand interdependencies.
- Converted categorical features into numerical formats via feature mapping.
- Split the dataset into training and testing sets and applied scaling techniques.
- Implemented and trained four machine learning models: **XGBoost**, **Random Forest**, **Gradient Boosting**, and **Multi-Layer Perceptron**.
- Evaluated the models using confusion matrices and compared their accuracies to determine the best-performing model.

### 🚀 **Models Implemented**
Model Building: We implemented the following algorithms for their distinct advantages in handling various aspects of the dataset:

- XGBoost Classifier: Known for its high performance and efficiency in handling large datasets with complex patterns.
- Random Forest Classifier: Effective in reducing overfitting and providing reliable feature importance insights.
- Gradient Boosting: Powerful for capturing intricate data relationships and improving accuracy through boosting techniques.
- Multi-Layer Perceptron: Capable of capturing non-linear relationships due to its deep learning architecture.

### 📚 **Libraries Needed**
- Language Used
  - Python
- Libraries Used
  - Pandas
  - Seaborn
  - Numpy
  - Matplotlib
    
### 📊 **Exploratory Data Analysis Results**
<table>
    <tr>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/gender.png"></td>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/purchased.png"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/age-purchased.png"></td>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/salary-purchased.png"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/box-purchased-salary.png"></td>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/box-purchased-age.png"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/purchased-gender.png"></td>
        <td><img width=70% src='https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/correlation.png'></td>
    </tr>
</table>

### 📈 **Performance of the Models based on the Accuracy Scores**
<table>
    <tr>
        <td style="padding-right: 20px; vertical-align: top;">
            <ul style="list-style-type: disc; margin: 0;">
                <li>XGBoost Classifier - 92%</li>
                <li>RandomForest - 90%</li>
                <li>Gradient Boosting - 90%</li>
                <li>Multi-Layer Perceptron - 87%</li>
            </ul>
        </td>
        <td style="vertical-align: top;">
            <img src="https://github.com/snega16/ML-Crate/blob/snega16/Advertisement%20Click%20Prediction/Images/accuracy.png" alt="Description of image" style="max-width: 200px; max-height: 200px;">
        </td>
    </tr>
</table>


### 📢 **Conclusion**
Among all the models tested, the **XGBoost Classifier** achieved the highest accuracy, approximately **92%**, making it the best-performing model for predicting advertisement clicks. This demonstrates its effectiveness in handling the dataset and providing reliable predictions.

### ✒️ **Your Signature**
Created by [Suraj Kashyap](https://github.com/imsuraj675) as a part of SSOC'24.