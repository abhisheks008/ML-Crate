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
<br /> this dataset contains '?' as missing values due to which column A2,A14 dtype was initially object which could be seen in sns.countplot() <br />
Handled '?' using NaN and  rectified dtype of A2,A14 columns <br />
for Categorical missing values ,I have replaced with most_frequent_ones as they were not many missing values<br />
for numerical missing values, I have reolaced with wnd_of distribution as they were many outliers<br />
used one hot encoding for handling categorical features<br />
<br />
## MODELS USED<br />
Decsion Tree, Logistic Regression, KNN, RandomForest Classifier<br />
Reason: Because the given problem is a binary classification problem<br />
<br />

models and Accuracy <br />
Accuracy of Decision Tree -  74.8792270531401<br />
Accuracy of Logistic Regressuon- 84.05797101449275 <br />
Accuracy of  RandomForest Classifier- 84.526756808227 <br />
Accuracy of KNN(fo n_neighbors= 3)- 68.11594202898551

