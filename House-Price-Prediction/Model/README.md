# House price prediction

**GOAL**

prediction of house price in US using linear regression.

**DATASET**

In folder “USA_Housing”.

**DESCRIPTION**

The main aim of the project is to create a model that can predict house prices in US.

**WORK DONE**
- Importing the required packages into our python environment
- Importing the house price data and do some EDA on it
- Data Visualization on the house price data
- Feature Selection & Data Split
- Modeling the data using the algorithms
- Evaluating the built model using the evaluation metrics

**MODELS USED**

We will need to first split up our data into an X list that contains the features to train on, and a y list with the target variable, in this case, the Price column. We will ignore the Address column because it only has text which is not useful for linear regression modeling.

X and y List

`X = HouseDF[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]`

`y = HouseDF['Price']`

Split Data into Train, Test

Now we will split our dataset into a training set and testing set using sklearn train_test_split(). the training set will be going to use for training the model and testing set for testing the model. We are creating a split of 40% training data and 60% of the training set.

```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101) 
X_train and y_train contain data for the training model. X_test and y_test contain data for the testing model. X and y are features and target variable names.
```

*Creating and Training the LinearRegression Model*

We will import and create sklearn linearmodel LinearRegression object and fit the training dataset in it.
```
from sklearn.linear_model import LinearRegression 

lm = LinearRegression() 

lm.fit(X_train,y_train) 
```

OUTPUT
```
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False) 
LinearRegression Model Evaluation
Now let’s evaluate the model by checking out its coefficients and how we can interpret them.

print(lm.intercept_)
```
OUTPUT
```
-2640159.796851911 
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient']) coeff_df
```

**LIBRARIES NEEDED**

* pandas 
* numpy
* seaborn 
* matplotlib.pyplot

**CONCLUSION**

We have created a Linear Regression Model which we help the real state agent for estimating the house price.

**CONTRIBUTION BY**

Vanshika goel

