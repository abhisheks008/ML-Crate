## 🚀 Methodology
1. **Importing Libraries 📚**  
   - Libraries such as NumPy, Pandas, TensorFlow, and others are imported for data manipulation, visualization, and model building.

2. **Loading the Dataset 📓**
   - The training and testing datasets are loaded into dataframes.

3. **Data Preprocessing 📈**
   - Dataset is checked for null values and a comprehensive EDA is done.
   - The training dataset is split into train and test sets.

4. **Model Structure 🚧**
   - Eight models have been trained: 
     - Logistic Regression
     - Decision Tree
     - Random Forest Classifier
     - Support Vector Classifier
     - Gradient Boosting Classifier
     - Guassian NB classifier using the Naive Bayes algorithm
     - K-Nearest Neighbors
     - ANN model using artificial neural networks concepts, dense layers and dropout layers

5. **Training the Models ⬆️**
   - ML models have been trained on the training dataset provided with necessary parameters to improve performance.
   - ANN model has been trained with softmax and ReLu activation functions and sparse_categorical_crossentropy as loss function.

6. **Model Performance 📊**
   - Decision Tree model has a testing accuracy of 87.5, Gradient Boosting model has testing accuracy of 87.6.
   - All other models have a testing accuracy of 100.

## 📈 Model Performance
### Comparison of Accuracy

<img alt="graph" src="./Images/accuracy_comparison_of_models.png">

### Comparison of ROC score:

<img alt="graph" src="./Images/ROC_comparison_of_models.png">


## 📢 Conclusion
- The project explores eight different models for medical recommendation. Each model's performance is evaluated based on accuracy and ROC score.
- The best-performing model has been selected as Support Vector Classifier.
- The Decision Tree and Gradient Boosting models have not achieved as high an accuracy as the other models.
- No overfitting of data has occured as evident from the accuracy on train and test dataset.
