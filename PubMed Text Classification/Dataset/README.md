# PubMed Multi-label Text Classification Dataset

This dataset consists of approximately 50,000 research articles sourced from the PubMed repository. The documents in this collection have been manually annotated by Biomedical Experts with their MeSH (Medical Subject Headings) labels. Each article is described in terms of 10-15 MeSH labels.

## Dataset Details

- **Original Annotation:** Biomedical Experts manually annotated the documents with MeSH labels.
- **Label Space:** The original dataset had a large number of MeSH labels, resulting in an extensive output space and severe label sparsity issues.
- **MeSH Major Labels:** Each article is annotated with MeSH major labels, reducing the label space and addressing label sparsity.
  
## Data Processing and Label Mapping

To overcome the challenges of an extremely large output space and severe label sparsity, the dataset has undergone processing and mapping to its root labels. The following steps were taken:

1. **Label Reduction:** The original MeSH labels were reduced to their major categories.
2. **Root Mapping:** The major labels were mapped to their corresponding root categories to simplify the output space.

## Label Hierarchy

The MeSH major labels in the dataset have been organized in a hierarchical structure, allowing for a more structured and interpretable representation of the biomedical concepts.

## Data Statistics

- **Number of Articles:** 50,000
- **MeSH Labels:** Originally 10-15 per article, reduced to major labels.
- **Root Labels:** Reduced and mapped categories for more manageable classification.

## Citation

If you use this dataset in your research or publication, please cite the original dataset source and any relevant papers provided by the dataset creators.

## Acknowledgments

I extend my gratitude to the Kaggle and Biomedical Experts who manually annotated the documents and contributed this dataset to Kaggle.


