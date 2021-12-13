*This folder will be for storing the model created for the ML project. The file format should be in .ipynb.*

# MNIST Dataset Classification

### Goal  
Our aim here is to create/explore machine learning models for handwritten digit recognition.

## MNIST Handwritten Digits dataset

source : http://yann.lecun.com/exdb/mnist/

## DESCRIPTION

In this project we aim to find the best model fit for classifying the handwritten digit images in the MNIST dataset. We first need to know information about the data and then develop a proper approach to go about solving it, and that's what I did.

### WHAT I HAD DONE
In this project we don't to do any kind of preprocessing or EDA or anything so it's a pretty straight forward approach.
1. Visualize the data 
    - Dimensions of image
    - Is the data in jpeg format, numpy array, tensor ....
2. Spliting the Dataset into Trainging/Validation/Test set
    - I have used only 10k images (total images we have is 60000) initially, because otherwise the training process would become quite time consuming
3. Selecting a Model
4. Training the selected Model again on the entire dataset
5. Generate Predictions 
6. Save the Model

### MODELS USED
1. Logistic Regression 
    - this is a pretty simple choice but in some cases effective none the less.
2. Random Forest 
    - this is a good ensemble model which is quite a good choice for classification problems
3. 3 Layer Neural Network
    a. 64 Hidden units 
    b. 128 Hidden units

**ALL LIBRARIES NEEDED CAN BE FOUND IN THE REQUIREMENTS.TXT**

ACCURACIES

| **Model** | Validation Accuracy | 
| ---| --- |
| 1. Logistic Regression | 84.4% | 
| 2. Random Forest | 95% |
| 3. 3 layer NN | 97% | 

I also tried using 4 layers and played around with the number of hidden units and in some cases the accuracy did increase a bit but at the same time the computation time also increased, and by a lot if I may add. 

So in conclusion I ended up selecting the 3 layer NN with 64 hidden units as the most optimal option.

![image](https://user-images.githubusercontent.com/90238742/145832775-c7c5cc8b-4886-4635-8107-fe105e96cd37.png)



Name: Yagyesh Bobde \
Github: https://github.com/yagyesh-bobde \
medium: https://medium.com/@Yagyesh_bobde \
linkedin: https://www.linkedin.com/in/yagyesh-bobde-177523220/
