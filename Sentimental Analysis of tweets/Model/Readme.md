# *Sentimental Analysis of tweets*
_________________________________________
## **GOAL**

>The aim of the project is to build a model which would predict the opinion of the people in tweets under particular # 
>In this case we have used the omicron variant of COVID to see the world's opnion about it
_________________________________________
## **DATASET**

>The dataset was created by fetching the tweets from twitter using [tweepy](https://docs.tweepy.org/en/stable/) and converted to dataframe using [Pandas library](https://pandas.pydata.org/docs/)

________________________________________
## **DESCRIPTION**

>In this project, we compare the sentiments of the tweets either positive,negative, or neutral opinion from [vader_lexicon](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
>and tried to calculate the score of each sentiments  
_________________________________________
## **WHAT I HAD DONE**
_________________________________________
## Steps followed:
 > * Created a twitter developer account and fetched my consumer_key, consumer_secret, access_token, access_token_secret 
 > * Connecting to Twitter with API
 > * Gathering the tweets regarding OMICRON
 > * Setting up the dataset
 >  * Then performed Data cleaning :Removing the stopword and handling unnecessary wordse
 >  * Then performed Visualising of the tweets using [wordcloud](https://pypi.org/project/wordcloud/)
 >  * Then used vader_lexicon (Valence Aware Dictionary and sEntiment Reasoner) to analyse positive,negative and neutral tweets
 >  * Then Calculated the Sentiment Score

_________________________________________
## **MODELS USED**
> To be specific we have used a tookit [Natural Language Toolkit](https://www.nltk.org/#natural-language-toolkit) from python to which provides easy-to-use interfaces to over 50 corpora and lexical resources such 
> as [vader_lexicon](https://www.nltk.org/_modules/nltk/sentiment/vader.html), [SentimentIntensityAnalyzer](https://www.nltk.org/api/nltk.sentiment.html), [SnowballStemmer](https://www.nltk.org/_modules/nltk/stem/snowball.html) ,
> stopwords removal to analyse the tweets and  calculate the Sentiment Score

_________________________________________
##**LIBRARIES NEEDED**

>* Pandas
>* Matplotlib
>* nltk
>* Numpy
>* tweepy
>* wordcloud



_________________________________________
## **CONCLUSION**

>From this project we conclude that using [Natural Language Toolkit](https://www.nltk.org/#natural-language-toolkit) we can analyse the sentiments of tweets

_________________________________________
## **Contribution by**
[Venkatakrishnan R](https://github.com/Cody-coder017)

