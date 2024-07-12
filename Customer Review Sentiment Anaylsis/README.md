
# Customer Review Sentiment Analysis
Customer Review Sentiment Analysis is a project focused on automatically analyzing and classifying customer reviews based on their sentiment. The project leverages machine learning techniques to understand and categorize customer sentiments expressed in reviews.

Note: The labeling is done based on Star.
<img width="922" alt="webapp" src="https://github.com/tanuj437/Customer-Review-Sentiment-Anaylsis/assets/128210429/5528ae7e-6ded-46d3-a845-026451cf40e6">

## 📝 Abstract
Customer Review Sentiment Analysis involves automatically identifying and classifying sentiment from customer reviews. Techniques such as natural language processing (NLP), machine learning models, and sentiment analysis algorithms are employed to achieve this.

## 🔍 Methodology
**Importing Libraries**
  -Libraries such as NumPy, Pandas, Sklearn, Transformers, and others are imported for data manipulation, visualization, and machine learning model building.

**Loading the Dataset**
  -The dataset contains multiple rows of comments labeled with their sentiment based on the Star rating.

**Data Preprocessing**
  -Prepare data for analysis: handle missing values, encode categorical data, scale features, perform feature engineering, split into train-test sets, and normalize data. Ensure data is in a suitable format for machine learning algorithms.

**Training the Models**
  -Each model is compiled using techniques like LightGBM and Logistic Regression.
The models are trained on the training dataset and evaluation is done.

**Model Performance Analysis**
  -Training and validation loss and accuracy are plotted to visualize the models' performance.
  
<img width="404" alt="precision_cmp" src="https://github.com/tanuj437/Customer-Review-Sentiment-Anaylsis/assets/128210429/f34e3bfc-c14c-4c9e-8a58-e9de9f27c2d9">


**Model Prediction**
  -The model is given a test dataset to check the accuracy and precision of the predictions.
  
<img width="416" alt="recall_cmp" src="https://github.com/tanuj437/Customer-Review-Sentiment-Anaylsis/assets/128210429/748c1245-c55c-4b4b-850a-e687c6c9ffe7">


**Deploy**
  -Using the Streamlit library, the model is deployed for real-time sentiment analysis.

**Data and Model File Download**
  -The dataset used in the project is taken from the Kaggle Customer Review Dataset. [Kaggle Dataset Link](https://www.kaggle.com/datasets/cynthiarempel/amazon-us-customer-reviews-dataset?select=amazon_reviews_us_Musical_Instruments_v1_00.tsv)

### Project Directory Structure
```
BRICS Sentiment Analysis
|- Dataset
  |- column_overview.png
  |- dataset_view.png
  |- README.md

|- Model
  |- customer-review-aentiment-analysis.ipynb
  |- README.md
  |- model.pkl
  |-tfidf_vectorizer.pkl
|- Web App
  |- app.py
  |- README.md
|- Images
  |- f1_cmp.png
  |- README.md
  |- precision_cmp.png
  |- recall_cmp.png
  |- review_length.png
  |- sentiment_distribution.png
  |- star_rating.png
  |- star_ratingtocount.png
  |- webapp.png
  |- running_test.mp4
  |-wordcloud.png
|- requirements.txt
|-README.md
```

## How to Use
**Requirements**
  -Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the requirements.txt file.

**Download Data**
  -Download the brics_comments.csv dataset from Kaggle mentioned in the dataset section of the project.

**Run the Jupyter Notebook**
  -Open the provided Jupyter Notebook file and run each cell sequentially. Make sure to update any file paths or configurations as needed for your environment.

**Training and Evaluation**
  -Train the models using the provided data and evaluate their performance using metrics such as accuracy and loss.

**Interpret Results**
  -Analyze the model's performance using the visualizations and metrics provided in the notebook.

Feel free to reach out if you encounter any issues or need further assistance with running the notebook.

## Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
