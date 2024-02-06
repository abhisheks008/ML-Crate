# Project Title: Arabic_Hand_written_digit_recognition
# Abstract
In recent years handwritten digit recognition has emerged as important area due to its application in several sectors. This dataset is comprised of 60000 training example and 10000 test images collected unlimited variation in human writing. This project focuses on recognising the arabhic handwritten digit accurately. Various approaches are made to solve the problems and finally result came out that convolutional neural network has increased the accuracy of the model significantly.
The convolutional neural network trained on normalized dataset with the appropriate learning rate chosen has increased the accuracy of the model upto 99.08% with loss 0.065 on test set.
# Dataset:
The dataset is already split in training and test set with labels, can be found on the link below:

https://www.kaggle.com/mloey1/ahdd1

It is a multiclassification problem havving 10 category ranging form 0 to 9.
# Aim of the project:
Aim of this project is to classify arabic hand written digit and predict them accordingly.
# Libraries Used:
* `Numpy`
* `Pandas`
* `matplotlib`
* `seaborn`
* `Tensorflow`
* `keras`
# Data Visualization:
![Random images of the training dataset](https://github.com/Han9128/Arabic_Hand_written_digit_recognition/blob/main/Images/Data_image.png)
![Count plot of lables](https://github.com/Han9128/Arabic_Hand_written_digit_recognition/blob/main/Images/count_plot_digit.png)
# Model Comparision:
| Approach | Accuracy on test set | Error |
| ------| ---------------------| -----|
| Dense NN | 97.74% | 0.143 |
| Convolutional NN | 99.08%| 0.065 |

On comparing the models trained with **Dense NN** and **Convolutional NN (CNN)** it is wide to go for the model trained with **CNN** having high accuracy.
But one problem is with this model is that it is computationally expensive in comparison to the **Dense NN**, so trained for small number of epochs one may try with the large number of opochs having good setup and see if there is any improvement on test set accuracy.
# Final prediction on test set using model trained with **CNN:**
![Prediction](https://github.com/Han9128/Arabic_Hand_written_digit_recognition/blob/main/Images/Prediction.png)
