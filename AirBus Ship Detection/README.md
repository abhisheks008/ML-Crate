# AirBus Ship Detection

Explore the detection and segmentation of ships in satellite images using advanced machine learning techniques. This project leverages models such as UNet, basic CNN, and ResNet for accurate ship detection and segmentation.
![Screenshot (150)](https://github.com/tanuj437/ML-Crate/assets/128210429/404ca0e4-b087-480c-8b58-4d8983c100c8)

## 📝 Description
This repository contains the code, pre-trained models, and scripts for detecting and segmenting ships in satellite images using deep learning models. The project aims to improve maritime monitoring and analysis by providing accurate ship detection capabilities.

## 📂 Contents
### Main Directory
- **app.py:** Streamlit application script for ship detection.
- **requirements.txt:** List of required libraries and dependencies.
- **README.md:** This document.

### Notebooks
- **AirBus.ipynb:** Jupyter Notebook containing the complete process of data preprocessing, model training, evaluation, and visualization.


### Images
- **CNN_model_output.png:** Training loss and validation accuracy plot for the CNN model.
- **unet_model_output.png:** Training loss and validation accuracy plot for the UNet model.
- **RNS_output.png:** Training loss and validation accuracy plot for the ResNet Segmentation model.

## 🎯 Goal
The goal of this AirBus Ship detection project is to accurately identify and segment ships from satellite images using various machine learning models. By automatically detecting these ships, the project aims to aid maritime monitoring and analysis, providing valuable insights for various applications.

## 🧠 Methodology
**1. Importing Libraries**
- Libraries such as NumPy, Pandas, Sklearn, PyTorch, Torchvision, and others are imported for data manipulation, visualization, and model building.

**2. Loading the Dataset**
- The dataset consists of satellite images with annotations for ship locations, which are preprocessed for model training.

**3. Data Preprocessing**
- Data preprocessing involves tasks such as resizing images to 256x256 pixels, normalizing pixel values, and augmenting data to enhance model performance and robustness.

**4. Training the Models**
- Multiple models are trained, including UNet, basic CNN, and ResNet segmentation models, to detect and segment ships in satellite images.

**5. Model Performance Analysis**
- Performance metrics such as accuracy, precision, and recall are computed to evaluate and compare the effectiveness of each model.

**6. Model Prediction**
- The trained models are used to predict ship locations in unseen images, showcasing their segmentation capabilities.

**7. Deployment**
- Streamlit is utilized to deploy a web application for real-time ship detection, enabling users to upload images and receive instant segmentation results.

## 🚀 How to Run the App
1. **Install the required libraries:**
    ```sh
    pip install -r requirement.txt
    ```

2. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

3. **Open the provided local URL in your web browser to access the app.**

## 📈 Visualizations
The `Images` folder contains visualizations showing the training loss and validation accuracy for the CNN and UNet models over multiple epochs. These visualizations help in understanding the model performance during the training process.

### CNN Model Output
<img width="588" alt="CNN_model_output" src="https://github.com/tanuj437/ML-Crate/assets/128210429/6d148519-a2f0-4833-8486-6214faf3b3c0">

- **Training Loss:** The left plot shows the training loss decreasing over epochs.
- **Validation Accuracy:** The right plot shows the validation accuracy improving over epochs.

### UNet Model Output
<img width="598" alt="unet_model_output" src="https://github.com/tanuj437/ML-Crate/assets/128210429/414aad57-71b9-49fc-96ac-76cf41de7a7f">

- **Training Loss:** The left plot shows the training loss decreasing over epochs.
- **Validation Accuracy:** The right plot shows the validation accuracy improving over epochs.
  
### ResNet Segmentation Model Output
<img width="584" alt="resnetsegmention_model_output" src="https://github.com/tanuj437/ML-Crate/assets/128210429/7ed26e3d-bc79-482f-8776-1acf06ae2e29">

- **Training Loss:** The left plot shows the training loss decreasing over epochs.
- **Validation Accuracy:** The right plot shows the validation accuracy improving over epochs.
  
## 📢 Conclusion
The AirBus Ship detection project demonstrates that various machine learning models can accurately detect and segment ships in satellite images. These models help automate maritime monitoring, providing valuable assistance to researchers and maritime authorities.

## ✒️ Connect with Me
Tanuj Saxena [LinkedIn](https://www.linkedin.com/in/tanuj-saxena-970271252/)
