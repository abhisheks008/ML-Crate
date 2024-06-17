# Body Fat Prediction Web Interface

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
    git clone https://github.com/yourusername/body-fat-prediction.git
    cd BODY\ FAT\ PREDICTION
    ```

2. **Install Dependencies**

    It is recommended to use a virtual environment to manage dependencies. You can create and activate a virtual environment as follows:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

    Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask Application**

    Start the Flask development server:

    ```bash
    flask run
    ```

    By default, the application will be accessible at `http://127.0.0.1:5000/`.

### Using the Web Interface

1. Open your web browser and navigate to `http://127.0.0.1:5000/`.

2. You will see a form where you can input the necessary parameters for Body Fat prediction.

3. Fill out the form with the required details and click on the "Predict" button.

4. The application will process the input data using the pre-trained model and display the predicted body fat percentage.

## Directory Structure

```
BODY FAT PREDICTION/
├── Web App/
    ├── app.py                          # Main Flask application
    ├── templates/
        ├── index.html                   # HTML template for the web interface
    ├── static/
        ├── css/
            ├── styles.css              # CSS for styling the web interface
├── Model/
    ├── Body_Fat_Prediction.ipynb       # ML model for predicting Body fat
    ├── README.md                       # Model Documentation
├── Images/
    ├── README.md                       # Has links for images of plots (Data visualization)
├── Dataset/
    ├── bodyfat.csv                     # Body fat dataset - CSV file
    ├── README.md                       # Has Kaggle link for the Dataset
├── model.pkl                           # Pickle dumped model
├── requirements.txt                # Requirements to run the application
├── README.md                           # Project documentation
```

## Additional Notes

- **Model File**: The model file `body_fat_model.pkl` is stored in the `model/` directory. Ensure this file is present when running the application.
- **Error Handling**: Basic error handling has been implemented to guide users if they input invalid data.
- **Future Improvements**: Potential enhancements include adding user authentication, improving the UI/UX, and deploying the application to a cloud platform for broader access.

## Acknowledgments

- Thanks to the contributors of the original Body Fat prediction model.
- Special mention to the open-source community for providing the tools and libraries that made this project possible.

CONTRIBUTED BY

Tandrima Singha, K S Prateek

For any issues or contributions, please refer to the project's GitHub repository [here](https://github.com/yourusername/body-fat-prediction).

---
```