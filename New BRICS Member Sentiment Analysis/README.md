# BRICS Sentiment Analysis
Delve into the collective sentiment of the global community as we analyze public perspectives on the inclusion of six new member nations in the BRICS alliance. This sentiment analysis provides valuable insights into how individuals perceive and respond to the evolving dynamics within this influential coalition, offering a nuanced understanding of public sentiment towards the new additions. Uncover the diverse range of opinions, emotions, and reactions as we navigate the intricacies of international relations and the impact on public discourse.

Note: The labeling is done based on likes on the comments.
<img width="926" alt="Screenshot 2024-06-10 170311" src="https://github.com/tanuj437/New-BRICS-members-Sentiment-Analysis-518/assets/128210429/53f68679-6d6e-4180-bab0-6fc61051a9c7">

## 📝 Abstract
BRICS Sentiment Analysis involves automatically identifying and classifying public comments into categories based on their sentiment. Techniques like analyzing comment content, using machine learning models, and leveraging BERT embeddings help achieve this. The goal is to understand public sentiment towards the inclusion of new member nations in the BRICS alliance.

## 🔍 Methodology
**Importing Libraries**
  -Libraries such as NumPy, Pandas, Sklearn, Transformers, and others are imported for data manipulation, visualization, and machine learning model building.

**Loading the Dataset**
  -The dataset contains multiple rows of comments labeled with their sentiment based on the number of likes.

**Data Preprocessing**
  -Prepare data for analysis: handle missing values, encode categorical data, scale features, perform feature engineering, split into train-test sets, and normalize data. Ensure data is in a suitable format for machine learning algorithms.

**Training the Models**
  -Each model is compiled using techniques like LightGBM and Support Vector Machines.
The models are trained on the training dataset and evaluation is done.
**Model Performance Analysis**
  -Training and validation loss and accuracy are plotted to visualize the models' performance.

**Model Prediction**
  -The model is given a test dataset to check the accuracy and precision of the predictions.

**Deploy**
  -Using the Streamlit library, the model is deployed for real-time sentiment analysis.

**Data and Model File Download**
  -The dataset used in the project is taken from the Kaggle BRICS Sentiment Analysis Dataset. [Kaggle Dataset Link]

### Project Directory Structure
```
BRICS Sentiment Analysis
|- Dataset
  |- BRICS.csv
  |- README.md

|- Model
  |- BRICS_Sentiment_Analysis.ipynb
  |- README.md
  |- lgb_model.pkl
|- Web App
  |- app.py
  |- README.md
|- Images
  |- LightGBM_output.png
  |- README.md
  |- advance_stacking_output.png
  |- cmp_all_model.png
  |- distribution.png
  |- likecount.png
  |- lstm_output.png
  |- mlp_output.png
  |- simple_neural_network_output.png
  |- Stacking_classifier_confusion.png
  |- webapp_run.mp4
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
Tanuj Saxena [LinkedIn(https://www.linkedin.com/in/tanuj-saxena-970271252/)]
