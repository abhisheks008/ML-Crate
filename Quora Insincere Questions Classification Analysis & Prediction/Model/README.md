# Quora Insicere Questions Analysis

**Task -> Text Classification**

# Datset
There are 3 columns in our train data : 
1. qid - user id
2. question_text - Questions Asked ( Input/Feature layer )
3. target - 0 or 1 ( Target Layer)

# Approach : 
1. Text Exploration : we want to know what kind of values/words links or what exactly is included in the quetions.
2. Text Preprocessing : 
   1. One hot Encoding 
   2. Padding 
   3. Embedding 
3. Creating A Model and Training : 
4. Checking the Accuracy
5. Repeat steps 3 and 4 for a few models.

# Models Used : 
## Deep learning models : 

| Model Structure | Accuracy or Training | 
| ---- | ---- |
| LSTM 100 Neuron Model | ![](Images/../../Images/100%20neuron%20LSTM.png) |
| ![](../Images/NN_1model.png) | ![](Images/../../Images/nn_1.png) |
I stopped training at only 10 epochs becaues I observed that the training accuracy was increasing very slowly and when I increased the nuber of neurons and/or added another LSTM layer the accuracy was pretty much the same but the computational time increased.

**Higest Accuracy Reached with these simple ANN/LSTM models ~ 69%**

## Machine Learning models used : 
1. LogisticRegression: 
![](../Images/log_reg.png)

2. RandomForestClassifier : 75% validation accuracy
![](../Images/random_forest.png)

## RandomForest

But we will probably have different results if take the whole data into account, I mean we only considered a small portion of the dataset right?     


<hr><hr>

**Project By**  
Yagyesh Bobde  
  
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yagyesh-bobde-177523220/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yagyesh-bobde)

<hr><hr>