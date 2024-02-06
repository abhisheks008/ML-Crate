
# Eye Disease Prediction

**GOAL**

The purpose of the project is to predict the type of Eye Disease

**DATASET**

https://www.kaggle.com/bongsang/eye-disease-deep-learning-dataset

**DESCRIPTION**

In this project we have used a pretrained deep learning model to classify
the type of Eye Disease

**WHAT I HAD DONE**

* We have download the dataset from kaggle 
* From the downloaded dataset there are two folders - image and a label.csv file
* We have imported the libraries and files 
* Then we checked the information from the csv file
* We visualized the categories from the dataset
* We merged the labels from the csv file with the images
* We splitted the dataset, with a test_size of 30%
* We did some data augmentation
* Using Transfer Learning technique we implemented InceptionResNetV2 model for training
* We tuned the model to get better accuracy
* We train the dataset on the above model
* Generate Prediction,Classification Report and Confusion Matrix
* Save the model

**MODELS USED**

We have implemented a pretrained transfer learning model and also tuned the model
The model that we have used is InceptionResNetV2 model
This model has 164 layers and total parameters after tuning is 8,319,531

**LIBRARIES NEEDED**

* NUMPY

* PANDAS

* SEABORN

* SCIKIT-LEARN

* TENSORFLOW

* WARNINGS

* TQDM

* MATPLOTLIB

**ACCURACY**

Using this model we got an accuracy of 88%

**VISUALISATION**

<h4>Confusion Matrix</h4>
<img src = "https://github.com/Suryageeks/ML-Crate/blob/main/Eye%20Disease%20Prediction/Images/image1.png " alt="Confusion Matrix" title="Confusion Matrix" style="width:60%" />
<h4>Classification Report</h4>
<img src = "https://github.com/Suryageeks/ML-Crate/blob/main/Eye%20Disease%20Prediction/Images/image2.PNG" alt='Classification Report' title="Classification Report" style="width:60%" />
<h4>Visualisation of Categories</h4>
<img src = "https://github.com/Suryageeks/ML-Crate/blob/main/Eye%20Disease%20Prediction/Images/image3.png " alt="Visualisation of Categories" title="Visualisation of Categories" style="width:60%" />


**CONCLUSION**

Thus using this model we can accurately predict the type of corneal ulcers in the eyes

**CONTRIBUTED BY:-**

*Surya Sarkar*

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/suryasarkar1282) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Suryageeks)


