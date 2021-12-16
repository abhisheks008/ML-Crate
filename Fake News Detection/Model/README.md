**PROJECT TITLE**

**GOAL**

To predict whether news provided is real or fake

**DATASET**

The Fake News Dataset is from [Kaggle](https://www.kaggle.com/c/fake-news/data)

**DESCRIPTION**

The project mainly focuses on handling huge amounts of text data, extracting meaningful information from it using methods like lemmatization, stemming, tokenization and soo much more and then passing all these informations as features to a model and making a prediction whether the news is reliable(0) or unreliable(1)

**WHAT I HAD DONE**

 - The very first step is doing an exploratory data analysis, in which I explored the relationship between labels and features
 - Compared the data before and after preprocessing, significantly reduced less informative data like punctuations and stopwords
 - For preprocessing I have used methods like
    >- Lower casing
    >- Removed stopwords,puntuations
    >- Performed Stemming(Finding root words like for functioning root word will be function) using nltk's PorterStemmer
    >- Created sparse matrix using CountVectorizer for vocab size of 6000 features using bag of words and n-grams to extract more details
- Train/Test Validation splits
- Finally trained models, tuned them to make final predictions

**MODELS USED**

I have used these models as they perform good classification of text data
* Logistic Regression
* Passive Aggressive Classifier 
* KNeighbors Classifier
* Random Forest Classifier
- Out of these models I choose Passive Aggresive Classifer as it performed good and handle larges streams of text data very well

**LIBRARIES NEEDED**

* scikit-learn
* nltk
* wordcloud
* matplotlib
* seaborn
* pandas
* numpy

**ACCURACIES**

![Performances](../Images/performance.png )


**CONCLUSION**

Even though the Logistic Regression very well but it took a lot of time to train it, in terms of performance the Passive Aggressive Classifier model is the best and there are soo many to extract insights from text data if we use natural langauage processing methods like word embeddings, bag of words, n-grams, stemmization and many more. 

**Rahul Kumar**

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahul-netizen/) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahul-netizen/)
