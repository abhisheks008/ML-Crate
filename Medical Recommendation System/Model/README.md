# Medical Recommendation System using Machine Learning ALgorithms

## 📝 Abstract

A medical recommendation system is increasingly valuable in today's healthcare landscape due to its ability to enhance personalized care, efficiency, and data-driven decision-making. These systems tailor treatments and recommendations to individual patients based on their unique health data, leading to more effective and personalized care. By automating the analysis of patient data, medical recommendation systems provide healthcare professionals with rapid and actionable insights, reducing the time required for diagnosis and treatment planning. They also ensure consistency and accuracy in medical recommendations, adhering to the latest evidence and guidelines, which can improve diagnosis accuracy and treatment outcomes.

### Project Overview
The Medical Recommendation System project aims to develop a machine learning based model to diagnose a patient on the basis of given symptoms, and propose medications, workouts, diets and precautions.

### Project Directory Structure
```
Medical Recommendation System
|- Dataset
  |- 8 datasets
  |- README.md
|- Images
  |- 16 images
|- Model
  |- medical_recommendation_system.ipynb
  |- README.md
|- README.md
|- requirements.txt
```

### Methodology
1. **Importing Libraries:**  
   - Libraries such as NumPy, Pandas, TensorFlow, and others are imported for data manipulation, visualization, and model building.

2. **Loading the Dataset:**
   - The training and testing datasets are loaded into dataframes.

3. **Data Preprocessing:**
   - Dataset is checked for null values and a comprehensive EDA is done.
   - The training dataset is split into train and test sets.

4. **Model Structure:**
   - Eight models have been trained: 
     - Logistic Regression
     - Decision Tree
     - Random Forest Classifier
     - Support Vector Classifier
     - Gradient Boosting Classifier
     - Guassian NB classifier using the Naive Bayes algorithm
     - K-Nearest Neighbors
     - ANN model using artificial neural networks concepts, dense layers and dropout layers

5. **Training the Models:**
   - ML models have been trained on the training dataset provided with necessary parameters to improve performance.
   - ANN model has been trained with softmax and ReLu activation functions and sparse_categorical_crossentropy as loss function.

6. **Model Performance:**
   - Decision Tree model has a testing accuracy of 87.5, Gradient Boosting model has testing accuracy of 87.6.
   - All other models have a testing accuracy of 100.

### Model Performance
#### Comparison of Accuracy

<img alt="graph" src="./Images/accuracy_comparison_of_models.png">


#### Comparison of ROC score:

<img alt="graph" src="./Images/ROC_comparison_of_models.png">



### Conclusion
- The project explores eight different models for medical recommendation. Each model's performance is evaluated based on accuracy and ROC score.
- The best-performing model has been selected as Support Vector Classifier.
- The Decision Tree and Gradient Boosting models have not achieved as high an accuracy as the other models.
- No overfitting of data has occured as evident from the accuracy on train and test dataset.


## How to Use
Requirements: Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the requirements.txt file.

Download Data: Download the dataset from Kaggle as mentioned in the dataset section of the project.

Run the Jupyter Notebook: Open the provided Jupyter Notebook file and run each cell sequentially. Make sure to update any file paths or configurations as needed for your environment.

Training and Evaluation: Train the models using the provided data and evaluate their performance using metrics such as accuracy.

Interpret Results: Analyze the model's performance using the visualizations and metrics provided in the notebook.


**Name :** **Sebonti Patra**