**📍PROJECT TITLE**

 Face Mask Detection

**📍GOAL**

Detect the face mask using a machine learning approach.

**📍DATASET**

[Kaggle](https://www.kaggle.com/andrewmvd/face-mask-detection)

**📍DESCRIPTION**

Main aim is to build a model that can predict whether a person is wearing mask properly, not properly or not at all wearing mask from a set of 853 files.

**📍WHAT I HAD DONE**

Developed a Sequential Model that uses a total of around 68 Lakhs parameter to detect to which of the three classes the given image belongs to.

**📍MODEL USED**

![model-1](https://user-images.githubusercontent.com/81156510/153702526-36cca1a4-ae69-467e-8692-d15c7def2314.png)

A Convolutional Model (CNN) with 4 convolutional layers, 3 max-pooling layers, and Relu and Softmax as activation functions.
Used ```adam``` as Optimizer, ```categorical_rossEntropy``` as Loss Function, ```accuarcy``` as metrics
with ```batch_size``` as 64, ```epochs``` as 20, and ```seed``` as 1000.

> Can also use other parameters as per your wish to make the model more robust.

**📍LIBRARIES NEEDED**

The required libraries for this project work:

- Seaborn
- Numpy
- Pandas
- Sklearn
- Matplotlib
- Tensorflow
- Keras
- OS
- XML
- Random
- CV2

and few others.

**📍VISUALIZATION**

![output-1](https://user-images.githubusercontent.com/81156510/153702527-ea8751a0-4a4a-46bb-bfe9-0e4740c18a60.png)


**📍ACCURACIES**

![output-2](https://user-images.githubusercontent.com/81156510/153702529-d037f3fa-b85e-44e1-92bc-def379f64404.png)


**📍CONCLUSION**

The model that is built performs good on the train data but performs much better on the test data (random samples taken). The same can be inferred from the image above and those stats will vary for a different dataset.
