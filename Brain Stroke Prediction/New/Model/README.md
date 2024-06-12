## **Brain Stroke Prediction** ##

## **Goal:** ##

To cleanse and analyse the data to understand the data and make the best performing Neural Network for the same.

## **Dataset:** ##

 https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

## **Description:** ##

 Brain stroke is very common disease nowadays. Through this model, we try to predict that if a person might suffer from a Brainstroke based on the given inputs such as work type, residence type, BMI, glucose levels, smoking etc

## **What I Had Done:** ##
* Basic data exploration using pandas
* Cleaning the data and transforming it for the neural network to understand using pandas
* Data visualisation using seaborn and matplotlib
* Making Neural Networks with Tensorflow by using various layers, activation functions and regularisers

## **Model implemented:** ##
* Model - 1: 3 layers with relu and sigmoid activation functions
* Model - 2: 6 layers with relu and sigmoid activation functions
* Model - 3: 3 layers with linear and sigmoid activation functions
* Model - 4: 3 layers with relu and sigmoid activation functions with equal units and L2 regularised
* Model - 5: 12 layers with relu and sigmoid activation functions with L2 regularised
* Model - 6: 4 layers with relu and sigmoid activation functions with L2 equlaliser and inputs units = number of parameters aka x
* Model - 7: 9 layers with both relu and linear and L2 regulariser with same units <br/>
All models are Neural Networks using sequential and dense layers since these architectures are well suited for predictions and regression tasks on these types of data. Since the output is going to be binary, I used sigmoid in the output layer of all models.

## **Libraries Needed:** ##
* pandas
* seaborn
* matplotlib
* sklearn
* tensorflow

## **Exploratory Data Analysis Results** ##
![DA Graph 1](</Brain Stroke Prediction/New/Pictures/Screenshot 2024-06-08 001109.png>) ![DA Graph 2](</Brain Stroke Prediction/New/Pictures/Screenshot 2024-06-08 001118.png>) ![DA Graph 3](</Brain Stroke Prediction/New/Pictures/Screenshot 2024-06-08 001128.png>) ![DA Graph 4](</Brain Stroke Prediction/New/Pictures/Screenshot 2024-06-08 001134.png>)


## **Performance of the Models based on the Accuracy Scores:** ##
* Model - 1: 95.18% training accuracy and 95.5% test accuracy. 
* Model - 2: 95.41% training accuracy and 95.5% test accuracy. 
* Model - 3: 94.29% training accuracy and 95.5% test accuracy. 
* Model - 4: 94.91% training accuracy and 95.5% test accuracy. 
* Model - 5: 95.05% training accuracy and 94.42% test accuracy. 
* Model - 6: 94.83% training accuracy and 95.5% test accuracy. 
* Model - 7: 95.6% training accuracy and 95.3% test accuracy.  <br/>
All models had no overfitting or underfitting.

## **Conclusion:** ## 
 Best performing model was Model - 7 consisting of 9 layers with both relu and linear activation functions along with L2 regularisers and same number of units. This model had 95.6% training accuracy and 95.3% test accuracy.

## **Contributed By:** ##
Armaan Jagirdar <br/>
Github: https://github.com/Armaan457
