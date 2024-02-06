**Bundesliga Season Analysis**

**GOAL**

This project aims at analyzing data from the previous 2 seasons along with few matches from the current season of the Bundesliga in order to gain insights on players and team performances. In addition to analyzing data the project uses available data to predict future events such as match results or number of goals scored by some player.

**DATASET**

https://www.kaggle.com/datasets/memocan/bundesliga-2021-2024-complete-season-analysis

**DESCRIPTION**

The project consists of 2 parts, the first part focuses on teams data and the second focuses on players data. Each part has its analysis and modeling part.

**WHAT I HAD DONE**
 
    - Importing neccesary libraries

    - Reading and understanding teams data 

    - Feature Engineering 

    - Data Cleaning 

    - Data Analysis and Visualization 

    - Encoding categorical columns 

    - train test split

    - models training and evaluation

**MODELS USED**

**Match Result Prediction Models**
1. Logistic Regression: provides interpretable coefficients, making it useful for understanding the impact of different features on the predicted outcome.

2. K-Nearest Neighbors (KNN): a straightforward algorithm, doesn't make any assumptions about the underlying data distribution.

3. Decision Tree: implicitly perform feature selection by choosing the most informative features at each split, Robust to Outliers

**Player Goals Prediction Models**
1. Linear Regression: Simple and interpretable and provides a baseline model

2. K-Nearest Neighbors (KNN)

3. Random Forest: High Predictive Accuracy, Ease of Use, Reduced Sensitivity to Noisy Data

4. XGBoost: excels in capturing complex relationships within the data and is widely used for tasks requiring high predictive accuracy.



**LIBRARIES NEEDED**

    - Pandas
    
    - Numpy
    
    - Sklearn
    
    - xgboost
    
    - Matplotlib
    
    - Seaborn
        
    - Plotly
**VISUALIZATION**

<!-- Row 1 -->
<div style="display: flex;">

  <!-- Image 1 -->
  <div style="flex: 20%;">
    <img src="../Images/Home wins for each team.png" alt="Home wins for each team" style="width:100%">
  </div>

  <!-- Image 2 -->
  <div style="flex: 20%;">
    <img src="../Images/away wins for each team.png" alt="Away wins for each team" style="width:100%">
  </div>

  <!-- Image 3 -->
  <div style="flex: 20%;">
    <img src="../Images/percentage of home winning.png" alt="Percentage of home winning" style="width:100%">
  </div>
   
  <!-- Image 4 -->
  <div style="flex: 20%;">
    <img src="../Images/win xG and game.png" alt="Win xG and game" style="width:100%">
  </div>
    
  <!-- Image 5 -->
  <div style="flex: 20%;">
    <img src="../Images/goals vs xG.png" alt="Goals vs xG" style="width:100%">
  </div>

</div>

<!-- Row 2 -->
<div style="display: flex;">

  <!-- Image 6 -->
  <div style="flex: 20%;">
    <img src="../Images/frequency of match results.png" alt="Frequency of match results" style="width:100%">
  </div>

  <!-- Image 7 -->
  <div style="flex: 20%;">
    <img src="../Images/lng balls aerials won.png" alt="Lng balls aerials won" style="width:100%">
  </div>

  <!-- Image 8 -->
  <div style="flex: 20%;">
    <img src="../Images/lng balls fouls.png" alt="Lng balls fouls" style="width:100%">
  </div>

  <!-- Image 9 -->
  <div style="flex: 20%;">
    <img src="../Images/tckls ints.png" alt="Tackles vs Interceptions" style="width:100%">
  </div>

  <!-- Image 10 -->
  <div style="flex: 20%;">
    <img src="../Images/teams data pairwise correlations.png" alt="Teams data pairwise correlations" style="width:100%">
  </div>

</div>

<!-- Row 3 -->
<div style="display: flex;">

  <!-- Image 11 -->
  <div style="flex: 20%;">
    <img src="../Images/players data frequency of goals scored.png" alt="Players data frequency of goals scored" style="width:100%">
  </div>

  <!-- Image 12 -->
  <div style="flex: 20%;">
    <img src="../Images/players average minutes played per position.png" alt="Players average minutes played per position" style="width:100%">
  </div>

  <!-- Image 13 -->
  <div style="flex: 20%;">
    <img src="../Images/players age distribution.png" alt="Players age distribution" style="width:100%">
  </div>
    
  <!-- Image 14 -->
  <div style="flex: 20%;">
    <img src="../Images/players data mutual information scores.png" alt="Players data mutual information scores" style="width:100%">
  </div>

  <!-- Image 15 -->
  <div style="flex: 20%;">
    <img src="../Images/players data pairwise correlations.png" alt="Players data pairwise correlations" style="width:100%">
  </div>

</div>



**ACCURACIES**

**Match result prediction accuracies**

1. logistic regression: 84%

2. k-nearest neighbors: 78%

3. decision tree: 65%

**Player Goals Goals prediction root mean squared errors**
1. Linear Regression: 23084745303.70263

2. K-Nearest Neighbors (KNN): 0.26034959089814597

3. Random Forest: 0.24604634364707467

4. XGBoost: 0.24353236626038605

**CONCLUSION**

The logistic regrssion model is the best model to predict match results, the XGBoost model is the best to predict players goals scored

**Contribution by**

[Ahmed Anwar](https://www.linkedin.com/in/ahmed-anwar-637ab3225/)