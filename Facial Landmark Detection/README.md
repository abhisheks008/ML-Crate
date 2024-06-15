# Facial Landmark Detection

## Project Overview
Facial Landmark Detection is a sophisticated application that utilizes cutting-edge computer vision technologies to detect and visualize facial landmarks in real-time. Built using the Streamlit framework, this application employs the MediaPipe library, renowned for its robust facial recognition capabilities. This project aims to provide an interactive interface where users can see the detected facial landmarks overlaid on their face using a live video feed from their webcam.

## Features
- **Real-time Detection**: Utilizes the webcam to detect facial landmarks in real-time, providing immediate visual feedback.
- **High Accuracy**: Leverages MediaPipe's FaceMesh model, which is known for its high accuracy in detecting multiple facial landmarks.
- **User-Friendly Interface**: Built with Streamlit, the application offers a clean and navigable interface that is easy for users to operate.

## Screenshots
![image](https://github.com/Anshg07/ML-Crate/assets/96684989/3706a046-2f71-47e3-b7cb-caed404b5906)
![image](https://github.com/Anshg07/ML-Crate/assets/96684989/46c409d6-bcd9-4d17-8924-6cd79e8a782d)
![image](https://github.com/Anshg07/ML-Crate/assets/96684989/b9036098-274d-431b-b40f-ca02278a6b76)
![image](https://github.com/Anshg07/ML-Crate/assets/96684989/e954ce1c-d8b3-4b74-be11-3fff37e95420)

## Installation
Before running this application, ensure you have Python installed on your computer. Follow these steps to set up the environment:

1. **Clone the Repository**: First, clone this repository to your local machine using Git commands:
   ```bash
   git clone <repository-url>
   ```
2. **Install Dependencies**: Navigate to the cloned directory and install the necessary Python libraries using pip:
   ```bash
   pip install streamlit opencv-python numpy mediapipe Pillow
   ```

## Usage
To use the application, follow these steps:

1. **Start the Application**: In your terminal, navigate to the project directory and execute the following command:
   ```bash
   streamlit run app.py
   ```
2. **Access the Application**: The application will automatically open in your default web browser. If it does not, you can manually access it by visiting `http://localhost:8501` in your browser.
3. **Interact with the App**: Enable your webcam when prompted and observe the facial landmark detection in real-time. The application will display the facial landmarks as overlays on your live video feed.

## Contributing
We encourage contributions from the community, whether it's fixing bugs, improving the documentation, or suggesting new features. Here's how you can contribute:

1. **Fork the Repository**: Fork the project to your GitHub account.
2. **Create a Feature Branch**: Create a new branch for each feature or improvement.
3. **Send a Pull Request**: After you've completed your changes, send a pull request from your feature branch. Please provide a clear description of the problem and solution, including any relevant issues.

## Acknowledgments
- **MediaPipe**: For providing the powerful FaceMesh technology.
- **Streamlit**: For the intuitive framework that powers the application's frontend.
