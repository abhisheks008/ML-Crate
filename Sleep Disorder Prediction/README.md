## Sleep Disorder Prediction using ML & EDA with Web App


[![Open in Streamlit](https://img.shields.io/badge/Open%20with-Streamlit-red?style=for-the-badge&logo=streamlit)](https://sleeeepy.streamlit.app/) [![Open in Colab](https://img.shields.io/badge/Open%20with-Colab-gold?style=for-the-badge&logo=google-colab)](https://colab.research.google.com/drive/1iUNcDuqsTgx5Z3DtTeSxpK-LcyfBJE0Z?usp=sharing)

<p align=center>
  <img src="https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/167ba0cc-b7ec-49fe-b992-d398931d9964" height="400" width="400"/>
</p>


### 🎯 **Goal**

The goal of the this project is to predict sleep disorders based on personal and lifestyle factors using machine learning techniques. Additionally, it aims to provide users with exploratory data analysis (EDA) visualizations to understand sleep health patterns better. By analyzing sleep duration, physical activity, stress levels, BMI, heart rate, and other factors, the project seeks to offer insights into sleep health and facilitate early detection of potential sleep disorders. 

### 🧵 **Dataset**

The dataset used for training and testing the models can be accessed from the [Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)

### 🧾 **Description**

This project is designed to analyze sleep health and lifestyle data to predict sleep disorders and conduct exploratory data analysis (EDA). Through this project, users can input various personal and lifestyle factors such as sleep duration, physical activity level, stress level, BMI category, heart rate, daily walking steps, and blood pressure. Using these inputs, the project employs a Decision Tree Classifier model to predict the likelihood of a sleep disorder.

In addition to the predictive aspect, the project also offers an EDA section where users can explore the dataset visually. This includes visualizations such as gender distribution, BMI category distribution, occupation distribution, average heart rate by age group, average stress activity level by age group, distribution of sleep disorder by gender, distribution of sleep disorder by occupation, and average stress level by occupation. These visualizations provide insights into various factors related to sleep health and lifestyle.


### 📜 **Repo Structure**

```bash
Sleep Disorder Predictor
|- Dataset
  |- data.csv
  |- README.md
|- Images
  |- img1.png
  |- img2.png
       :
       :
  |- README.md
|- Models
  |- Notebook.ipynb
  |- model.h5
  |- README.md
|- Web_app
  |- app.py
  |- data.csv
  |- Demo.mp4
  |- README.md
|- requirements.txt

```


### 🧮 **What I had done!**

- **Data Cleaning**:

    - Load the dataset using pandas and inspect its structure, including the number of rows and columns, and the data types of each column.
    - Check for missing values in the data that may affect model performance.
    - Handle missing values by either removing them, imputing them with mean or median values, or using more advanced techniques like interpolation or prediction.

- **Exploratory Data Analysis (EDA)**:
    - The EDA phase involves exploring the dataset's characteristics and relationships between variables.
    - Visualizations such as pie charts, histograms, box plots, and line plots are used to analyze distributions, correlations, and trends in the data.
    - Key aspects examined include gender distribution, occupation distribution, age distribution, sleep duration by gender, average heart rate by age group, and average stress level by age group.

- **Data Preprocessing**:
    - Data preprocessing steps are implemented to prepare the dataset for model training.
    - Categorical variables are encoded using one-hot encoding or label encoding to convert them into numerical representations.
    - Numerical features are standardized using techniques like z-score normalization to ensure they are on a similar scale

- **Training ML Classifiers**:
    - Several machine learning classifiers are trained on the preprocessed data to predict sleep disorders.
    - Models such as Decision Trees, Random Forests, Logistic Regression, SVM, KNN, and Gaussian Naive Bayes are trained and evaluated for their predictive performance.
    - Model accuracies are calculated, and a line chart is created to visualize the accuracy of each model.

- **Training ANN Model**:
    - An Artificial Neural Network (ANN) model is built and trained using TensorFlow and Keras.
    - The neural network architecture includes multiple layers with appropriate activation functions and regularization techniques.- The model is compiled with an optimizer, loss function, and evaluation metric before training on the preprocessed data.

- **Evaluation and Comparison**:

    The performance of both traditional machine learning classifiers and the ANN model is compared using accuracy metrics.

-  **Building Streamlit Application**:
    - After training and evaluating machine learning models, the project proceeds to build a user-friendly Streamlit application for practical use.
    - The Streamlit app provides an intuitive interface for users to input their sleep-related information, such as sleep duration, physical activity level, stress level, BMI category, heart rate, daily steps, and blood pressure.
    - Users can interact with sliders and input fields to input their data, and the application dynamically updates based on user input.

    ![image](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/6b1a70c3-aaa0-46d6-8c36-d68d54d8cb58)

    - Upon submission of user data, the trained machine learning model predicts the likelihood of sleep disorders based on the input features.

   ![image](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/f31dea03-67c5-4ec0-9df5-b37eb2b70b9c)



### 🚀 **Models Implemented**

- Decision Tree Classifier
- Random Forest Classifier
- Logistic Regression
- K Nearest Neighbor Classifier
- Support Vector Machine Classifier
- Gaussian Naive Bayes Classifier
- Simple Artificial Neural Network (Feed Forward Neural Network)


### 📚 **Libraries Needed**

- TensorFlow
- Streamlit
- Numpy
- Pandas
- Seaborn
- Sklearn
- Matplotlib
- Plotly Graph Objects

### 📊 **Exploratory Data Analysis Results**


<p align="center">
<img src="https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/c39e467f-c9f2-4ba2-8b01-d82120485d15" width=500 />


<img src="https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/24ff44a0-2a9f-4f69-ad1b-e16a040db7d1" width=500/>
</p>



![newplot (23)](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/74c833f6-4d79-485b-a7d9-e263b2bc2d83)

![newplot (24)](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/11043155-cfb2-4c2b-9473-54e760d4a3bb)

![newplot (20)](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/d5170625-6045-4389-9ea9-65335bcc5f98)

![newplot (19)](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/42e49ae0-80cb-4a8e-8783-271a0bc61559)

### 🎥 Demo




### ⚙️ **Usage**

1. **Exploring Notebooks**: Navigate to the `Models/` directory to explore Jupyter notebooks. These notebooks cover data analysis, preprocessing, model training, and evaluation steps.
   -  Navigate to the `Models/Notebook.ipynb`
   -  Run all the cells

2. **Trained Models**: The `Models/` directory contains trained Deep Learning model saved in HDF5 format. This model can be loaded and used for making predictions.

3. **Streamlit App:** The `Web_app/app.py` contains the source code for the Streamlit web application. To run the app locally, follow the instructions below:

    ```bash
    pip install -r requirements.txt
    cd Web_app
    streamlit run app.py
    ```

    
### 📈 **Performance of the Models based on the Accuracy Scores**



<div align="center">
<table>
  <tr>
    <th>Model</th>
    <th>Validation Accuracy</th>
  </tr>
  <tr>
    <td>Decision Tree</td>
    <td>88.0%</td>
  </tr>
  <tr>
    <td>Random Forest</td>
    <td>88.0%</td>
  </tr>
  <tr>
    <td>Logistic Regression</td>
    <td>88.0%</td>
  </tr>
    <tr>
    <td>Gaussian Naive Bayes</td>
    <td>88.0%</td>
  </tr>  
  <tr>
    <td>KNN</td>
    <td>86.67%</td>
  </tr>
  <tr>
    <td>ANN</td>
    <td>86.67%</td>
  </tr>  
  <tr>
    <td>SVM</td>
    <td>64.0%</td>
  </tr>
</table>
</div>

![](https://github.com/Sgvkamalakar/SnoozeMonitor/assets/103712713/5b7f8211-6b6d-439c-a1ba-a5b802ea6de4)


### 📢 **Conclusion**

- Decision Tree, Random Forest, Logistic Regression, and Gaussian Naive Bayes achieved comparable accuracies of 88%. These models demonstrate robustness and effectiveness in capturing patterns within the dataset.

- K-Nearest Neighbors (KNN) and Artificial Neural Network (ANN) also performed well with an accuracy of approximately 86.67%, indicating its suitability for classification tasks where instances are grouped based on similarity.

- However, the Support Vector Machine (SVM) model lagged behind with an accuracy of 64%, suggesting potential challenges in properly separating the data points in the feature space.

Overall, the decision tree-based models, Random Forest and Decision Tree, along with Logistic Regression and Gaussian Naive Bayes, exhibit promising performance and could be considered as strong candidates for further evaluation and deployment, while further optimization may be necessary for SVM to enhance its performance.


### ✒️ **Signature**

<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)
