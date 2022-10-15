# HEART FAILURE PREDICTION


## GOAL

Implementing classification models that can be used to predict the likelihood of a heart failure.


## DATASET

https://www.kaggle.com/datasets/asgharalikhan/mortality-rate-heart-patient-pakistan-hospital

he data contains complete history of heart patients (so data scientists from different parts of the world can work with it). The dataset is collected from Pakistan, Faisalabad hospital named institute of cardiology.


## DESCRIPTION

A machine learning model to classify if the patient is at risk of heart failure or not based on the given data of a patient.


## WORK DONE

A)	Data Analysis:  
    a.	Importing the dataset  
    b.	Getting information about dataset (mean, max, min, quartiles etc.)  
    c.	Finding the correlation between all fields.  

B)	Data Visualization:  
    a.	Visualizing the number of patients having a heart disease and not having a heart disease.  
    b.	Visualizing the age and weather patient has disease or not  
    c.	Visualizing correlation between all features using a heat map  
    
C)	Logistic Regression:  
    a.	Built a simple logistic regression model   
        i.	Divided the dataset in 70:30 ratio  
        ii.	Built the model on train set and predict the values on test set  
        iii. Built the confusion matrix and get the accu	racy score   

D)	Decision Tree:  
    a.	Built a decision tree model  
        i.	Divided the dataset in 70:30 ratio  
        ii.	Built the model on train set and predict the values on test set  
        iii.Built the confusion matrix and calculate the accuracy  
        iv.	Visualizing the decision tree using the graphviz package  


E)	Random Forest:  
    a.	Built a Random Forest model  
        i.	Divided the dataset in 70:30 ratio  
        ii.	Built the model on train set and predict the values on test set  
        iii.Built the confusion matrix and calculate the accuracy  
        iv.	Visualizing the model using the graphviz package  

F)	Selecting the best model:  
    a.	Printed the confusion matrix of all classifiers  
    b.	Printed the classification report of all classifiers  
    c.	Calculated Recall Precision and F1 score of all the models  
    d.	Visualized confusion matrix using heatmaps and Recall Precision and F1 score of all the models using bar graphs  
    e.	Selected the best model based on the best accuracies  


## CONCLUSION

Logistic Regression Classifier had the highest accuracy out of all the others, followed by Decision Tree and Random Forest. Through this project, we learned how to apply various classification algorithms and analyse their performance by using confusion matrix and classification report. Heart failure is one of the leadinng causes of death in the world. This dataset and model can be used and further improved by healthcare industry to prevent the risks of having a heart failure.

