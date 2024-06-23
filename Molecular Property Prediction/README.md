## Molecular Property Prediction & EDA

### 🎯 **Goal**

The goal of this project is to develop predictive models for estimating scalar coupling constants between atom pairs in molecules based on their structural features. Additionally, the project aims to conduct exploratory data analysis (EDA) to gain insights into the relationships between molecular properties and their structural characteristics, facilitating a deeper understanding of molecular behavior and interactions.

### 🧵 **Dataset**

The dataset for this project is sourced from the "Predicting Molecular Properties" competition hosted on Kaggle, titled [CHAMPS Scalar Coupling](https://www.kaggle.com/competitions/champs-scalar-coupling/data) 

### 🧾 **Description**


Molecular properties play a crucial role in understanding chemical interactions and reactions, with applications spanning drug discovery, materials science, and environmental research. Predicting these properties accurately is essential for advancing various scientific domains. This project aims to develop predictive models for estimating scalar coupling constants between atom pairs in molecules and conducting exploratory data analysis (EDA) to gain insights into molecular behavior and interactions.

The ultimate goal is to accurately predict the scalar coupling constant for the atom pairs listed in the test dataset.


### 📜 **Repo Structure**

```bash
Molecular Property Prediction & EDA

|- Dataset
    |- README.md
|- Images
    |- img1.png
    |- img2.png
        :
        :
    |- img11.png
    |- README.md
|- Models
    |- Notebook.ipynb
    |- mulliken_charge.ipynb
    |- dipole_moments_and_potential_energy.ipynb
    |- model.h5
    |- README.md
|- requirements.txt
|- README.md

```

### 🧮 **What I had done!**

- Data Preparation and Cleaning:
    - Loading Data: Importing datasets such as `train.csv`,`structures.csv`, `mulliken_charges.csv`, and `dipole_moments.csv`.

    - Merging Data: Combining different datasets for a comprehensive analysis.

    - Data Cleaning: Handling missing values, filtering data, and ensuring data consistency.

- Exploratory Data Analysis (EDA)

  **Interactive 3D Visualization of Molecular Structures: Atoms are color-coded (H-🟣, C-⚫, O-🔴, N-🔵, F-🟢)**

  <img src="https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/055d77c0-cc81-4508-93b6-402a3f4e40dc" />
   
  ----

  **Distribution of Unique Atom Counts in Molecules**

  <img src="https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/642ac187-61f4-4795-a2d7-b53ac6869d39"/>

  ----

  **Scatter Plot of Bond Distance vs. 1st Neighbor Distance**

  <img src=" https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/b44baa28-e7ac-43c4-a0f2-b4cf35301262"/>  

  ----

    - Scalar Coupling Constants: 

        Analyzing the distribution and characteristics of scalar coupling constants.

        ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/bd828496-21e1-4545-9319-9c85d6e3531a)

        Visualizing the scalar coupling constants through histograms and scatter plots.

    - Mulliken Charges:

        Exploring the distribution of Mulliken charges.

        ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/7ad7edf9-326c-45cc-ab28-11ff50acc358)

        Visualizing Mulliken charges using boxplots, histograms and 3D scatter plots.

        ![newplot](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/6dcff582-5124-4e77-8679-897c5a7c081d)

    - Dipole Moments:

        Analyzing the distribution of dipole moments along different coordinates.

        ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/ed18cdc6-f4ec-4cf9-8bf6-e3cc98641a18)
        
        Visualizing the dipole moments through 2D scatter plots and 3D scatter plots.

        ![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/5593b3a8-eed0-400e-8afe-d82952942343)

    - Potential Energy:

        Exploring the distribution of potential energy values.

        ![newplot](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/77e949a3-c95e-47e7-abc2-c15317d2260f)

        Visualizing the potential energy through histograms and scatter plots.

- Feature Engineering
    - Generating Features: Creating new features based on atomic interactions and spatial coordinates.

    - Standardization: Standardizing molecular data to ensure consistency across different molecules.

- Model Building and Evaluation
    - Feature Selection: Selecting relevant features for model training.

    - Model Training: Training different regression models to predict scalar coupling constants.
        Linear Regression
        Random Forest Regressor
        K Nearest Neighbors
        Support Vector Regressor
        Decision Tree Regressor

- Model Evaluation: Evaluating models using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² score.

![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/a4685674-218a-4b06-9d2b-a4d4ec27b73c)

----

![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/469d5d8b-e310-448d-9530-b8584c0b87cf)

----

![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/b05146d6-852e-4bdd-9712-2c2c52239ff7)

----

![image](https://github.com/Sgvkamalakar/Sgvkamalakar/assets/103712713/7cec01b1-c254-4b1d-8991-f47b871387a5)

----

### 🚀 **Models Implemented**

- Linear Regressor
- Random Forest Regressor
- K Nearest Neighbors
- Support Vector Regressor
- Decision Tree Regressor
- Simple Feed Forward Neural Network

### 📚 **Libraries**

<img src="https://numpy.org/doc/stable/_static/numpylogo.svg" width="80" height="60"><img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" width="80" height="60"><img src="https://images.prismic.io/plotly-marketing-website-2/798854a2-209b-4e03-959f-965613354c4f_favicon_new_white.png" width="60" height="60"><img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="80" height="60"><img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" width="80" height="60"><img src="https://matplotlib.org/_static/logo_dark.svg" width="80" height="60"><img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="60" height="60"/>

### ⚙️ **Usage**


1. Install Dependencies: Ensure you have all the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    
    ```
2. Open the Notebooks: You can open the notebooks in Jupyter Notebook or JupyterLab. Navigate to the Models folder and open the desired notebook.

3. Run the Cells: Execute the cells sequentially to reproduce the analyses and results. Each notebook is designed to be self-contained, with explanations and comments for each code snippet.

4. Explore the Visualizations: Use the visualizations in the Images folder to gain insights into the molecular data. The images are referenced within the notebooks to provide context.


    
### 📈 **Performance of the Models based on the Accuracy Scores**



<div align="center">
<table>
  <tr>
    <th>Model Name</th>
    <th>MAE</th>
    <th>MSE</th>
    <th>R2</th>
  </tr>
  <tr>
    <td>Linear Regressor</td>
    <td>8.6099</td>
    <td>176.955</td>
    <td>0.8536</td>
  </tr>
  <tr>
    <td>Random Forest Regressor</td>
    <td>1.6670</td>
    <td>8.0106</td>
    <td>0.9934</td>
  </tr>
  <tr>
    <td>K Nearest Neighbors</td>
    <td>2.1068</td>
    <td>17.1477</td>
    <td>0.9858</td>
  </tr>
  <tr>
    <td>Support Vector Regressor</td>
    <td>8.0809</td>
    <td>193.659</td>
    <td>0.8398</td>
  </tr>
  <tr>
    <td>Decision Tree Regressor</td>
    <td>2.1842</td>
    <td>15.0023</td>
    <td>0.9876</td>
  </tr>
  <tr>
    <td>Feed Forward NN</td>
    <td>----</td>
    <td>31.2838</td>
    <td>----</td>
  </tr>
</table>


</div>


### ✒️ **Signature**

<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)
