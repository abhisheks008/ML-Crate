# Music Recommendation System

## Goal

The main goal of this project is to develop a machine learning model that can recommend music to the users based on their listening history and the listening history of other users. The model will be developed using the scikit-learn library and evaluated using appropriate metrics.

## Dataset

The dataset for this project can be found at [Kaggle](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset).

For more information about the dataset, please refer to this readme file in the Dataset folder [Dataset Description](../Dataset/README.md).

## Approach

1. **Data loading and exploration:** Loaded the dataset, explored the dataset using pandas profiling, and performed exploratory data analysis. In EDA, I have used different plots to visualize the relationship between the features. I have used the seaborn and matplotlib libraries to create the plots. The visualizations include line plots, bar plots, and word clouds.

2. **Data preprocessing:** Performed data preprocessing steps such as temporal feature handling like year, decade with the help of python lambda function.

3. **Model development:** Developed the model using the scikit-learn library. The model is developed using the following algorithm and then further dimensionality reduction techniques are applied to the model to visualize the clusters. The following algorithms are used to develop the model:

```bash
a. K-Means Clustering:

- Description: K-Means clustering is an unsupervised learning algorithm that seeks to partition the dataset into K distinct, non-overlapping clusters. It works iteratively to assign each data point to one of K clusters based on the features that are provided. Data points are clustered based on feature similarity.
```

```bash
b. Principal Component Analysis (PCA):

- Description: PCA is a linear dimensionality reduction algorithm that seeks to project the features of the dataset onto a lower-dimensional space in such a way that the variance of the dataset in the low-dimensional representation is maximized.
```

```bash
c. t-Distributed Stochastic Neighbor Embedding (t-SNE):
- Description: t-SNE is a non-linear dimensionality reduction algorithm that is well-suited for embedding high-dimensional data for visualization in a low-dimensional space of two or three dimensions.
```

4. **Model evaluation:** Evaluated the performance of the model using appropriate metrics such as euclidean distance, spatial distance, and other similarity metrics. The Scikit-learn library and SciPy library are used to evaluate the model based on these metrics.

## Libraries Needed

- Numpy
- Pandas
- Seaborn
- Matplotlib
- Scipy
- Plotly
- Wordcloud
- Spotipy
- Scikit-learn

## Clustering Visualization

- Cluster Visualization using PCA
  ![Clusters of Songs](..\Images\clusters_of_songs.png)

- Cluster Visualization using t-SNE
  ![Clusters of Genres](..\Images\clusters_of_genres.png)

## Model Prediction

```
recommend_songs([{'name': 'Blinding Lights', 'year': 2019}], data)
- Fetching song information from spotify dataset
[{'name': 'Best News Ever', 'year': 2017, 'artists': "['MercyMe']"},
 {'name': 'Bit By Bit', 'year': 2012, 'artists': "['Mother Mother']"},
 {'name': 'Hotel Ceiling', 'year': 2014, 'artists': "['Rixton']"},
 {'name': 'We Go Together Like', 'year': 2020, 'artists': "['Abby Anderson']"},
 {'name': "Somethin' Bad (with Carrie Underwood) - (Duet with Carrie Underwood)",
  'year': 2014,
  'artists': "['Miranda Lambert', 'Carrie Underwood']"},
 {'name': 'A Different World (feat. Corey Taylor)',
  'year': 2016,
  'artists': "['Korn', 'Corey Taylor']"},
 {'name': 'Sober', 'year': 2015, 'artists': "['Selena Gomez']"},
 {'name': 'Almost Maybes', 'year': 2020, 'artists': "['Jordan Davis']"},
 {'name': "Don't Say Goodnight",
  'year': 2014,
  'artists': "['Hot Chelle Rae']"},
 {'name': 'Sight of the Sun - Single Version',
  'year': 2014,
  'artists': "['fun.']"}]
```

```
recommend_songs([{'name': 'Fix You', 'year':2005}], data)
- Fetching song information from local dataset
[{'name': 'Have I Told You Lately',
  'year': 1989,
  'artists': "['Van Morrison']"},
 {'name': 'Amazing Grace (My Chains Are Gone)',
  'year': 2020,
  'artists': "['Pentatonix']"},
 {'name': 'Fine Line', 'year': 2019, 'artists': "['Harry Styles']"},
 {'name': 'Goodbye', 'year': 1993, 'artists': "['Air Supply']"},
 {'name': 'Thank You For Loving Me', 'year': 2000, 'artists': "['Bon Jovi']"},
 {'name': 'Stop Crying Your Heart Out', 'year': 2002, 'artists': "['Oasis']"},
 {'name': 'Awake My Soul', 'year': 2009, 'artists': "['Mumford & Sons']"},
 {'name': 'Ashes of Eden', 'year': 2015, 'artists': "['Breaking Benjamin']"},
 {'name': 'Go the Distance', 'year': 1997, 'artists': "['Michael Bolton']"}]
```

```
recommend_songs([{'name': 'I Will Follow', 'year':2010},{'name': 'Come As You Are', 'year':1991}],  data)
- Fetching song information from local dataset
[{'name': 'Face Down',
  'year': 2006,
  'artists': "['The Red Jumpsuit Apparatus']"},
 {'name': 'BURN IT DOWN', 'year': 2012, 'artists': "['Linkin Park']"},
 {'name': 'The Last Stand', 'year': 2016, 'artists': "['Sabaton']"},
 {'name': 'In Your Eyes (feat. Kenny G) - Remix',
  'year': 2020,
  'artists': "['The Weeknd', 'Kenny G']"},
 {'name': 'Pray to God (feat. HAIM)',
  'year': 2014,
  'artists': "['Calvin Harris', 'HAIM']"},
 {'name': '空に歌えば', 'year': 2017, 'artists': "['amazarashi']"},
 {'name': 'Stranded', 'year': 2016, 'artists': "['Gojira']"},
 {'name': 'Tequila - R3HAB Remix',
  'year': 2018,
  'artists': "['Dan + Shay', 'R3HAB']"},
 {'name': 'Charlie', 'year': 2006, 'artists': "['Red Hot Chili Peppers']"},
 {'name': 'War of Change',
  'year': 2012,
  'artists': "['Thousand Foot Krutch']"}]
```

## Conclusion

In conclusion, this project aimed to develop a music recommendation system using the listening history of the users and the listening history of other users. The dataset was loaded and explored. The dataset was preprocessed by handling temporal features such as year and decade. The model was developed using the scikit-learn library. Clustering algorithms such as K-Means Clustering, Principal Component Analysis (PCA), and t-Distributed Stochastic Neighbor Embedding (t-SNE) were used to develop the model. The model was evaluated using appropriate metrics such as euclidean distance, spatial distance, and other similarity metrics. The model was able to recommend songs to the users based on their listening history. The model was able to recommend songs to the users based on the name and year of the song.

## Author [Sitam Meur](https://github.com/sitamgithub-MSIT)

## References

- Scikit-learn Documentation: https://scikit-learn.org/stable/modules/clustering.html
- Dimensionality Reduction: https://scikit-learn.org/stable/modules/decomposition.html
- Scipy Documentation: https://docs.scipy.org/doc/scipy/reference/
- Plotly Documentation: https://plotly.com/python/
- Spotipy Documentation: https://spotipy.readthedocs.io/en/2.22.1/
