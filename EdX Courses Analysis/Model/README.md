## **EdX Courses Analysis** ##

## **Goal:** ##

To cleanse and analyse the course data to understand and draw insights from the given dataset.

## **Dataset:** ##

https://www.kaggle.com/datasets/khusheekapoor/edx-courses-dataset-2021

## **Description:** ##
With the world becoming digital, any new skill can be acquired with just a click. However, many of us still needs a dedicated curriculum in order to excel in a specific topic. This is where e-learning platforms comes handy and EdX is one of such massive open online course (MOOC) providers. This dataset is scraped off the publicly available information on the EdX website. This dataset consists of 720 rows and 6 columns namely Name of the Course, Name of the University, Difficulty Level, Course URL, short summary about the course and course description.

## **What I Had Done:** ##
* Reading the data in python
* Basic Exploration of data
* Cleaning the data and transforming it to be useful for basic analysis 
* Visual Data exploration

## **Libraries Needed:** ##
* pandas - To manipulate dataframes
* seaborn - To visualise data
* matplotlib - To visualise data
* nltk - Natural Language Toolkit
* wordcloud - To generate wordclouds
* re - The regular expression module

## **Visualisations:** ##
![Level_of_Courses](https://user-images.githubusercontent.com/73251652/179422356-2517d727-e8f7-4a8c-920e-b425dfc63e67.png)

![Top_Universities](https://user-images.githubusercontent.com/73251652/179422461-e1eea6a1-c13d-4a0c-a6f3-702fb695d3bc.png)

![WordCLoud_for_AboutColumn](https://user-images.githubusercontent.com/73251652/179422474-860e9911-7dc2-4e36-8f29-55d7e24f92fc.png)

![wordCloud_for_CourseDescription](https://user-images.githubusercontent.com/73251652/179422480-8b36e3c5-145e-4a50-8318-2e30a5b6735a.png)

![wordCloud_for_Names_of_Courses](https://user-images.githubusercontent.com/73251652/179422486-aecde706-37fd-45e7-8a05-fefeaf4f230a.png)


## **Conclusions:** ##
*	The most commonly occurring three words together are “data analysis statistic” . This implies that data analysis is closely related to statistics and also, these words are majorly mentioned by most of course descriptions indicating that these two are taught together.
* “Computer Science” is being the top most bi-gram with 150+ occurrences. This shows that CS is still the major topic among the courses offered by Universities and Organisations.
*	Almost 61% of the courses are beginner friendly. This indicates that the users even without any pre-requisites are good to take up the courses.
*	28% of the courses are of Intermediate Level and might require certain amount of background knowledge before enrolling in the courses.
*	Harvard University is the top most university to offer a greater number of courses. In other words, almost 85+ courses are offered by this prestigious University.
*	Successively, MIT (Massachusetts Institute of Technology) stood in the second position for being offering more than 40 courses.
*	The about section of the dataset majorly speaks about “learn, course and skill”. This states that it talks about learning a new course or upskilling in a particular field.
* The course description part of the dataset is slightly similar to the about section of the dataset. Both are certainly talking about learning and courses.
*	Majority of the Names of the Courses evidently have the term “Introduction”.
*	This presence of the term “Introduction” justifies for having 61% beginner friendly courses as most of the courses might be an introduction to a certain technology or domain.

## **Contributed By:** ##
Lahari Boni 
Github - https://github.com/LahariBoni
