**FLICKR8k Dataset Analysis (MS COCO)**

**GOAL**

The aim of the project is to build a model which can generate captions from images

**DATASET**

The dataset used was the flickr8 dataset which has 8000 images from kaggele: https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip (Images) https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip (Text Files)
Download glove.6B,200.txt from: https://www.kaggle.com/incorpes/glove6b200d

**DESCRIPTION**

In this project, we first use convoluted neural network (CNN) to extract features from images and then use LSTM which is a recurrent neural network to generate captions for the images.

**WHAT I HAD DONE**

Steps followed:
* Downloaded the dataset from kaggle
* Preprocessed the data: this dataset had 8000 images and each image had five captions describing it, so we created a python dictionary with image names as key and the five captions in a list as the values. We then divided the dataset in train and test split with train split having 6000 images.
* Built a vocabulary of words from the captions avaliable which had been used atleast 10 times. We then used pretrained GloVe (global vectors: 6B 200d) to create a vector for each word in the vocabulary 
* We used the InceptionV3 network which is pre-trained on the ImageNet dataset to extract features from the images in train set
* Then we build a model where we combine the image vector and the partial caption
* After training the model we use greedy search (words in the vocabulary we greedily pick the word with the highest probability to get the next word prediction) and beam search (where we take top k predictions, feed them again in the model and then sort them using the probabilities returned by the model) to generate captions for unseen images

**MODELS USED**

InceptionV3: It is our CNN layer used to extract features from images, it is pre-trained on the ImageNet dataset. Ad we do not need to classify the images here, and only need to extract an image vector for our images, we remove the softmax layer from the inceptionV3 model.

LSTM: Long short term memory is a recurrent neural network which has the capability to remember information for long periods of time

**LIBRARIES NEEDED**

* Pandas
* Matplotlib
* Numpy
* Tensorflow
* Keras



**CONCLUSION**

In this project we successfully built and trained the model to generate captions from images, the number of epochs used is 5 and the loss was 2.6, this can be improved by increasing the number of epochs to get more accurate captions but it may take a lot of time. When we fed the model some unseen images it was able to generate proper sentences but it did miss classify some objects but that can be improved by increasing the number of epochs.  

**Contribution by**

Karishni Mehta
Github: https://github.com/karishni