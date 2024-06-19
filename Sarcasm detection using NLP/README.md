# Sarcasm Detection Using NLP

This repository contains various deep learning models for detecting sarcasm in text data using TensorFlow and Keras. Each model explores different architectures and techniques to improve sarcasm detection performance.

## Dataset

The models are designed to work with any text classification dataset. Ensure your dataset is preprocessed and tokenized before feeding it into the models.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/text-classification-models.git
   cd text-classification-models


## Models

1. **Model 1: Global Average Pooling**
   - Embedding layer followed by a GlobalAveragePooling1D layer and Dense layers.
   - Simple and efficient for basic text classification tasks.

2. **Model 2: Stacked Bidirectional LSTM**
   - Two Bidirectional LSTM layers stacked together.
   - Suitable for capturing long-term dependencies in the text data.

3. **Model 3: Single Bidirectional LSTM**
   - A single Bidirectional LSTM layer with Dense layers.
   - Effective for capturing sequential information with lower complexity.

4. **Model 4: Conv1D + Bidirectional LSTM**
   - Convolutional layers followed by a Bidirectional LSTM.
   - Combines local feature extraction with sequence modeling.

5. **Model 5: CNN-LSTM Hybrid with Batch Normalization**
   - Combines Conv1D and Bidirectional LSTM layers with Batch Normalization.
   - Enhances feature extraction and improves convergence.

6. **Model 6: GRU-Based Model with Dropout**
   - Uses GRU layers with Dropout for regularization.
   - Potentially faster training with regularization to prevent overfitting.

7. **Model 7: Attention Mechanism**
   - Incorporates an attention layer after Bidirectional LSTM.
   - Helps the model focus on important parts of the input sequence.


## Conclusion

Experiment with different models and architectures provided in this repository to find the best performing model for your text classification task. Each model offers unique strengths, and their performance may vary depending on your specific dataset and task requirements.