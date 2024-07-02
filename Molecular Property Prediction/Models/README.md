## Molecular Property Prediction & EDA - Notebooks


### Scalar Coupling Constant Prediction 

The `Notebook.ipynb` notebook provides an in-depth exploration of molecular structures and feature extraction for predicting scalar coupling constants. 

1. **Data Preparation:**
   - The notebook begins with data preparation steps, including loading the provided datasets (`train_df`).
   - Random sampling is performed to extract a subset (`sample_df`) for feature extraction and model training.

2. **Feature Extraction:**
   - Feature extraction techniques are employed to derive relevant molecular features, including bond distances and neighboring atom types and distances.
   - The `standardizer` function is utilized to standardize molecular structures and extract these features efficiently.
   
      ![img1](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/e1f0b4dd-87c7-4b63-a942-8cc1e3acdf43)

3. **Feature Selection:**
   - Bond distances, neighboring atom types, and distances are extracted and concatenated into a feature matrix (`X`).
   - The target variable, scalar coupling constants, is extracted and stored separately (`y`).
   - Feature matrix `X` and target variable `y` are combined and saved as a CSV file (`bond_lengths.csv`) for further analysis and modeling.

4. **Analysis and Insights:**
   - The notebook offers insights into the distribution of unique atom counts in molecules through visualization techniques like histograms.
  
      ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/642ac187-61f4-4795-a2d7-b53ac6869d39)

   - Feature engineering and selection strategies are discussed to highlight important molecular characteristics influencing scalar coupling constants.

5. **Modeling and Prediction:**
   - The extracted features are utilized to train machine learning models for predicting scalar coupling constants.
   - Various regression algorithms, including Linear Regression, Random Forest Regressor, K Nearest Neighbors, Support Vector Regressor, and Decision Tree Regressor, are evaluated for their predictive performance.
   
      ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/a4685674-218a-4b06-9d2b-a4d4ec27b73c)

6. **Conclusion:**
   - The notebook concludes with observations and recommendations for further analysis, highlighting the importance of feature selection and model optimization in accurately predicting scalar coupling constants.
   
      ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/7cec01b1-c254-4b1d-8991-f47b871387a5)

### Mulliken Charge 

The `mulliken_charge.ipynb` notebook explores Mulliken charges obtained from Mulliken population analysis, offering insights into partial atomic charges estimation.

1. **Data Loading and Exploration:**
   - The notebook begins by loading the Mulliken charges dataset (`mulliken_charges.csv`) and the molecular structures dataset (`structures.csv`).
   - Initial exploration is conducted to understand the structure and dimensions of the datasets.

2. **Mulliken Charge Analysis:**
   - Specific molecules' Mulliken charges are examined to observe their distribution and variations.
   - Statistical summaries and visualizations, such as histograms, provide insights into the distribution of Mulliken charges across molecules.
      
      ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/7ad7edf9-326c-45cc-ab28-11ff50acc358)

3. **Integration with Molecular Structures:**
   - Mulliken charges are integrated with molecular structures data to analyze spatial relationships.
   - A 3D scatter plot visualizes spatial coordinates alongside Mulliken charges, offering a comprehensive view of atomic charges' spatial distribution.
      
      ![newplot](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/75d5aec6-f62d-49f8-a279-408fcaa3b789)

4. **Atom-wise Charge Analysis:**
   - The notebook explores Mulliken charges at the atom level, investigating how charges vary across different atom types.
   - A box plot visualizes Mulliken charges grouped by atom type, highlighting differences in charge distributions among atoms.
      
      ![newplot](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/6dcff582-5124-4e77-8679-897c5a7c081d)

5. **Conclusion and Insights:**
   - The notebook concludes with insights into the distribution and variation of Mulliken charges across molecules and atom types.
   - Recommendations for further analysis or modeling based on observed patterns are provided.

### Dipole Moments and Potential Energy

The `dipole_moments_and_potential_energy.ipynb` notebook explores dipole moments and potential energy in molecular systems.

1. **Dipole Moments Analysis:**
   - The notebook begins by loading and examining the dipole moments dataset (`dipole_moments.csv`).
   - Visualizations, including histograms and scatter plots, illustrate the distribution and relationships of dipole moments along X, Y, and Z coordinates.

      ![newplot](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/4ac0ab70-ac13-4f1b-bc6b-00d5fba2de5f)
   
   - A 3D scatter plot showcases dipole moments' magnitude, offering insights into their spatial distribution and variation.
   
      ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/5593b3a8-eed0-400e-8afe-d82952942343)

2. **Potential Energy Analysis:**
   - The potential energy dataset (`potential_energy.csv`) is loaded and analyzed through histograms to understand its distribution across molecules.

      ![newplot (29)](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/97f3d9ea-60dc-42c1-a65c-1f17deb81ed5)

   - Scatter plots visualize potential energy alongside dipole moments, providing insights into their potential relationship.

3. **Integration and Correlation Analysis:**
   - Dipole moments data is integrated with potential energy data, and correlation analysis is performed to identify relationships between variables.
   - Heatmaps and pair plots visualize correlations between dipole moments, potential energy, and their components.

      ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/c78812f0-aff0-4107-a3a7-2d63855c5895)

4. **Additional Insights:**
   - Box plots offer further insights into potential energy distributions across molecules.

      ![newplot (30)](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/b6aaa9dc-8839-4811-bcd6-cdcc26e7f0e7)

   - Various visualizations aid in understanding the interplay between dipole moments, potential energy, and molecular properties.


### ✒️ **Signature**

<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)

