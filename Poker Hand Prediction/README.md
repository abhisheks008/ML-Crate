## **Poker Hand Prediction**

### 🎯 **Goal**

To predict the most likely poker hand present with at least one of the players in the game, given the sequence of 5 'community' cards drawn from a standard deck.

### 🧵 **Dataset**

The dataset is acquired from UCI's Machine Learning repository. Find it [here](https://archive.ics.uci.edu/ml/datasets/Poker+Hand).

### 🧾 **Description**

Texas Hold 'Em is played by dealing each player 2 'hole' cards (face down) and 5 'community' cards (face up) on the table. The player makes a poker hand using any combination of the 2 cards dealt to them and the 5 cards on the table. The objective is to predict the rank of the poker hand that is most likely to be present among the players, given the 5 community cards.

### 🧮 **What I had done!**

1. **Data Acquisition**: Downloaded the dataset from UCI's Machine Learning repository.
2. **Data Preprocessing**: Cleaned and prepared the data for analysis.
3. **Model Selection**: Implemented various machine learning models to predict poker hands.
4. **Model Training**: Trained the models on the training dataset.
5. **Model Evaluation**: Evaluated the models on the testing dataset.
6. **Performance Comparison**: Compared the accuracy of different models to determine the best one.

### 🚀 **Models Implemented**

1. **Linear Regression**: Basic model to establish a baseline.
2. **Support Vector Machine (SVM)**: Chosen for its effectiveness in classification tasks.
3. **Adaboost**: Implemented to improve model performance through boosting.
4. **Output Code Classifier**: Used for multiclass classification.
5. **Random Forest**: Chosen for its robustness and ensemble learning capabilities.
6. **Artificial Neural Network (ANN)**: Implemented for its potential in capturing complex patterns.
7. **Deep Neural Network (DNN)**: Used for its ability to learn from large datasets.
8. **Multi-Layer Perceptron (MLP)**: Chosen for its superior performance in the dataset.

### 📚 **Libraries Needed**

- numpy
- pandas
- scikit-learn
- tensorflow
- matplotlib
- seaborn

### 📊 **Exploratory Data Analysis Results**

![EDA Result 1](https://github.com/aviralgarg05/ML-Crate/blob/main/Poker%20Hand%20Prediction/Images/ANN.png)
![EDA Result 2](https://github.com/aviralgarg05/ML-Crate/blob/main/Poker%20Hand%20Prediction/Images/DNN.png)

### 📈 **Performance of the Models based on the Accuracy Scores**

| Model | Accuracy |
| :---: | :------: |
| Linear Regression | 42% |
| SVM | 58% | 
| Adaboost | 49% | 
| Output Code Classifier | 61% | 
| Random Forest | 56% | 
| Artificial Neural Network | 45% | 
| Deep Neural Network | 87% |
| Multi-Layer Perceptron | 97% |

### 📢 **Conclusion**

The Multi-layer Perceptron (MLP) is clearly the best model for the dataset in hand, achieving an accuracy of 97%. This indicates that MLP is highly effective in predicting the poker hands given the community cards.

### ✒️ **Your Signature**

**Aviral Garg**

[LinkedIn](https://www.linkedin.com/in/aviral-garg-b7b053280/)