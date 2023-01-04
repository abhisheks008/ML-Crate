# Credit Card Approval Prediction<br />
## GOAL<br />
 Create a prediction model based project which will predict whether a credit card is going to be approved or, not.
## DATASET <br />
https://www.kaggle.com/datasets/devzohaib/predicting-credit-card-approvals
## DESCRIPTION<br />
Commercial banks receive a lot of applications for credit cards. Many of them get rejected for many reasons, like high loan balances, low income levels, or too many inquiries on an individual's credit repor.<br />
This file concerns credit card applications. All attribute names and values have been changed to meaningless symbols to protect confidentiality of the data.

This dataset is interesting because there is a good mix of attributes -- continuous, nominal with small numbers of values, and nominal with larger numbers of values. There are also a few missing values.

Attribute Information:

A1: b, a.<br />
A2: continuous.<br />
A3: continuous.<br />
A4: u, y, l, t.<br />
A5: g, p, gg.<br />
A6: c, d, cc, i, j, k, m, r, q, w, x, e, aa, ff.<br />
A7: v, h, bb, j, n, z, dd, ff, o.<br />
A8: continuous.<br />
A9: t, f.<br />
A10: t, f.<br />
A11: continuous.<br />
A12: t, f.<br />
A13: g, p, s.<br />
A14: continuous.<br />
A15: continuous.<br />
A16: +,- (class attribute)<br />


## WHAT I HAVE DONE<br />
1. this dataset contains '?' as missing values due to which column A2,A14 dtype was initially object which could be seen in sns.countplot() 
2. Handled '?' using NaN and  rectified dtype of A2,A14 columns 
3. for Categorical missing values ,I have replaced with most_frequent_ones as they were not many missing values<br />
4. for numerical missing values, I have reolaced with wnd_of distribution as they were many outliers<br />
5. used one hot encoding for handling categorical features<br />
<br />

## MODELS USED<br />
Decsion Tree, Logistic Regression, KNN, RandomForest Classifier<br />
Reason: Because the given problem is a binary classification problem<br />
<br />

## LIBRARIES
* NumPy
* Pandas
* Matplotlib
* Seaborn
* sklearn
## VISUALIZATION
![A1](https://user-images.githubusercontent.com/97605562/210540074-ade56fd2-1002-497b-84b0-2bec860a0dcc.jpg)
![A4](https://user-images.githubusercontent.com/97605562/210540285-e222385e-ab0c-4f60-8590-04ad2f0f6190.jpg)
![A5](https://user-images.githubusercontent.com/97605562/210540517-8305a48c-89a2-4c77-9b35-ce6108a0c484.jpg)
![A6](https://user-images.githubusercontent.com/97605562/210540558-0409f896-db6c-44df-afa0-2f0077619511.jpg)
![A7](https://user-images.githubusercontent.com/97605562/210540635-17f95353-101d-4bf2-b3f5-81931a02aadd.jpg)
![A9](https://user-images.githubusercontent.com/97605562/210540662-56bd4fa3-5ef4-43c4-87e2-985145116a13.jpg)
![A10](https://user-images.githubusercontent.com/97605562/210540681-21425133-3956-423d-ab94-0dc093b2e082.jpg)
![A12](https://user-images.githubusercontent.com/97605562/210540728-e5daecae-b3b3-4ad4-ad8f-2242615bd60b.jpg)

![A13](https://user-images.githubusercontent.com/97605562/210540739-d081b641-becb-4af9-94f5-9bc3c21a5645.jpg)


## ACCURACIES <br />
Accuracy of Decision Tree -  74.8792270531401<br />
Accuracy of Logistic Regressuon- 84.05797101449275 <br />
Accuracy of  RandomForest Classifier- 84.526756808227 <br />
Accuracy of KNN(fo n_neighbors= 3)- 68.11594202898551

## CONCLUSION
<br /> '?' were there so some numerical columns were having dtype as 'obj" so replsced with NaN
<br />for categorical feature the missing values were not large so can be replaced with most_frequent_ones
<br />for numerical only 2 columns were having missing values so can be handled using end_distribution method

## YOUR NAME
Saurabh Jaiswal
