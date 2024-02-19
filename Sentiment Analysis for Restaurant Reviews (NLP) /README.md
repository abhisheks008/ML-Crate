<h1>Sentiment Analysis for Restaurant Reviews (NLP)</h1>

**GOAL**

To build a machine learning model for predicting the Sentiments of Customer based on their review on a Restaurant.

**DATASET**

[https://www.kaggle.com/datasets/d4rklucif3r/restaurant-reviews]

**DESCRIPTION**

This Dataset contains two COLUMNS Customer Reviews and Liked. It has 1000 rows/entries.
Customer reviews tells us about the reviews given by the customers for a food in restaurant and liked column tells about whether they liked the food or not.

### Visualization and EDA of different attributes:

<img alt="length_of_review" src="./Images/Number_of_characters_in_each_review.png">

<img alt="barchart" src="./Images/barchart.png">

<img alt="piechart" src="./Images/piechart.png">

**Positive Review WordCloud**

<img alt="wordcloud" src="./Images/wordcloud_positive.png">

**Negative Review WordCloud**

<img alt="wordcloud" src="./Images/negative_wordcloud.png">

**NLP TECHNIQUES USED**

1. **Text Cleaning:**

    - **Punctuation Removal:** I have removed punctuation from the text using a list comprehension to keep only non-punctuation characters.
    - **Stopword Removal:** I have removed common English stopwords using the NLTK library. Stopwords are words that are frequently used but often carry little meaning (e.g., "the," "and," "is").
    - **Stopword Customization:** I have a set of custom stopwords ({'not', 'nor', 'no', "don't", "was'nt", "aren't", "didn't"}) that I want to exclude from removal. This is important to preserve negation words like "not" which can change the sentiment of a sentence.

2. **Vectorization:**

    - Using CountVectorizer I have represented each review as a bag of its words, ignoring grammar and word order but keeping track of word frequency i.e, Tokenization. And then I have converted this tokenized review into array of Numerical vector which is nothing but Vectorization.
    - TF-IDF Vectorization (vectorizer.transform): You use the vectorizer.transform method, which suggests the use of TF-IDF vectorization. TF-IDF represents the importance of a term in a document relative to its importance in a collection of documents. It converts the text into a numerical vector.

3. **WORDCLOUD:**

     - Generating a word cloud is a data visualization technique commonly used in NLP to represent the most frequent words in a text corpus. I have generated word cloud for both positive reviews and negative reviews separately as shown in image above.


**MODELS USED**

| Model                     | accuracy_train(%) | precision_train(%) | accuracy_test(%)  | precision_test(%)   |
|---------------------------|-------------------|--------------------|-------------------|---------------------|
|SVM		                    |97.57          	  |94.25	             |92.86	             |85.5                 |
|Logistic Regression	      |93.51	            |90.38	             |88.66	             |87.0                 |
|Random Forest	            |91.84	            |80.88	             |87.18	             |78.5                 |
|Decision Tree	            |99.22	            |97.50	             |79.09	             |81.5                 |
|Guassian Naive Bayes	      |69.61	            |77.88	             |68.61	             |75.0                 |


**WHAT I HAD DONE**

* Load the dataset which is CSV format.
* It has 1000 entries(Rows), 2 columns.
* Checked for missing values and cleaned the data accordingly.
* Analyzed the data, found insights and visualized them accordingly.
* Tokenized and Vectorized the Review Column, and then used this array of vectorized review to train my model.
* Train the datasets by different models and saves their accuracies into a dataframe.


**LIBRARIES NEEDED**

1. Pandas
2. Matplotlib
3. Sklearn
4. NumPy
5. nltk
6. Seaborn
7. wordcloud

**CONCLUSION**

- ML Model predicts sentiments are positive or negative too correctly even if negation words such as not, no, nay are present in our review. Generally negation words opposes positive condition, so considering them is important in order to train our model correctly. Hence I didn't remove negation stopwords.
- We got highest testing accuracy using SVM algorithm which is around 93%
- We got good accuracy for other algorithms also


**YOUR NAME**

*Ghousiya Begum*

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ghousiya-begum-a9b634258/)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ghousiya47)
