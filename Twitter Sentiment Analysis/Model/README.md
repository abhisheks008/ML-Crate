# TWITTER SENTIMENTAL ANALYSIS

## Goal

The goal of this project is to predict whether a comment is positive ,negative or neutral on twitter

## Dataset

I have Downloaded this dataset from kaggle website. Here is the link:
[Dataset Link](https://www.kaggle.com/datasets/kazanova/sentiment140)

##Approack involved
-So basiaclly after performing eda and feature engineering i have used Vader and Roberta model for twitter sentimental analysis and compare the performance of the dataset on both the models . Roberta accuracy is all over increased as it goes with the context of the data also which is very important part of human speech ..At last i have used the transformer pipeline for increasing the speed

## Models involved

-Vader
\_RoBERTa(from hugging face)
-Transformer Pipeline

## Steps involoved

- Imported all the required libraries and dataset for this project.
- Exploratory Data Analysis and Visualizing different aspects of the dataset.
  -Applying Feature Engineering
  -Applying Vader model to the preprocessed tweets to get sentiment scoress
- VADER provides positive, negative, and neutral sentiment scores, as well as an overall compound score.

-RoBERTa-(from Hugging face)
-Fine-tune a pre-trained RoBERTa model on a sentiment analysis task using a labeled dataset
-Use the fine-tuned RoBERTa model to predict the sentiment of each tweet.

-Compare the sentiment analysis results obtained from VADER and RoBERTa.
Analyze cases where VADER and RoBERTa disagree to understand the strengths and weaknesses of each method.

-Application of the transformer pipeline for the increase of the speed .

## Library used:

1. numpy.
2. pandas.
3. matplotlib.
4. seaborn.
   5.nltk
   6.Transformers library
   7.scikit-learn

## Visualization and EDA of different attributes:

![download]("C:\Users\jagri\Downloads\img03.png")

# So basically the context of the language is an important part of human speech .. Some tweets or comments can be sarcastic which is identified as negative but may not be ..So RoBerta satisfies that and predict the tweets to meet good accuracy o the tweets ...

## Conclusion:

-The sarcastic comments can be negtaive positive or neutral.. depending on the human context ..
-Hence applying transformer library and pipeline helps in analysis of the tweets in a more accurate manner..

## Authors

- Created by [JagritiGautam793](https://github.com/JagritiGautam793) JWOC2024

[Dataset Link](https://www.kaggle.com/datasets/kazanova/sentiment140)
