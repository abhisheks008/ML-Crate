Exploratory Data Analysis:  <br />
<br /> this dataset contains '?' as missing values due to which column A2,A14 dtype was initially object which could be seen in sns.countplot() <br />
Handled '?' using NaN and  rectified dtype of A2,A14 columns <br />
for Categorical missing values ,I have replaced with most_frequent_ones as they were not many missing values<br />
for numerical missing values, I have reolaced with wnd_of distribution as they were many outliers<br />
used one hot encoding for handling categorical features<br />
<br />
<br />
models and Accuracy <br />
Accuracy of Decision Tree -  74.8792270531401<br />
Accuracy of Logistic Regressuon- 84.05797101449275 <br />
Accuracy of  RandomForest Classifier- 84.526756808227 <br />
Accuracy of KNN(fo n_neighbors= 3)- 68.11594202898551

