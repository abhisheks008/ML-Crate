# Project Title : Real / Fake Job Posting Prediction
<!-- cover image -->
![cover](https://user-images.githubusercontent.com/81156510/152502185-8620325f-3ff9-47eb-9737-c033bd964619.png)

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

Count Plot - Only Fraudulent (Predictor Column) 
![count-1](https://user-images.githubusercontent.com/81156510/152502206-62a746a3-801f-4a36-9bb8-670cf111ce76.png)

Count Plot - Location Count (with Fraudulent Column as hue)
![count-2](https://user-images.githubusercontent.com/81156510/152502243-f29984f1-1298-4199-af41-1c60d8c74a05.png)

Confusion Matrix - Logistic Regression
![confusion-1](https://user-images.githubusercontent.com/81156510/152502258-5e7e5ff7-c6bf-479c-adeb-94ad61ebea05.png)

Confusion Matrix - Logistic Regression CV
![confusion-2](https://user-images.githubusercontent.com/81156510/152502284-702b5386-83e9-4073-94a8-1334c119f773.png)

Confusion Matrix - Support Vector Classifier
![confusion-3](https://user-images.githubusercontent.com/81156510/152502311-ea994888-a72b-4335-8d52-b37e22a64cc6.png)

Confusion Matrix - Decision Tree Classifier
![confusion-4](https://user-images.githubusercontent.com/81156510/152502339-4bcdfa81-d462-4be9-becf-1446d3ecc183.png)

Decision Tree Model
![tree](https://user-images.githubusercontent.com/81156510/152502357-768315e7-8675-439a-93e0-7d0f74ac5f01.png)

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
