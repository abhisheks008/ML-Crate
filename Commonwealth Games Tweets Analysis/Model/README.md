# Commonwealth Games 2022 Twitter Analysis

## Overview

This project aims to analyze Twitter data related to the Commonwealth Games 2022. The dataset includes tweets with various features such as sentiment, topic, and word frequency. The analysis involves the application of several machine learning and deep learning models to understand patterns and sentiments within the tweets.

## Key Insights

1. **Sentiment Analysis:**
   - Majority of tweets exhibit a positive sentiment.
   - Most common sentiment is positive, contributing to an overall positive tone.
   - ![Graph of sentiment](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta12.PNG)

2. **Word Frequency:**
   - "cwg2022" is the most frequently used word.
   - Word cloud and frequency distribution highlight prominent topics in tweets.
   - ![Frequency Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta10.PNG)

3. **Tweet Length:**
   - Majority of tweets fall within 150 to 190 words.
   - Users express detailed thoughts and opinions about Commonwealth Games 2022.
   - ![Distribution of Tweet Lengths](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta9.PNG)

## Models and Accuracies

| Model                 | Accuracy |
|-----------------------|----------|
| Logistic Regression   | 93%      |
| Decision Tree         | 90%      |
| Gradient Boosting     | 89%      |
| SVM                   | 86%      |
| Deep Learning Models  | 41.76%   |

## Models Overview

1. **Logistic Regression:**
   - Achieved the highest accuracy of 93%.
   - Demonstrates strong performance in classifying tweet sentiments.

2. **Decision Tree:**
   - Achieved an accuracy of 90%.
   - Captures complex relationships within the dataset.

3. **Gradient Boosting:**
   - Achieved an accuracy of 89%.
   - Provides effective ensemble learning for improved predictions.

4. **SVM:**
   - Achieved an accuracy of 86%.
   - Utilizes support vector machines for accurate classification.
  
-![Joint Accuracy Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta3.png)

5. **Deep Learning Models(ANN,CNN,DNN,RNN,LSTM):**
   - Achieved an accuracy of 41.76%.
   - Indicates challenges in capturing complex patterns in the dataset.
   - ![CNN Accuracy Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta5.png)
   - ![ANN Accuracy Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta6.png)
   - ![RNN Accuracy Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta7.png)
   - ![DNN Accuracy Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta8.png)
   - ![LSTM Accuracy Graph](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta4.png)


## Word Cloud

![Word Cloud of Most Common Words](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta11.PNG)

## Topic Analysis

![Distribution of Topics in Tweets](https://github.com/adi271001/ML-Crate/blob/Commonwealth-Games-Tweets-Analysis/Commonwealth%20Games%20Tweets%20Analysis/Images/cgta13.PNG)

## Conclusions

- Logistic Regression emerges as the most accurate model for sentiment analysis.
- Decision Tree and Gradient Boosting models provide robust performances.
- Deep learning models show potential areas for improvement.

## Usage
1. Install dependencies:
   pip install -r requirements.txt
2. Run the analysis scripts.

3. View the generated visualizations in the plots directory.

## Acknowledgement 

I would Love to thank Kaggle for providing the dataset and maintainer for assigning me this project and KOSS for participating in KWOC 2023
