# Mineral-Classification
Explore the classification of minerals using machine learning techniques, analyzing images to identify and categorize different mineral types. Gain insights into the diversity of minerals and their visual characteristics through image data analysis.
<img width="926" alt="webapp" src="https://github.com/tanuj437/Mineral-Classification/assets/128210429/de679733-b0e8-4383-8b22-93d918e842ee">


## 📝 Abstract
Mineral Classification involves using machine learning models to automatically classify images of minerals into specific categories. Techniques like convolutional neural networks (CNNs) are employed to extract features from mineral images, enabling accurate classification based on visual attributes.

## 🔍 Methodology
**Importing Libraries**
  -Libraries such as NumPy, Pandas, Sklearn, Transformers, and others are imported for data manipulation, visualization, and machine learning model building.

**Loading the Dataset**
  -The dataset consists of images of various minerals categorized into different classes based on their types.

**Data Preprocessing**
  -Data preprocessing involves tasks such as resizing images, normalizing pixel values, and augmenting data to enhance model performance and robustness.

**Training the Models**
  -Multiple models are trained, including CNNs, Random Forest, SVM, KNN, Logistic Regression, Decision Tree, and Extra Tree classifiers, to classify mineral images.
  
**Model Performance Analysis**
  -Performance metrics such as accuracy, precision, and recall are computed to evaluate and compare the effectiveness of each model.

**Model Prediction**
  -The trained models are used to predict the types of minerals in unseen images, showcasing their classification capabilities.
  
**Deploy**
  -Streamlit is utilized to deploy a web application for real-time mineral classification, enabling users to upload images and receive instant classification results.

**Data and Model File Download**
  -The dataset used for training and the pre-trained models are available for download and further exploration.. [Kaggle Dataset Link](https://www.kaggle.com/datasets/spadini/mineral-classification)

### Project Directory Structure
```
BRICS Sentiment Analysis
|- Dataset
  |- img
    |- apatite/
    |- calcite/
    |- corundum/
    |- diamond/
    |- fluorite/
    |- gypsum/
    |- orthoclase/
    |- quartz/
    |- talc/
    |- topaz/
  |- README.md

|- Model
  |- mineral_classification.ipynb
  |- README.md
  |- mineral_classification_model.pkl
|- Web App
  |- app.py
  |- README.md
|- Images
  |- CNN_conf.png
  |- README.md
  |- Decision_tree_conf.png
  |- SVM_conf.png
  |- classifying_minerals.mp4
  |- comparision.png
  |- extra_tree_classification_conf.png
  |- logistic_regression.png
  |- mineral_classificaiton.png
  |- mineral_classificaiton_2.png
  |- mineral_classificaiton_3.png
  |- prediction.png
  |- random_forest_conf.png
  |- webapp.png
|- requirements.txt
|-README.md
```

## How to Use
**Requirements**
  -Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the requirements.txt file.

**Download Data**
  -Download the img dataset from Kaggle mentioned in the dataset section of the project.

**Run the Jupyter Notebook**
  -Open the provided Jupyter Notebook file and run each cell sequentially. Make sure to update any file paths or configurations as needed for your environment.

**Training and Evaluation**
  -Train the models using the provided data and evaluate their performance using metrics such as accuracy and loss.

**Interpret Results**
  -Analyze the model's performance using the visualizations and metrics provided in the notebook.

Feel free to reach out if you encounter any issues or need further assistance with running the notebook.

## Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
