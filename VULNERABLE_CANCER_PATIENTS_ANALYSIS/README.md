**VULNERABLE CANCER PREDICTION**


**GOAL**

To build a deep learning model based on sentimental analysis of text database to evaluate the intensity of sentiment.

**DATASET**

https://www.kaggle.com/datasets/irinhoque/mental-health-insights-vulnerable-cancer-patients



**MODELS USED**
1) Neural Networks
2) LSTM
3) GRU
4) Roberta 


**LIBRARIES**
1) PANDAS
2) NUMPY
3) TENSORFLOW
4) PYTORCH
5) TRANSFORMERS
6) SCIKIT-LEARN


**IMPLEMENTATION**
1) Loaded the dataset with 3 columns having 10000 entries.
2) Started with checking for null values and cleaning textual data from any spaces,capitals,etc which could hamper learning process.
3) Used 4 classes of Positive,neutral,negative,very negative for sentiment analysis
4) Implemented tokenization for conversion of text in suitable sequences.
5) Trained model via different algorithms.
   


...

### Models and Accuracies

| Model                         | Accuracy   | 
| ----------------------------- |:----------:| 
| ROBERTA                       | 0.78(Expected) |                    
| LSTM                          | 0.72       |                    
| Neural Network                | 0.67       |                    
| Logistic Regression           | 0.71       |                    

**NOTE:NO GRAPHS WERE PLOTTED**


**ROBERTA MODEL IN TENSORFLOW AND PYTORCH WERE NOT FULLY TRAINED DUE TO LACK OF RESOURCES ON MY MACHINE,HOWEVER I WILL BE ATTACHING RESULT OF ONLY 1 EPOCH**


**IMAGE**
![Alt Text](./Images/1.png)
...

**NAME**
Keshav Arora
