import streamlit as st
import pickle
import re
from nltk.corpus import stopwords

# Load NLTK stopwords
stop_words = set(stopwords.words('english'))

# Define text preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<[^>]+>', ' ', text)  # Remove HTML tags
    text = re.sub(r'[^a-z\s]', '', text)  # Remove non-alphabetic characters
    text = ' '.join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Load the pretrained model
model_filename = 'Model/model.pkl'
with open(model_filename, 'rb') as file:
    logistic_model = pickle.load(file)

# Load the pretrained TF-IDF vectorizer
vectorizer_filename = 'Model/tfidf_vectorizer.pkl'
with open(vectorizer_filename, 'rb') as file:
    vectorizer = pickle.load(file)

# Define a function to make predictions
def predict_sentiment(text):
    preprocessed_text = preprocess_text(text)
    transformed_text = vectorizer.transform([preprocessed_text])
    prediction = logistic_model.predict(transformed_text)
    return prediction[0]

# Streamlit app
st.title('Sentiment Analysis Web App')

st.write('This is a web app to classify the sentiment of customer reviews as positive, neutral, or negative.')

# User input
user_input = st.text_area('Enter a customer review:', '')

if st.button('Predict'):
    if user_input:
        prediction = predict_sentiment(user_input)
        st.write(f'The sentiment of the review is: **{prediction}**')
    else:
        st.write('Please enter a review to get a prediction.')

# To run the app, save this script and use the command: streamlit run your_script_name.py
