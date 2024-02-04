# PubMed Multi-label Text Classification Project Overview

## Overview

This project focuses on multi-label text classification of biomedical research articles sourced from the PubMed repository. The dataset consists of approximately 50,000 documents, each manually annotated with MeSH (Medical Subject Headings) labels by Biomedical Experts. The primary challenge addressed in this project is the extensive output space and severe label sparsity issues in the original dataset.

## Key Features

- **Dataset:** 50,000 research articles from PubMed, annotated with MeSH labels.
- **Label Reduction:** Original MeSH labels reduced to major categories.
- **Root Mapping:** Major labels mapped to corresponding root categories for a simplified output space.
- **Models:** Utilized BioBERT, RoBERTa, and XLNet for multi-label text classification.
- **Results:** BioBERT demonstrated the highest accuracy at 87%, outperforming RoBERTa and XLNet.

## Dataset Processing

The dataset underwent preprocessing to address label sparsity and reduce the output space. Major MeSH labels were retained, and a hierarchical structure was introduced through root mapping for better interpretability.

## Model Training

- Three state-of-the-art pre-trained language models were employed: BioBERT, RoBERTa, and XLNet.
- Training involved optimization for multi-label classification with a focus on improving F1 and flat validation accuracies.
- Graphs depicting training loss, F1 validation accuracy, and flat validation accuracy over epochs are available in the `results` directory.
- the training runs charts can be seen in weughts and Biases Dashboard:  https://wandb.ai/ai-guru/Multi%20Label%20Classification%20of%20PubMed%20Articles%20%28Paper%20Night%20Presentation%29

## Conclusion

BioBERT emerged as the most effective model, achieving an accuracy of 87%. The dataset analysis revealed Class B as the category with the highest number of articles. Training graphs illustrate the models' learning processes and performance improvements over epochs.



