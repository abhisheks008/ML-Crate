# Body Fat Prediction

This repository hosts a Body Fat prediction model, which now includes a Flask-based web interface for user interaction. This document details how to run the app and explains the contributions made to enhance the project with a user-driven web interface.

## Contributions

### Added Features:
1. **Flask Web Application**: Developed a Flask web application to enable user interaction with the Body Fat prediction model.
2. **Model Integration**: Integrated the existing Body Fat prediction model with the Flask application using `pickle`.
3. **User Interface**: Designed a simple and intuitive user interface for inputting data and displaying predictions.
4. **Instructions for Running the App**: Provided comprehensive instructions for setting up and running the web application.

## How to Run the Application

### Prerequisites

- Python 3.8 or higher
- Anaconda
- Jupyter notebook
- Flask
- Pickle
- Necessary libraries (listed in `requirements.txt`)

### Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/abhisheks008/ML-Crate.git
    cd Body\ Fat\ Prediction
    ```

2. **Install Dependencies**

    - Install Anaconda (https://docs.anaconda.com/free/anaconda/install/)
    <br>
    Use the following command to confirm the installation of Anaconda
    ```
        conda --version 
    ```

    - It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment as follows:

    ```bash
    conda create --name myEnv
    source activate myEnv
    ```

    Install the required packages:

    ```bash
    conda update
    conda install --yes --file requirements. txt
    ```

 - Install and make sure Jupyter notebook server is running at `http://localhost:8888`
    ```
        conda install jupyter
        jupyter notebook
    ```

3. **Run the Flask Application**

    Start the Flask development server:

    ```bash
    python3 Web\ App/app.py
    ```

    By default, the application will be accessible at `http://127.0.0.1:5000/`.

### Using the Web Interface

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
<img src="Images/Web App/Initial.png" alt="Initial State" width="600" />

2. You will see a form where you can input the necessary parameters for Body Fat prediction.
<img src="Images/Web App/FormFilled.png" alt="Filling the form" width="600" />


3. Fill out the form with the required details and click on the "Predict" button.
<img src="Images/Web App/Predicted.png" alt="Prediction output" width="600" />


4. The application will process the input data using the pre-trained model and display the predicted body fat percentage.



## Directory Structure

```
Body Fat Prediction/
├── model.pkl                           # Pickle dumped model
├── requirements.txt                   # Requirements to run the application
├── README.md                           # Project documentation
├── Web App/
    ├── app.py                          # Main Flask application
    ├── README.md
    ├── templates/
        ├── index.html                   # HTML template for the web interface
    ├── static/
        ├── css/
            ├── styles.css              # CSS for styling the web interface
├── Model/
    ├── Body_Fat_Prediction.ipynb       # ML model for predicting Body fat
    ├── README.md                       # Model Documentation
├── Images/
    ├── README.md                       # Has links for images of plots (Data visualization) and Web App's working
    ├── Web App/                        # Has images of Web App's working
├── Dataset/
    ├── bodyfat.csv                     # Body fat dataset - CSV file
    ├── README.md                       # Has Kaggle link for the Dataset
```

## Additional Notes

- **Model File**: The model file `model.pkl` is stored in the project's root directory. Ensure this file is present when running the application.
- **Future Improvements**: Potential enhancements include adding user authentication, improving the UI/UX, and deploying the application to a cloud platform for broader access.

## Acknowledgments

- Thanks to the contributors of the original Body Fat prediction model.
- Special mention to the open-source community for providing the tools and libraries that made this project possible.

CONTRIBUTED BY

[Tandrima Singha](https://github.com/tandrimasingha) (Training the model)<br> [K S Prateek](https://github.com/imksprateek) (Web interface and Documentation)

For any issues or contributions, please refer to the project's GitHub repository [here](https://github.com/abhisheks008/ML-Crate/tree/main/Body%20Fat%20Prediction).

---
