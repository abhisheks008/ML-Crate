## **Advertisement Click Prediction**

### 🎯 **Goal**
To explore the intricate dance between gold prices and key economic events across major global players – Canada, Japan, USA, Russia, European Union, and China. 

### 🧵 **Dataset**
Link for the dataset used in the project: ['https://www.kaggle.com/datasets/fekihmea/the-effect-of-economic-news-on-gold-prices'](https://www.kaggle.com/datasets/fekihmea/the-effect-of-economic-news-on-gold-prices)

### 🧾 **Description**
Start with *Exploratory Data Analysis (EDA)* and *Data Visualization* to gain insights from the dataset. Then, we apply various machine learning algorithms to predict the change in the price of Gold based on the sentiment of the Event. Finally, we compare the accuracies of these algorithms to identify the best-performing model.

### 🧮 **What I had done!**
- Imported essential libraries for data manipulation and machine learning.
- Conducted Exploratory Data Analysis (EDA) to comprehend the dataset.
- Visualized data to extract meaningful patterns and insights.
- Setup a function to assign Sentiment to a Event
- Assessed feature correlations to understand interdependencies.
- Converted categorical features into numerical formats via feature mapping.
- Split the dataset into training and testing sets and applied scaling techniques.
- Implemented and trained four machine learning models: **Random Forest**, **SVM**, **Logistic Regression**, and **Gradient Booster**.
- Evaluated the models using classification report and compared their accuracies to determine the best-performing model.

### 🚀 **Models Implemented**
Model Building: We implemented the following algorithms for their distinct advantages in handling various aspects of the dataset:

- Random Forest Classifier: Random forests or Random Decision Trees is a collaborative team of decision trees that work together to provide a single output.
- SVM: Support vector machines are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis.
- Logistic Regression: Logistic regression is a supervised machine learning algorithm used for classification tasks where the goal is to predict the probability that an instance belongs to a given class or not.
- Gradient Booster: Gradient Boosting is a powerful boosting algorithm that combines several weak learners into strong learners, in which each new model is trained to minimize the loss function such as mean squared error or cross-entropy of the previous model using gradient descent

### 📚 **Libraries Needed**
- Language Used
  - Python
- Libraries Used
  - Pandas
  - Seaborn
  - Numpy
  - Matplotlib
  - Sklearn
    
### 📊 **Exploratory Data Analysis Results**

### 📊 **Exploratory Data Analysis Results**

<table>
    <tr>
        <td><img src="https://github.com/fspzar123/ML-Crate/blob/48ce7189e52355c9ef268a87d9d4d160dbc55b28/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/Weekly-Gold.png" alt="Weekly Gold Prices"></td>
        <td><img src="https://github.com/fspzar123/ML-Crate/blob/22465f62c53b71fd029d4c1b350ae3bd1eda3f1f/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/Avg%20Price%20by%20country.png" alt="Average Price by Country"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/fspzar123/ML-Crate/blob/22465f62c53b71fd029d4c1b350ae3bd1eda3f1f/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/Dist%20of%20price%20by%20country.png" alt="Distribution of Price by Country"></td>
        <td><img src="https://github.com/fspzar123/ML-Crate/blob/22465f62c53b71fd029d4c1b350ae3bd1eda3f1f/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/Trend%20of%20Price%26Vol_K.png" alt="Trend of Price and Volume"></td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><img src="https://github.com/fspzar123/ML-Crate/blob/22465f62c53b71fd029d4c1b350ae3bd1eda3f1f/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/HeatMap%20Of%20Correlation.png" alt="Heatmap of Correlation" style="width: 70%;"></td>
    </tr>
    <tr>
        <td colspan="2" style="text-align: center;"><img src="https://github.com/fspzar123/ML-Crate/blob/22465f62c53b71fd029d4c1b350ae3bd1eda3f1f/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/Dist%20of%20events%20per%20date.png" alt="Distribution of events per date" style="width: 70%;"></td>
    </tr>
</table>

### 📈 **Performance of the Models based on the Accuracy Scores**

<table>
    <tr>
        <td style="padding-right: 20px; vertical-align: top;">
            <ul style="list-style-type: disc; margin: 0;">
                <li>Random Forest Classifier - 99.5%</li>
                <li>Support Vector Machines - 97.5%</li>
                <li>Logistic Regression - 97%</li>
                <li>Gradient Booster - 100%</li>
            </ul>
        </td>
        <td style="vertical-align: top;">
            <img src="https://github.com/fspzar123/ML-Crate/blob/22465f62c53b71fd029d4c1b350ae3bd1eda3f1f/The%20Effect%20of%20Economic%20News%20on%20Gold%20Prices%20Analysis/Images/Accuracies%20of%20Models.png" alt="Accuracies of Models" style="max-width: 200px; max-height: 200px;">
        </td>
    </tr>
</table>


### 📢 **Conclusion**
Among all the models tested, the **Gradient Booster** achieved the highest accuracy, approximately **100%**, making it the best-performing model for predicting gold prices. This demonstrates its effectiveness in handling the dataset and providing reliable predictions.

### ✒️ **Your Signature**
Created by [Filbert Shawn](https://github.com/fspzar123) as a part of SSOC'24 Season 3.
