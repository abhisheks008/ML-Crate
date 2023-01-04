# Fish Segmentation

### Goal
Identify the images of different kinds of fishes using a machine learning model/framework.

### Dataset
Kaggle Dataset given here : [Fish Dataset]( https://www.kaggle.com/crowww/a-large-scale-fish-dataset)

### Description
In this project I used an existing CNN architectures : VGG-16, ResNet50 to predict the images given.

### Work Done
* Importing Keras, Tensorflow, mathplotlib for the solution
* Creating the function that returns the VGG_16 model and ResNet model
* Importing the data, Splitting the dataset to Train and Test (Validation) data and normalising them.
* Training the model. (Uses Early Stopping for maximum accuracy and Adam as an optimiser)
* Plotting the accuracy and loss per epoch

### Model Used
The models used here are VGG_16 from VGG team for ILSVRC-2014 competition, and ResNet 50 from won the top position at the ILSVRC 2015 competition.

### Libraries used
* Keras
* TensorFlow
* Seaborn
* Mathplotlib
* Pathlib
* os

### Final Model Results

#### VGGNet
Accuracy on Train Data : 100%
Accuracy on Test Data : 99.67%

#### ResNet
Accuracy on Train Data : 99.04% 
Accuracy on Test Data : 95.72%

### Model Visualisation

#### VGGNet

![VGGNet](/Fish%20Segmentation/extras/plots/VGGNet.png)

#### ResNet

![ResNet](/Fish%20Segmentation/extras/plots/ResNet.png)


