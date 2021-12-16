**Spam Email Detection**

**GOAL**

To build a model that can identify your emails as spam or non-spam

**DATASET**

https://archive.ics.uci.edu/ml/datasets/Spambase

**DESCRIPTION**

In this project we aim to find the most accurate algorithm which correctly categorizes our emails as spam or non-spam. \
For this project we'll be using the *spambase dataset*. This dataset has about 4.6K rows and the each row contains numerical information regarding the email. So there is no need for us to process the data. \

**WHAT I HAD DONE**
1. Load the dataset
2. Analyse the dataset
<u>Since there is no need for data processing</u>
3. Train/Test Split 
4. Selecting A Model
5. Hyperparameter Optimization
6. Generating Predictions
(Optional, recommended)
6. Save the model


**LIBRARIES NEEDED**

- Numpy 
- pandas
- matplotlib
- plotly
- sklearn

**Model Used and Their ACCURACIES**   

<img src="../Images/base_models.png" alt="Accuracies" style="height: 700px; width:1200px;"/>  

**CONCLUSION**

The RandomforestClassifier algorithm has the highest accuracy of ~95% (I tweaked the params later and got the accuracy to 96%), and logistic regression also has has a pretty high accuracy, despite it's simplicity it's a very effective model and this why in many of the classification problems the first approach is always Logistic regression. On the other hand ensembling methods are so powerful in some problems that they can easily have a higher accuracy socre than other algorithms.   
This why we need to try out many algorithms and find out the most optimized solution. 
**NOTE:** *The most optimal solution dosen't always mean the most accurate.*

**CONTRIBUTION BY**  

*Yagyesh Bobde*  

  
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yagyesh-bobde-177523220/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yagyesh-bobde)


