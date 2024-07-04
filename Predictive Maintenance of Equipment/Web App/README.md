## App demo

A Streamlit web application to provide an interface to the user to input operational parameters and predict if they could cause machine failure, along with a confidence score in the form of probability.  
This can act as a simulation tool, since these parameters are available once the machine starts operating. User can know in advance if certain combinations of parameters are high risk for machine failure, and avoid operating at those conditions.

User can input the following parameters:

1. Product type (Machine quality)
2. Tool wear
3. Air temperature
4. Process temperature
5. Rotational speed
6. Torque

### Prediction: No

![demo-no](/Web%20App/streamlit-app-demo-prediction-no.png)

### Prediction: Yes

![demo-yes](/Web%20App/streamlit-app-demo-prediction-yes.png)

(A video demonstration is also included in the folder.)
