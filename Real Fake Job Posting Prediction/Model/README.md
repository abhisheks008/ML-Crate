# Project Title : Real / Fake Job Posting Prediction
<!-- cover image -->

<hr>

## Abstract/Brief Description about the Project:
This dataset contains 18K job descriptions out of which about 800 are fake. This data consists of both textual information and meta-information about the jobs. This dataset can be used to create classification models which can learn the job descriptions which are fraudulent.
<hr>

## Dataset : 
**The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset :** <br>
https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction
<hr>

## Goal/Aim of the project: 
**This project is to identify the Real/Fake job postings.**
<hr>

## Libraries used: 
- ```Numpy```
- ```Pandas```
- ```Matplotlib```
- ```Seaborn```
- ```Sklearn```
<hr>

## Data Visualization :

Count Plot - 1 
<!--  -->

Count Plot - 2
<!--  -->

Confusion Matrix - 1
<!--  -->

Confusion Matrix - 2
<!--  -->

Confusion Matrix - 3
<!--  -->

Confusion Matrix - 4
<!--  -->

Decision Tree Model
<!-- -->
<hr>

## Model comparison :
<table>
    <tr>
        <th><u>Model Name</u></th>
        <th><u>Accuracy Score</u></th>
    </tr>
    <tr>
        <th>Logistic Regression</th>
        <th> 95.67567567567568 </th>
    </tr>
    <tr>
        <th>Logistic Regression CV</th>
        <th> 95.61936936936937 </th>
    </tr>
    <tr>
        <th>Support Vector Classifier</th>
        <th> 94.97747747747748 </th>
    </tr>
    <tr>
        <th>Decision Tree Classifier</th>
        <th> 96.26126126126127 </th>
    </tr>
</table>
<hr>

## Conclusion and Discussion :
- Buit 4 models with an average accuracy score of the models ranging the area of about ```95%```.

- Decision Tree Model has the highest accuracy score of 96.26%.

- Both the Logistic Regression Models have a similar accuracy of about 95%.

- SVC model doesn't perform as expected.

- If we consider only the Accuracy score it's good to go with **Decision Tree** else we can choose **Logistic Regression(CV)**.
<hr>

P.S.: Time taken to run the notebook in a 8GB RAM, i5 11th Gen Processor is ```180 seconds```.
<hr>
