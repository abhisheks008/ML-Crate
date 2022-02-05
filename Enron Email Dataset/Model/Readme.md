# Enron email dataset

## GOAL

The main goal of the project is to identify the spam detection and also classification. 

## DATASET

Link of the dataset : https://www.kaggle.com/wcukierski/enron-email-dataset

## DESCRIPTION
This dataset was collected and prepared by the CALO Project (A Cognitive Assistant that Learns and Organizes). It contains data from about 150 users, mostly senior management of Enron, organized into folders. 

The corpus contains a total of about 0.5M messages. This data was originally made public, and posted to the web, by the Federal Energy Regulatory Commission during its investigation. The email dataset was later purchased by Leslie Kaelbling at MIT, and turned out to have a number of integrity problems. 

A number of folks at SRI, notably Melinda Gervasio, worked hard to correct these problems, and it is thanks to them (not me) that the dataset is available. The dataset here does not include attachments, and some messages have been deleted "as part of a redaction effort due to requests from affected employees.

## WHAT I HAD DONE

**In this dataset the procedure followed is:**
1. Having a glance at the dataset.
2. Reducing the size of the dataset.
3. Analysing the sender.
4. Counting the frequency.
5. Create df with 2 highest emails. 
6. Preprocessing and get ready for machine learning
7. Remove rare words
8. Define X and y
9. Split for training and validating
10. Vectorise
11. Define and train model
12. Predict on validation set
13. Evaluate

## MODELS USED

List out all the algorithms or models used in this project Why have you choosed that algorithms should also be stated

## LIBRARIES NEEDED

- sklearn
- seaborn
- Numpy==1.19.2
- pandas==1.2.4
- matplotlib==3.4.2

## VISUALIZATION

![image](https://user-images.githubusercontent.com/63282184/152628107-21a0dd5f-977c-46d6-86b3-8c9ec3eac1b1.png)

![image](https://user-images.githubusercontent.com/63282184/152628118-6e5b9a7f-3464-4256-a50b-21a28a0a5bc6.png)

## ACCURACIES

I have used the Naive Bayes algorithm. 
- Training set accuracy is 99.79591836734694%
- Test set accuracy is 96.36363636363636%

## CONCLUSION

I have tried to build a model which helps to classify the mails whether they are spam, so that the users can be risk free. 

## Munagala Ashish Reddy
