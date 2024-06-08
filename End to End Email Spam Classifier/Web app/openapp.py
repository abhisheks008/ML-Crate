import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import os

# Download required NLTK data only once
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Initialize the PorterStemmer
ps = PorterStemmer()

# Function to preprocess and transform the text
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
def transform_text(text):
    cleaned_text = text.lower()
    
    tokens = nltk.word_tokenize(cleaned_text)
    
    tokens = [token for token in tokens if token.isalnum()]

    stop_words = set(stopwords.words('english'))
    
    tokens = [token for token in tokens if token not in stop_words]
    
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(token) for token in tokens]
    
    cleaned_text = " ".join(stemmed_tokens)
    return cleaned_text

def predict_spam(vector_input, model, tfidf):
    dense_input = vector_input.toarray()  # Convert sparse matrix to dense array
    prediction = model.predict(dense_input)[0]
    return "Spam" if prediction == 1 else "Not Spam"

# Verify the presence of files before loading
vectorizer_path = '../Model/vectorizer.pkl'
model_path = '../Model/model.pkl'

if not os.path.exists(vectorizer_path):
    st.error(f"Error: {vectorizer_path} file not found.")
    st.stop()

if not os.path.exists(model_path):
    st.error(f"Error: {model_path} file not found.")
    st.stop()

# Load the vectorizer and model with error handling
try:
    with open(vectorizer_path, 'rb') as file:
        tfidf = pickle.load(file)
except Exception as e:
    st.error(f"Error loading {vectorizer_path}: {e}")
    st.stop()

try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading {model_path}: {e}")
    st.stop()

# Streamlit UI
st.title("Email Spam Classifier")
input_sms = st.text_input("Enter the message")

if st.button("Predict"):
    if input_sms:
        try:
            transformed_sms = transform_text(input_sms)
            vector_input = tfidf.transform([transformed_sms])
            result = predict_spam(vector_input, model, tfidf)  # Pass entire vector_input
            
            if result == 0:
                st.header("Not Spam")
            else:
                st.header("Spam")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
    else:
        st.error("Please enter a message to classify.")
