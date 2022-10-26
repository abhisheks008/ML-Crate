#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[2]:


my_train_df = pd.read_csv("/kaggle/input/learn-ai-bbc/BBC News Train.csv")
my_test_df = pd.read_csv("/kaggle/input/learn-ai-bbc/BBC News Test.csv")


# In[3]:


#Categorize sport articas 1 and non-sport as
my_train_df['Category_id'] = np.where(my_train_df['Category'] == 'sport', 1, 0)
len(my_train_df)


# In[4]:


my_train_df.drop_duplicates(subset=['Category', 'Text'], inplace=True)
len(my_train_df)


# In[5]:


#separating sport and non sport distribution to do correct class distribution
sport_articles_df = my_train_df[my_train_df['Category_id'] == 1]
non_sport_articles_df = my_train_df[my_train_df['Category_id'] != 1]


# In[6]:


len(sport_articles_df),len(non_sport_articles_df)


# In[7]:


# Addressing Class imbalance.
# Performing Oversampling

#non_sport_articles_df = non_sport_articles_df.sample(n=len(sport_articles_df) , ignore_index=True)
sport_articles_df = sport_articles_df.sample(n=len(non_sport_articles_df),replace=True,ignore_index=True)


# In[8]:


len(sport_articles_df),len(non_sport_articles_df)


# In[9]:


#now we need to merge the two dataframe.

total_df = pd.concat([sport_articles_df,non_sport_articles_df], axis=0)
len(total_df)


# In[10]:


#now we need to suffle the df
total_df = total_df.sample(frac=1, ignore_index=True)


# # Processing: Punctuation removal, stop words removal ..

# In[11]:


#lowercase
total_df['Text'] = total_df.Text.apply(lambda x: x.lower())


# In[12]:


#remove punctuations
import string
table = str.maketrans("", "", string.punctuation)
def remove_punc(text):
    return text.translate(table)


# In[13]:


total_df['Text'] = total_df.Text.apply(lambda x: remove_punc(x))
total_df.head(100)


# In[14]:


#Remove stopwords

from nltk.corpus import stopwords

stop = set(stopwords.words("english"))

def rem_stop(text):
    word_list = [word for word in text.split() if word not in stop]
    return " ".join(word_list)


# In[15]:


total_df['Text'] = total_df.Text.apply(lambda x: rem_stop(x))
total_df.head(30)


# In[16]:


# Lemmatization process
# import nltk
# dler = nltk.downloader.Downloader()
# dler.download('wordnet')
# import re
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def tokenize_and_lemmatize(text):
    # tokenization to ensure that punctuation is caught as its own token
#     tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
#     filtered_tokens = []
    
#     for token in tokens:
#         if re.search('[a-zA-Z]', token):
#             filtered_tokens.append(token)
    lem = [lemmatizer.lemmatize(stemmer.stem(t)) for t in text.split()]
    return " ".join(lem)


# In[17]:


total_df['Text'] = total_df.Text.apply(lambda x: tokenize_and_lemmatize(x))
total_df.head(30)


# # Glove Embedding

# In[18]:


#Create corpus for glove

from nltk.tokenize import word_tokenize

def create_corpus(df):
    corpus = []
    for text in df['Text']:
        words = [word for word in word_tokenize(text)]
        corpus.append(words)
    return corpus


# In[19]:


corpus = create_corpus(total_df)


# In[20]:


corpus_len = len(corpus)
print(corpus_len)


# In[21]:


#getting max length for padding
max_length = max([len(text.split()) for text in total_df['Text']])


# In[22]:


#train, val split
from sklearn.model_selection import train_test_split

x_train, x_val, y_train, y_val = train_test_split(
    total_df['Text'], total_df['Category_id'], test_size=0.20, random_state=1)


# In[23]:


x_train.shape, x_val.shape, y_train.shape, y_val.shape


# In[24]:


#install tensorflow
get_ipython().system('pip install tensorflow')


# In[25]:


# #Tokenizer
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[26]:


# #tokenize texts
tokenizer = Tokenizer(num_words=corpus_len)


# In[27]:


# # text word sequences for train
tokenizer.fit_on_texts(x_train)
train_sequence = tokenizer.texts_to_sequences(x_train)


# In[28]:


# # text word sequences for val
tokenizer.fit_on_texts(x_val)
val_sequence = tokenizer.texts_to_sequences(x_val)


# In[29]:


# #Padding Train and Val. Using max_length in total corpus of train and val
train_padded = pad_sequences(train_sequence, maxlen=max_length, truncating="post", padding="post")
val_padded = pad_sequences(val_sequence, maxlen=max_length, truncating="post", padding="post")


# In[30]:


#get the word index in dictionary 
word_index = tokenizer.word_index


# In[31]:


#len(word_index)


# # Glove pretrained embedding : Downloaded from (https://nlp.stanford.edu/data/glove.6B.zip)

# In[32]:


# Glove embedding
embedding={}
with open("/kaggle/input/glove-embeddings/glove.6B.300d.txt","r") as f:
    for line in f:
        values = line.split()
        word = values[0]
        vectors = np.asarray(values[1:],'float32')
        embedding[word] = vectors
f.close()


# In[33]:


# #Embedding contains in matrix
# num_words = len(word_index) +1
# embedding_matrix = np.zeros((num_words, 300)) #each word will be a 1:100 dim vector

# for word, i in word_index.items():
#     if i < num_words:
#         embd_vec = embedding.get(word)
#         if embd_vec is not None:
#             embedding_matrix[i] = embd_vec


# In[34]:


# sentance vectorization

def sent_vectorize(sentance):
    sent_vec = []
    count = 0
    for w in sentance:
        try:
            if count == 0:
                sent_vec = embedding.get(w) #get the embedding of the word using the position index
            else:
                sent_vec = np.add(sent_vec, embedding.get(w)) #adding all the word embeddings into one embedding for a sentance
            count += 1
        except:
            pass
    
    return np.asarray(sent_vec) / count #average out the sentace embedding


# In[35]:


train_data = []
for sentance in x_train:
    train_data.append(sent_vectorize(sentance))


# In[36]:


val_data = []
for sentance in x_val:
    val_data.append(sent_vectorize(sentance))


# # Model Creation

# In[37]:


#import
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import plot_model


# In[38]:


model = Sequential()
model.add(Dense(100, input_dim = 300, activation="relu"))
model.add(Dense(50, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(50, activation="relu"))
model.add(Dropout(0.2))
# model.add(Dense(50, activation="relu"))
# model.add(Dropout(0.2))
model.add(Dense(1, activation="sigmoid"))


# In[39]:


plot_model(model, show_shapes=True, show_layer_names=True)


# In[40]:


#optimizer
model.compile(loss="binary_crossentropy", optimizer="Adam", metrics=['accuracy'])


# In[41]:


#training
train_data = tf.stack(train_data)
y_train = tf.stack(y_train)
tf.compat.v1.reset_default_graph()
model.fit(train_data, y_train, epochs=100, batch_size=10, verbose=0)


# In[42]:


#evaluation
val_data = tf.stack(val_data)
y_val = tf.stack(y_val)
loss, accuracy = model.evaluate(val_data,y_val, verbose=0)
print("Model loss: %2f, Accuracy: %2f" %((loss*100),(accuracy*100)))

