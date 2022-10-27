GOAL

Implemention of different models like RNN, RNN + LSTM, BiLSTM to see which gives better accuracy.

DATASET 

The dataset can be found at the below given link.
https://drive.google.com/file/d/1GeUzNVqiixXHnTl8oNiQ2W3CynX_lsu2/view

The above text file contains text in the form of short stories from the novel - Adventures of Sherlock Holmes by Arthur Conan Doyle

DESCRIPTION

The main aim of the project is to predict the next word based on the input of three continuous sequential words based on a text file which contains text from the Sherlock Holmes short stories.

WHAT I HAVE DONE 
Imported the dataset which was a text file of which I only wanted the 12 short stories and the rest was filtered out. Also various text pre-processing techniques were employed to clean out the special characters,special UTF-8 characters and links. The final training data was splitted into traning and validation sets. After, to convert the long string of text into tokens and then vectorize them, tokenizer() from tensorflow was used along with Bag-of-Words tokenization technique. After which I created 2 models based on LSTM and Bidirectional LSTM and fine-tuned distil-BERT with the help of happytransformer library on google colab. The models were trained and the results visualized.

LIBRARIES NEEDED
1. Tensorflow
2. Keras
3. Happytransformer
3. Pandas
4. Numpy
5. Matplotlib
6. pickle

VISUALIZATIONS
![alt bwhahaha](https://github.com/skartikc/ML-Crate/blob/59986c4b8ca312faabe9fdc11c5b3ca597ad712a/Next%20Word%20Prediction/Images/Model0-Graphs.png)
![alt bwhahah2] (https://github.com/skartikc/ML-Crate/blob/59986c4b8ca312faabe9fdc11c5b3ca597ad712a/Next%20Word%20Prediction/Images/Model1-Graphs.png)


PREDICTION/OUTPUT 
1. Model 0 - LSTM
2. Model 1 - BiLSTM
3. Model 2 - LSTM

MODEL PERFORMANCE 
| Sr. No.       | Model         | Accuracy/Loss(training) |
|    :---:      |     :---:     |    :---:                |
| 1             | RNN + LSTM    |         83.24 - A       |
| 2             | RNN + BiLSTM  |         83.89 - A       |
| 3             | distil-BERT   |         2.4949 - L      |

CONCLUSION
I was successfully able to develop solution to predicting the next word of a novel by using 3 different models, comparing their accuracies.