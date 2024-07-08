## Term Deposit Campaign Analysis and Classification

--- 

### 🎯 **Goal**

The goal of this project is to analyze a bank marketing campaign dataset and build various machine learning models to predict the success of the campaign. We aim to understand the characteristics of the clients who responded positively and identify patterns that can help improve future marketing strategies.


### 🧾 **Description**

This project involves:
1. Data cleaning and preprocessing.
2. Exploratory Data Analysis (EDA) to uncover insights and patterns.
3. Building and evaluating multiple machine learning models.
4. Comparing model performance based on key metrics.

### 📜 **Repo Structure**

```bash

Term Deposit Prediction
|- Dataset
    |- dataset.csv
    |- README.md
|- Images
    |- img1.png
    |- img2.png
        :
        :
    |- README.md
|- Models
    |- Notebook.ipynb
    |- README.md
|- requirements.txt

```


### 🧮 **What I had done!**

1. **Data Cleaning**: Replaced 'unknown' values with NaN and dropped rows with missing values.
2. **EDA**: Conducted visual and statistical analysis to understand the distribution and relationships of features.
3. **Feature Engineering**: Encoded categorical features and scaled numerical features.
4. **Model Training**: Trained and evaluated several machine learning models
   

### 🚀 **Models Implemented**

- Random Forest
- Decision Tree
- k-Nearest Neighbors (KNN)
- XGBoost
- AdaBoost
- Logistic Regression
- Naive Bayes
- Support Vector Classifier (SVC)


### 📚 **Libraries Needed**

- `numpy`
- `pandas`
- `seaborn`
- `matplotlib`
- `plotly`
- `scikit-learn`


### 📊 **Exploratory Data Analysis Results**

1. **Age Distribution**:
    - Most clients are in the age range of 30-40 years.
    - Age distribution is visualized using a pie chart.

    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/2c7fae04-f030-4e9c-b3e3-e621390a6d2d)


2. **Job Distribution**:
    - The most common job types are blue-collar, management, and technician.
    - Job distribution is visualized using a bar chart.
    
    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/b0d6a595-40c0-46f5-9b2f-3b2ac2728097)


3. **Education Level**:
    - Most clients have a university degree, followed by high school education.
    - Education distribution is visualized using a bar chart.

    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/11d9f16c-7233-4e3d-b7d4-21e387123f92)


4. **Loan Status**:
    - Majority of clients do not have personal loans, housing loans, or defaults.
    - Loan status distribution is visualized using a pie chart.

    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/a14127e0-d8fc-4b78-a9ad-9d573d0ef489)


5. **Marital Status**:
    - Most clients are married, followed by single and divorced.
    - Marital status distribution is visualized using a pie chart.

    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/2de201d4-a4d4-4d4a-8b39-587068057977)


6. **Contact Type**:
    - The preferred contact type is cellular.
    - Contact type distribution is visualized using a histogram.

    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/e6de612d-8229-4aef-93f3-2abcd6ce78a7)


7. **Call Duration**:
    - Total call duration peaks in certain months and days of the week.
    - Call duration by month and day is visualized using line charts.


    <div align='center'>
    <img src='https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/720037be-9dec-412c-9fd2-657298bac6c9' width=600/>
    <img src='https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/82dea548-9d84-479f-9791-f713fcb718a2' width=600/>
    </div>

8. **### Addressing Class Imbalance in the Target Variable Distribution**

    - The histogram shows a significant class imbalance in the target variable 'y', with the 'no' class having approximately 27,000 instances and the 'yes' class having only 3,859 instances.
    - This imbalance indicates that the dataset is heavily skewed towards the 'no' class, which can lead to biased model performance if not addressed properly.
  
    
    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/f2e9ed95-fc66-4ca2-8d55-9ce712ee439b)

    - Adjusting Class Weights: In models that support it, I adjusted the class weights to give more importance to the minority class during training.
    - Evaluation Metrics: Focused on metrics that are sensitive to class imbalance, such as precision, recall, and the F1 score, rather than just accuracy.

9. **Correlation Analysis**:
    - Heatmap reveals the correlation between numerical features.

    ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/2b5505c4-b4c4-4a43-bfe0-87065db6f15a)


### 📈 **Performance of the Models based on the Accuracy Scores**

<div align="center">
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1 Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Random Forest</td>
      <td>87.40%</td>
      <td>0.50</td>
      <td>0.87</td>
      <td>0.64</td>
    </tr>
    <tr>
      <td>Decision Tree</td>
      <td>88.22%</td>
      <td>0.54</td>
      <td>0.52</td>
      <td>0.53</td>
    </tr>
    <tr>
      <td>KNN</td>
      <td>89.07%</td>
      <td>0.61</td>
      <td>0.39</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>XGBoost</td>
      <td>90.11%</td>
      <td>0.63</td>
      <td>0.54</td>
      <td>0.58</td>
    </tr>
    <tr>
      <td>Adaboost</td>
      <td>89.98%</td>
      <td>0.68</td>
      <td>0.40</td>
      <td>0.50</td>
    </tr>
    <tr>
      <td>Logistic Regression</td>
      <td>89.95%</td>
      <td>0.67</td>
      <td>0.41</td>
      <td>0.51</td>
    </tr>
    <tr>
      <td>Naive Bayes</td>
      <td>82.98%</td>
      <td>0.39</td>
      <td>0.57</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>SVC</td>
      <td>89.69%</td>
      <td>0.67</td>
      <td>0.37</td>
      <td>0.48</td>
    </tr>
  </tbody>
</table>
</div>


![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/8ecf69f4-e2da-4ead-8683-0ce3c14ad324)

### 📢 **Conclusion**

- The XGBoost model achieved the highest accuracy and F1 score, making it the best-performing model in this study.
- The exploratory data analysis provided valuable insights into client demographics and behavior patterns.
- The findings from this project can help in optimizing future marketing campaigns and improving client targeting strategies.


### ✒️ **Signature**

<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)
