# PubMed Multi-label Text Classification

This repository contains code and models for multi-label text classification on the PubMed dataset using BioBERT, RoBERTa, and XLNet.

## Table of Contents

- [Dataset](#dataset)
  - [Dataset Analysis](#dataset-analysis)
- [Models and Accuracies](#models-and-accuracies)
- [Training Graphs](#training-graphs)
  - [Training Loss vs Number of Epochs](#training-loss-vs-number-of-epochs)
  - [F1 Validation Accuracy vs Number of Epochs](#f1-validation-accuracy-vs-number-of-epochs)
  - [Flat Validation Accuracy vs Number of Epochs](#flat-validation-accuracy-vs-number-of-epochs)
- [Conclusion](#conclusion)
- [Results](#results)
- [Acknowledgments](#acknowledgments)


## Dataset

The dataset used in this project is available on Kaggle: [PubMed Multi-label Text Classification](https://www.kaggle.com/datasets/owaiskhan9654/pubmed-multilabel-text-classification)

### Dataset Analysis

Class B has the highest number of articles, as shown in the bar chart below:

![Class Distribution](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt1.PNG)

## Models and Accuracies

- **BioBERT:** Achieved an accuracy of 87%
- **RoBERTa:** Achieved an accuracy of 84%
- **XLNet:** Achieved an accuracy of 85.5%

BioBERT outperformed the other models, demonstrating its effectiveness in handling biomedical text data.

## Training Graphs of ROBERTA

### Training Loss vs Number of Epochs

![Training Loss](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt2.PNG)

### F1 Validation Accuracy vs Number of Epochs

![F1 Validation Accuracy](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt3.PNG)

### Flat Validation Accuracy vs Number of Epochs

![Flat Validation Accuracy](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt4.PNG)


## Training Graphs of BIO-BERT

### Training Loss vs Number of Epochs

![Training Loss](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt5.PNG)

### F1 Validation Accuracy vs Number of Epochs

![F1 Validation Accuracy](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt6.PNG)

### Flat Validation Accuracy vs Number of Epochs

![Flat Validation Accuracy](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt7.PNG)


## Training Graphs of XL-NET

### Training Loss vs Number of Epochs

![Training Loss](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt8.PNG)

### F1 Validation Accuracy vs Number of Epochs

![F1 Validation Accuracy](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt9.PNG)

### Flat Validation Accuracy vs Number of Epochs

![Flat Validation Accuracy](https://github.com/adi271001/ML-Crate/blob/PubMed-Text/PubMed%20Text%20Classification/Images/pmt10.PNG)

## Result
The trained models, evaluation results, classification reports and additional details can be found in the results directory.

## Conclusion

In conclusion, this project successfully tackled the PubMed multi-label text classification problem using BioBERT, RoBERTa, and XLNet. BioBERT emerged as the most effective model, achieving the highest accuracy. The dataset analysis revealed Class B as the category with the highest number of articles.

The training graphs provide insights into the model's learning process, illustrating the reduction in training loss and the improvement in F1 and flat validation accuracies over epochs.

## Acknowledgement

Thanks to Kaggle for Providing the Dataset , Maintainers and IWOC for this beautiful opportunity
