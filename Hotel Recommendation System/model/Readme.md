Hotel Recommedation System

GOAL

Implementtion of hotel recomendation system based on user query and requirement.

DATASET

https://www.kaggle.com/datasets/keshavramaiah/hotel-recommendation

DESCRIPTION

The main of this project is to impement a model to recomend project based on user query.

WORK DONE

Analyzed the data and found insights such as correlation, missing values and plotted different plots and compared them.

![correlation_matrix_cost](https://user-images.githubusercontent.com/78209696/194793348-dbac3ad5-ac5c-47ba-8baf-1c3bb2a93ed9.png)
Correlation matrix of cost estimation

![correlation_matrix1](https://user-images.githubusercontent.com/78209696/194793441-492011f1-6cc4-4d48-b78d-67bbddc8387c.png)
Correlation matrix of hotel rooms details.

![star_rating_displot](https://user-images.githubusercontent.com/78209696/194793491-e50eccc5-a99c-414a-9e10-9f623121f3c0.png)
Displot to analyze star ratings.


Approach Taken(Algorithm)


We have gone with Case Based Reasoning (CBR) approach to analyse the data. Case-based reasoning (CBR), broadly construed, is the process of solving new problems based on the solutions of similar past problems.
An auto mechanic who fixes an engine by recalling another car that exhibited similar symptoms is using case-based reasoning.
A lawyer who advocates a particular outcome in a trial based on legal precedents or a judge who creates case law is using case-based reasoning. 
So, too, an engineer copying working elements of nature (practicing biomimicry), is treating nature as a database of solutions to problems. 
Case-based reasoning is a prominent type of analogy solution making.
It has been argued that case-based reasoning is not only a powerful method for computer reasoning, but also a pervasive behavior in everyday human problem solving; or, more radically, that all reasoning is based on past cases personally experienced. This view is related to prototype theory, which is most deeply explored in cognitive science.
LIBRARIES NEEDED

Numpy
Pandas
Matplotlib
scikit-learn
xgboost
seaborn
missingno
chart_studio
cufflinks
PLOTS





CONCLUSION

We investigated the data, checking for data unbalancing, visualizing the features, and understanding the relationship between different features. We made a system to recomend hotel based on user needs and using simmalrity index.
Hotel recomendation is also useful for stakeholders and hotel managers to understand the system of online booking system.
