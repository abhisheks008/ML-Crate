# Title: Premier League Match Analysis

<hr>

## Abstract/Brief Description about the Project:
The dataset contains the information about the league matches held in the year 2019-20 and has all the match statistics. Here I have made the current points table from the dataset using required parameters.
<hr>

## Dataset: 
**The dataset which is used here, is collected from Kaggle website. Here is the link of the dataset :** <br>
https://www.kaggle.com/datasets/idoyo92/epl-stats-20192020
<hr>

## Goal/Aim of the project: 
**Analyze the PL matches for the season of 2019-20**
<hr>

## Libraries used: 
- ```Numpy```
- ```Pandas```
- ```Matplotlib```
- ```Seaborn```
- ```Sklearn```
<hr>

## Data Visualization:

Points Table

![current_points_table](https://user-images.githubusercontent.com/81156510/180931372-b4b20e42-9ce9-4058-98f2-a5319e28b5eb.png)

<hr>

## Conclusion and Insights:
### General Insights
- Liverpool is highest as per the actual points table.
- But Manchester City was expected to be at the top of the table.

### Performance:
- Liverpool is over-performing because its better in the actual position than the predicted(expected) position.

- Manchester City is under-performing because it was better in the expected position but the actual position was disheartening.

### Model :
3 Models are built that compares a part of the datasets actual and predicted positions. Accuracy is calculated on the basis of [r2 Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html). They are as follows:
- Multi Output Regressor
- K Neighbours Regressor
- Decision Tree Regressor
<hr>

<table>
    <tr>
        <th><u>Model Name</u></th>
        <th><u>r2 Score</u></th>
    </tr>
    <tr>
        <th>Multi Output Regressor</th>
        <th>0.13599170702802976</th>
    </tr>
    <tr>
        <th>K Neighbours Regressor</th>
        <th>0.16308721644927548</th>
    </tr>
    <tr>
        <th>Decision Tree Regressor</th>
        <th>0.6670992571377428</th>
    </tr>
</table>

- We can intepret from the above table is Decision Tree Regressor performs the best as it has higher r2 Score compared to the others.
- But some times with varying parameters Decision Tree Regressor also under performs, hence we need to adjust the parameters accordingly.

<hr>

P.S.: ```requirements.txt``` contains all the libraries in the virtual environment that was run on the cloud based platform that has its own prerequistes too installed. Hence advicesable to use ```!pip install <lib_name>``` command as and when required to run the notebook.
<hr>


**CONTRIBUTION BY:** Sriniketh J

[![Linkedin](https://img.shields.io/static/v1?label=&message=Linkedin&color=%230A66C2&logo=Linkedin)](https://www.linkedin.com/in/sriniketh-jayasendil/) [![Github](https://img.shields.io/static/v1?label=&message=Github&color=%23181717&logo=Github)](https://github.com/srini047) [![Twitter](https://img.shields.io/static/v1?label=&message=Twitter&color=%231DA1F2&logo=Twitter)](https://twitter.com/srini047)
