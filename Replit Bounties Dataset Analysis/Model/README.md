**PROJECT TITLE**

Replit Bounties Dataset Analysis

**GOAL**

The goal of the project is to create a data analysis model for analyzing the data in the Replit Bounties Dataset on Kaggle and Find out different patterns in Replit Bounties.

**DATASET**

Link to the dataset: https://www.kaggle.com/datasets/ibrahimonmars/replit-bounties-dataset

**DESCRIPTION**

Used Linear Regression, Decision Tree Classifier, K-Nearest Neighbours (KNN) algorithms to implement the predictive models. Compared all the algorithms used to find out the best fitted algorithm for the model by checking the accuracy scores.

**WHAT I HAD DONE**

1. Performed **Exploratory Data Analysis (EDA)** and **Preprocessing** on the dataset to understand the structure of the data and identify relations between different fields. To visualize these findings, bar graphs/histograms were plotted.

2. **Data Cleaning:** Analyzed the dataset for missing values, null entries, and duplicate records. Unnecessary data, such as the 'status' parameter which was always 'Open', was removed. No null entries or duplicate values were found in this dataset.

3. **Data Transformation:** Converted the 'bounty' and 'coins' columns from string representations to float values by removing '$' and ',' symbols. Additionally, Label Encoding was performed on the 'title' and 'time' fields for easier analysis.

4. **Linear Regression:** Built and trained a predictive model using Linear Regression to predict the bounty amount based on the title. The dataset was split into 75% training data and 25% testing data. Model accuracy was evaluated using Mean Absolute Error, Mean Squared Error, and Root Mean Squared Error.

5. **Decision Tree:** Used the Decision Tree algorithm to classify Replit bounties based on their companies. The resulting model was visualized using the Graphviz library. Insights from the decision tree visualization were obtained to understand the most important features for classification.

6. **KNN Classifier:** Implemented a model for predicting the title of a bounty given its amount, coins, and time using KNN Classifier. The model's performance was evaluated using confusion matrix and classification report metrics.

**MODELS USED**

1. **Linear Regression:**
   - **Reason:** Linear Regression was chosen to build a predictive model for estimating the bounty amount based on the title. This algorithm was selected due to its simplicity, interpretability, and effectiveness in modeling linear relationships between variables. Since the goal was to predict a numerical value (bounty amount), Linear Regression was a suitable choice for this regression task.

2. **Decision Tree:**
   - **Reason:** Decision Tree algorithm was utilized for classifying Replit bounties based on their companies. Decision Trees were selected because they can handle both numerical and categorical data, and they are interpretable, allowing us to understand the decision-making process behind the classification.

3. **K-Nearest Neighbors (KNN) Classifier:**
   - **Reason:** KNN Classifier was employed to predict the title of a bounty given its amount, coins, and time. KNN was chosen for its simplicity and ability to handle non-linear relationships between variables. It does not make any assumptions about the underlying data distribution, making it suitable for this classification task. Additionally, KNN is a lazy learner, which means it does not require training time, making it efficient for small to medium-sized datasets.

**LIBRARIES NEEDED**

1. numpy
2. pandas
3. matplotlib
4. seaborn
5. plotly
6. missingno
7. scikit-learn
8. IPython
9. graphviz

**VISUALIZATION**
![Bounty_histogram](https://github.com/zul132/ML-Crate/assets/98112914/96edc5bc-b06d-4ae7-b149-26e021aa3640)
![Time_bar_plot](https://github.com/zul132/ML-Crate/assets/98112914/4733f9b8-4e58-4bfd-9fd3-56b0506e375f)
![bounty_company_bar](https://github.com/zul132/ML-Crate/assets/98112914/cea09489-a0e0-46b3-9617-4cc565e9cf8f) 
Missing values Matrix
![missingno_matrix](https://github.com/zul132/ML-Crate/assets/98112914/a72f849e-bfed-4166-ac04-7d3251e952a3) 
![corr_heatmap](https://github.com/zul132/ML-Crate/assets/98112914/b5c66a87-30b2-4b19-83c6-66ff4519b68b) 
![pairplot](https://github.com/zul132/ML-Crate/assets/98112914/b1f5d0b0-ad85-4394-95a4-12adffa2be7b)


**CONCLUSION**

1. During EDA, it was observed that there is a direct correlation between the bounty amount and coins. To put it precisely, one Replit coin is equivalent to $100 bounty. Thus, these two fields can be combined into a single column.
2. A linear relationship between the bounty amount and the company offering bounty was also observed from the plots. The companies offering the highest bounty amounts were observed to be Human-Protocol, YazanMoghrabi and WilliamBarber7. The bounties most often offered were 45, 90, 180 and 22.5 USD.
3. The Predictive models implemented using Linear Regression, Decision Tree, and KNN algorithms were all observed to be reasonably accurate, with the Linear Regression model performing best, having the least Absolute error of just 0.04 approximately.

**YOUR NAME**

Fathima Zulaikha

https://www.linkedin.com/in/fathima-zulaikha-2741a4217/

https://github.com/zul132
