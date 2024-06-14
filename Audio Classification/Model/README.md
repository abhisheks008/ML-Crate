## **Audio Classification**

### 🎯 **Goal**

The aim of this project is develop a machine learning model to classify audio recordings into predefined categories and analyze the audio features and model performance.

### 🧵 **Dataset**

https://www.kaggle.com/datasets/khadijehvalipour/audio-classification

### 🧮 **What I had done!**

1. Data Cleaning and Preprocessing

- **Convert all audio files to .wav format**: Standardize the audio files by converting them to .wav format for consistent input to the machine learning models.
- **Split audio files into smaller segments**: Divide each of the 23 audio files into 100 smaller parts to increase the dataset size and enhance model training.
- **Extract features from audio files**: Use feature extraction techniques (e.g., MFCCs, chroma, mel spectrogram) to obtain meaningful attributes from the audio data for model input.

2. Feature Extraction

- **Extract MFCCs (Mel-Frequency Cepstral Coefficients)**: Extract MFCC features from the audio files to capture the essential characteristics of the audio signals.
- **Extract Chroma Features**: Capture the pitch class distribution of the audio using chroma features for a better understanding of harmonic content.
- **Normalize Extracted Features**: Scale the extracted features to a standard range to ensure uniformity and improve model performance.
- **Aggregate Features**: Combine and aggregate the extracted features into a comprehensive feature set for model training and evaluation.
- **Save Extracted Features**: Store the extracted features in a structured format (e.g., CSV, NumPy array) for easy access during model development.

3. Encoding and Preparing Data for Model

- **Convert Features and Labels to NumPy Arrays**: Transform the list of extracted features and labels into NumPy arrays for efficient processing and manipulation.
- **Encode Labels**: Utilize a LabelEncoder to convert categorical labels into a numerical format suitable for machine learning models.
- **Transform Labels**: Apply the label encoder to the labels array, creating a set of encoded labels.
- **Determine Number of Classes**: Calculate the number of unique classes in the dataset to define the output dimensions for the classification model.

4. Model Selection and Training

- **Split data into training and testing sets**: Divide the dataset into training (e.g., 80%) and testing (e.g., 20%) subsets to evaluate model performance.
- **Explore Various Models**: Evaluate nine different machine learning models to determine their suitability for the audio classification task.
- **Train Models**: Train each selected model on the preprocessed audio features and corresponding encoded labels.

5. Model Evaluation

- **Evaluate performance using metrics**: Assess models using percision, accuracy, recall and f1 score .
- **Compare model performance**: Analyze and compare the evaluation metrics to select the best-performing model.

6. Visualization

- **Visualize Actual vs. Predicted Labels**: Plot graphs showing the comparison between actual and predicted labels for audio classification. This visualization helps assess how well the model predicts the correct categories for audio samples.
- **Compare Model Metrics**: Utilize histograms to compare metrics such as accuracy, precision, recall, and F1 scores across different models used for audio classification. This comparative analysis aids in selecting the model that exhibits the highest overall performance in classifying audio samples into their respective categories.

### 🚀 **Models Implemented**

1. Random Forest
2. Decision Tree
3. Logistic Regression
4. XG Boost
5. Lasso
6. Ridge
7. SVM (Support Vector Machine)
8. MLP (Multi-Layer Perceptron)
9. Gradient Boosting

### 📚 **Libraries Needed**

1. librosa
2. pydub
3. numpy
4. pandas
5. scikit-learn

### 📊 **Exploratory Data Analysis Results**
<img src = "https://github.com/keshav1441/ML-Crate/blob/main/Audio%20Classification/Image/Accuracy.png"/>
<img src = "https://github.com/keshav1441/ML-Crate/blob/main/Audio%20Classification/Image/Performance%20Metrics.png"/>

### 📈 **Performance of the Models based on the Accuracy Scores**

`accuracy was used as the performance metric.

1. Random Forest: 99.130435%
2. Decision Tree: 92.173913%
3. Logistic Regression: 98.260870%
4. XG Boost: 97.826087%
5. Lasso: 18.260870%
6. Ridge: 96.956522%
7. SVM (Support Vector Machine): 99.565217%
8. MLP (Multi-Layer Perceptron): 99.347826%
9. Gradient Boosting: 94.782609%

### 📢 **Conclusion**

**Best Performing Model**: SVM (Support Vector Machine)

- SVM model achieves the highest accuracy of 99.57%, indicating the lowest overall errors among all models.
- It outperforms other models across all metrics, demonstrating superior predictive power and reliability.
- Second Best: Model 4 (XG Boost)

**Second Best**: MLP (Multi-Layer Perceptron)

- MLP has an accuracy of 99.35% and performs closely behind SVM.
- It shows slightly higher errors compared to SVM: MAE (610.22), MSE (610,762.19), RMSE (781.51), and MAPE (22.02).

**Summary**:

- SVM and MLP are the top performers with SVM slightly edging out MLP in accuracy and error metrics.
- Random Forest and Logistic Regression also demonstrate strong performance with accuracies above 98%.
- Decision Tree, Ridge, and Gradient Boosting exhibit higher errors across all metrics compared to the top models.
- Lasso performs the poorest among all models based on accuracy and error metrics.

### ✒️ **Your Signature**

`Keshav`
