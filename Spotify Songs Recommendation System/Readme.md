Spotify Songs Recommendation System

GOAL

To Classify the song whether it has been liked by the user or not based on the song features.

DATASET

https://www.kaggle.com/datasets/corneliusjustin/spotify-songs-recommendationbinary-classification
https://www.kaggle.com/datasets/geomack/spotifyclassification

DESCRIPTION

The main of this project is to impement a model to classify the song into 1(liked) or 0(disliked).

WORK DONE

Analyzed the data and found insights such as correlation, missing values and also extracted features from the dataset useful for classification.

![confusion_matrix](https://user-images.githubusercontent.com/62555290/196527230-348bb88f-b0b8-4797-a61d-f375f16cebf6.jpeg)

Approach Taken(Algorithm)

We have used three different Classification Models like Logistic Regression, Naive Bayes Classifier, Support Vector Machine. Chi square test was used to select the features from the relevant columns of the dataset which were useful for classification. All the three models were trained from the training set and then evluated using testing set. All the three models gave an accuracy of 62.5% on test set  due to lesser number of data.
 
LIBRARIES NEEDED:-
Numpy Pandas Matplotlib  sklearn.feature_selection train_test_split seaborn StandardScaler chart_studio cufflinks PLOTS

CONCLUSION

We investigated the data, checking for data unbalancing, visualizing the features, and understanding the relationship between different features. We made a model to classify the song whether it has been liked by the user or not. Spotify Songs Recommendation System helps in better understanding what the customer wants to listen and what is their taste of music which can lead to construction of  marketing stategy. All the three models had same accuracy of 62.5%, it might be due to fewer number of data points or skewed dataset.



