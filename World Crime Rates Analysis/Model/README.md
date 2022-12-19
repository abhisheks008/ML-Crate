**PROJECT TITLE**

**GOAL**

Exploratory analysis on the given dataset country-wise and city-wise

**DATASET**

The data set used can be see here : https://www.kaggle.com/datasets/ahmadjalalmasood123/world-crime-index

**DESCRIPTION**

The dataset contains info about:
1. Cities and their countries
2. The crime index in that city
3. The saftey index in that city
The project intends to categorize countries and cities as ones with highest crime and highest safety indices. It makes use of various libraries of python to do so.

**WHAT I HAD DONE**

1. First I imported all important libraries required for the project.
2. Then, I read in the csv file of the data set.
3. Having done that, I proceeded with some basic EDA such as finding the shape of the data, the number of missing values and the data types present in the given dataset using some inbuilt pandas functions like shape, describe and info.
4. Then, I made a plot based on the number of cities lying in a particular crime index range, which showed me that most cities lie around the 50 - 55 crime index.
5. With this, I decided to separate the cities and their countries as that would help me to do some analysis based only on countries.
6. In doing this, there arose a problem with US and Canadian cities as their name had their state plus country, so I resolved that.
7. Then, I proceeded to find out the top ten coutries with highest crime index and top 10 countries with highest safety index.
8. I also plotted the top 10 safe and top 10 unsafe cities with their crime and safety indices respectively.

**MODELS USED**

No models have been used as this was only an analysis project. No prediction was done.

**LIBRARIES NEEDED**

1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn

**VISUALIZATION**

Histogram plot of number of cities versus their crime index:

![histogram plot of number of cities with crime index](https://user-images.githubusercontent.com/119129594/208433185-d8412206-0535-427a-a156-2eac513f4a04.png)

Top 10 countries with highest crime index:

![top 10 countries with highest crime index](https://user-images.githubusercontent.com/119129594/208433284-d8b2d05e-dee2-4de1-875f-0f984c26c841.jpg)

Top 10 countries with highest safety index:

![top 10 countries with highest safety index](https://user-images.githubusercontent.com/119129594/208433360-0f53796a-b631-4c48-8ff2-80a34b55ed33.jpg)

Top 10 Unsafe Cities:

![top 10 unsafe cities](https://user-images.githubusercontent.com/119129594/208437933-6da74448-dafb-4789-81c5-2e5fac626f08.jpg)

Top 10 Safe Cities:

![top 10 safe cities](https://user-images.githubusercontent.com/119129594/208438009-4070a9b3-6327-4255-9ab2-796f1d602e20.jpg)

**CONCLUSION**

I am not sure about the list because of possible extremes, in the sense that some of the safest or unsafest countries may only have one data point. With only one observation, there may be much more that is not being captured by the summary, or the sample of data per country is too small to offer a really good overview

**YOUR NAME**

Aditya Yash Raj
