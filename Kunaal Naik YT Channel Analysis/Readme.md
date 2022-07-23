# Kunaal Naik Youtube Channel Analysis
**Goal:**
Perform exploratory data analysis and predictive analysis on the YT chaneel's datasets and analyse the revenue, earnings and views.

**DATASET:**
(https://www.kaggle.com/datasets/funxexcel/data-science-with-kunaal-naik-youtube-channel-data)

## Description
The project is a collection of analysis of over six various datasets that contain various parameters to analyze.
Analyzed parameters include:
1. Revenue.
2. Estimated earnings.
3. Age groups count that view the channel.
4. Views with respect to publish month, days, and overall months in the corresponding years.

## Libraries used:
1. Pandas - for data wrangling
2. Pandas-profiling - to generate the EDA reports for datasets 
3. Seaborn - for large visual plots like histograms and distribution plots
4. Numpy - computation of huge arrays
5. Matplotlib - for plotting and visualization
6. Scikit Learn - to implement various ML techniques and algorithms 
7. Pickle - for pickling the ML model

## Visualizations
### Pie chart for age group analysis
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Kunaal%20Naik%20YT%20Channel%20Analysis/Images/Age%20Groups%20viewing%20the%20channel%20videos%20-%20Age%20Group%20dataset.png"/>

### Views analysis for the traffic dataset
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Kunaal%20Naik%20YT%20Channel%20Analysis/Images/Views%20distribution%20(traffic%20dataset).png"/>

### Views ddistribution (Videos dataset)
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Kunaal%20Naik%20YT%20Channel%20Analysis/Images/Views%20distribution%20-%20video%20dataset.png"/>

### Analysis for watchtime in hours per day
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Kunaal%20Naik%20YT%20Channel%20Analysis/Images/Watch%20in%20hours%20per%20day%20-%20dates%20dataset.png"/>

### Random Forest Regressor analysis results with evaluation metrics
<img src = "https://github.com/PiyushBL45t/ML-Crate/blob/main/Kunaal%20Naik%20YT%20Channel%20Analysis/Images/Decision%20tree%20regressor%20implementation%20with%20evaluation%20metrics.png"/>

## Set of operations performed:
1. First cleaned each dataset.
2. Performed the date time conversions for specific columns in few datasets.
3. Then used seaborn for computing the distribution of views, watch time in hours and comparing the average time.
4. Used the Pandas profiling library to generate the Dxploratory Data Analysis Reports.
5. Then on the dates dataset separeted the train and test variables.

## ML techniques implemented:
1. Implemented two ML algorithms:
      1. Linear Regression
      2. Random Forest Regressor
2. checked the accuracy and training scores.
3. Pickled the model with highest training socres.

## View the reports in the Model directory's Report folder of the project. You can view them in the browser as they all are HTML files.
