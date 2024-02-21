<h1>Google PlayStore Analysis and Rating Predictor</h1>

**GOAL**

To analyze the 'Google Playstore Dataset' Dataset using Exploratory Data analysis and make a regression model to predict the rating of the apps.

**DATASET**

https://www.kaggle.com/datasets/madhav000/playstore-analysis

**DESCRIPTION**

The problem is to identify the apps that are going to be good for Google to promote. App ratings, which are provided by the customers, is always a great indicator of the goodness of the app. The problem reduces to: predict which apps will have high ratings.

The dataset contains the following columns:
- App : Applicaton Name
- Category: Category to which the app belongs
- Rating: Overall user rating of the app
- Reviews: Number of user reviews for the app
- Size: Size of the app
- Installs: Number of user downloads/installs for the app
- Type: Paid or Free
- Price: Price of the app
- Content Rating: Age group the app is targeted at - Children / Mature 21+ / Adult
- Genres: An app can belong to multiple genres (apart from its main category). For example, a musical family game will belong to Music, Game, Family genres.
- Last Updated: Date when the app was last updated on Play Store
- Current Ver: Current version of the app available on Play Store
- Android Ver: Minimum required Android version

**WHAT I HAD DONE**

* Checked for missing values and cleaned the data accordingly
* Analyzed the data, found insights and visualized them accordingly.
* Found detailed insights of different columns with one another using plotting libraries.
* Deployed four regression models viz., Linear Regression, Support Vector regression, Decision Tree Regression, Random FOrest Regression to predict the rating.
* Used RMSE(Root Mean Square Error) to evaluate the performance of the models.


**LIBRARIES NEEDED**

1. Pandas
2. Matplotlib
3. Seaborn
4. Plotly
5. Numpy
6. WordCloud
7. Sklearn

**VISUALIZATION**
![App distribution sunburst chart by category](<../Images/App distribution sunburst chart by category.png>)
![App size distribution by category](<../Images/App size distribution by category.png>)
![App distribution by category](<../Images/App distribution by category.png>)
![Average Price By category](<../Images/Average Price By category.png>)
![Category by Content Rating](<../Images/Category by Content Rating.png>)
![wordcloud for category column](<../Images/wordcloud for category column.png>)
![Total installs by category](<../Images/Total installs by category.png>)
![Number of apps by type](<../Images/Number of apps by type.png>)
![Word Cloud for Genre Column](<../Images/Word Cloud for Genre Column.png>)
![Number of applications by content rating](<../Images/Number of applications by content rating.png>)

For more visualization refer the .ipynb file :)

**Model Performances**

|Model                      | RMSE               |
| ------------------------- | -------------------|
|Linear Regression          | 0.5474395094809866 |
|Support Vector Regression  | 0.545564956206932  |
|Decision Tree Regression   | 0.7552190124670595 |
|Random Forest Regression   | 0.7552190124670595 |

- reviews, type, installs and size columns were used to make the regression model with the rating column being the target vector
- high RMSE shows that the data has a wide variation in it.

**CONCLUSION**
- Various Categories of apps have varied ratings
- Most installed apps belonged to the category of 'Game'
- Most of the apps on the playstore are rated for all age groups of audience
- More than 3/4th of the apps are free to install.
- Among the paid apps, finance apps were most expensive having an average price of $8, followed by Lifestyle apps at $6 and medical apps at $3 average.
- All the apps were less than 100 mb.
- Most of the available apps had 'Family' category.
- The Support Vector regression(with rbf kernel) had the minimum RMSE among the algorithms used making it the best model.

**AUTHOR**

- Code contributed by *Mariam* @ #JWoC_2024

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariam-m7084)  
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mariam7084/)
