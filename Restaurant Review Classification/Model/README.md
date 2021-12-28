**PROJECT TITLE**

**GOAL**

To classify restaurant reviews as real or fake

**DATASET**

The dataset is the Yelp dataset taken from [Kaggle](https://www.kaggle.com/yelp-dataset/yelp-dataset)

**DESCRIPTION**

The project focusses on the restaurant reviews in the Yelp dataset, performing sentiment analysis on the reviews and classifying the reviews as real or fake by feeding the features to different classifier models and then comparing the accuracy of the models.

**WHAT I HAD DONE**

- First I loaded the data and performed checks missing data.
- Then I performed sentiment analysis on the reviews by using the following methods
    - Remove stopwords, punctuations
    - Tokenise the reviews to sentences and then words
    - Perform Lemmatisation
    - Sentiment score is computed and polarity score is assigned (1 = positive, 0 = negative)
    - Average all columns and also find the net positive sentiment score
- I then performed Exploratory Data Analysis to find the relationship between the various features and labels.
- Then I split the final dataset into train and test data and trained the models.
- Finally the trained models were used for classification and their performance was compared.

**MODELS USED**

- Support Vector Machine (SVM)
- Logistic Regression
- Decision Tree Classifier
- Gaussian NB model

**LIBRARIES NEEDED**

- numpy
- pandas
- matplotlib
- seaborn
- json
- scikit-learn
- nltk
- re

**ACCURACIES**

- Support Vector Machine (SVM) - 83%
- Logistic Regression - 83%
- Decision Tree Classifier - 92%
- Gaussian NB model - 92%

**CONCLUSION**

The decision tree and Naive Bayes models performed very well. However this was a sample of the full dataset (2500000 rows) because it took a long time to load the data. The results may vary with the full dataset. Natural Language Processing was really helpful in getting insights from the reviews. Also other parameters like checkins, tips, etc can influence the output.

**CONTRIBUTED BY**

Ahan Anupam

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahan-anupam-ab21411a4/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahananupam33)
