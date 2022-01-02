# German Traffic Sign Classification

**GOAL**

To build a deep learning framework that classifies traffic signs into the correct categories.

**DATASET**

The dataset is the German Traffic Sign Recognition Benchmark(GTSRB) dataset taken from [Kaggle](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)

**DESCRIPTION**

The project aims at creating a deep learning model using tensorflow and Keras that gets trained on the categorised images in the training set and then it classifies test signs into the correct category of signs.

**WHAT I HAD DONE**

- First I loaded the data and visualised it and found the number of categories.
- Then two lists images and labels were created to store the data in array form.
- Then I split the dataset into training and validation data.
- Then I created a deep learning model and trained it using the training and validation data.
- Finally the trained models were used for classification of test images.

**MODELS USED**

Sequential model by Keras

**LIBRARIES NEEDED**

- numpy
- pandas
- matplotlib
- scikit-learn
- tensorflow
- keras

**ACCURACIES**

The model gave an accuracy of 99.16% after 20 epochs.

**CONCLUSION**

The model was trained for 20 epochs and with 2 hidden layers and it gave a very high accuracy of 99.16%. While tuning the model, it was seen that 20 epochs was a good value to avoid overfitting. The model was also able to successfully classify the test images.

**CONTRIBUTED BY**

Ahan Anupam

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ahan-anupam-ab21411a4/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ahananupam33)
