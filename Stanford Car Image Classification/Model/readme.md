**Stanford Car Image Classification**

**GOAL**

This project aims at using the stanford cars data set to build a model that can recognize the type of the car given a picture of it.

**DATASET**

https://www.kaggle.com/datasets/jutrera/stanford-car-dataset-by-classes-folder

**DESCRIPTION**

The project starts with understanding the data and then proceeds to build and evaluate different image classification models.

**WHAT I HAD DONE**
 
    - Importing neccesary libraries

    - Reading and understanding the data 

    - Data transformations 

    - Creating a validation set

    - Training a convolutional neural network model

    - Adding Addtional layers and Batch Normalization and Dropout layers to the CNN model

    - Fine-tuning resnet34 model

    - used data augmentation to imporove the accuracy of the pretrained model

**MODELS USED**

1. Convolutional Neural Network: The state-of-the-art model for image recognition tasks

2. ResNet34: ResNet34 is favored for image classification due to its ability to train very deep networks effectively, mitigating vanishing gradient issues with skip connections, resulting in improved generalization, parameter efficiency, and state-of-the-art performance.


**LIBRARIES NEEDED**

    - Pytorch
    
    - Matplotlib
    
        
**VISUALIZATION**


Accuracy of CNN model:
<img src="../Images/cnn1 accuracy.png" alt="Accuracy of CNN model" style="width:100%">

Losses of CNN model:
<img src="../Images/cnn2 loss.png" alt="Losses of CNN model" style="width:100%">

Accuracy of CNN model after adding more layers and batch normalization and dropout layers:
<img src="../Images/cnn2 accuracy.png" alt="Accuracy of CNN model after adding more layers and batch normalization and dropout layers" style="width:100%">

Losses of CNN model after adding more layers and batch normalization and dropout layers:
<img src="../Images/cnn2 loss.png" alt="Losses of CNN model after adding more layers and batch normalization and dropout layers" style="width:100%">

Accuracy of fine-tuned ResNet34 model:
<img src="../Images/Accuracy of resnet34.png" alt="Accuracy of fine-tuned ResNet34 model" style="width:100%">

Losses of fine-tuned ResNet34 model:
<img src="../Images/losses of resnet34.png" alt="Losses of fine-tuned ResNet34 model" style="width:100%">

Accuracy of fine-tuned ResNet34 model After data augmentation:
<img src="../Images/Accuracy of data augmented resnet34.png" alt="Accuracy of fine-tuned ResNet34 model After data augmentation" style="width:100%">

Losses of fine-tuned ResNet34 model After data augmentation:
<img src="../Images/losses of data augmented resnet34.png" alt="Losses of fine-tuned ResNet34 model After data augmentation" style="width:100%">


**ACCURACIES**

1. CNN Model: 0.5%

2. CNN model after adding more layers: 0.8% 

3. ResNet34: 35%

4. ResNet34 after data augmentation: 69%

**CONCLUSION**

The data augmented ResNet34 is the best model for our project

**Contribution by**

[Ahmed Anwar](https://www.linkedin.com/in/ahmed-anwar-637ab3225/)