# STEP 1
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# STEP 2
class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        image = frame.to_ndarray(format="bgr24")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Perform facial landmark detection
        results = face_mesh.process(image)

        # Draw facial landmarks
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=drawing_spec)

        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#STEP 3
def detect_facial_landmarks(image):
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    results = face_mesh.process(image)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_drawing.draw_landmarks(
                image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=drawing_spec)

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# STEP 4
def main():
    st.title('Face Mask and Landmark Detection App')

    option = st.sidebar.selectbox('Choose the App Mode:', ['Documentation','Live Video', 'Photo'])
    
    if option == 'Photo':
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
        if image_file is not None:
            image = Image.open(image_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
            if st.button('Detect Landmarks'):
                result_img = detect_facial_landmarks(image)
                st.image(result_img, use_column_width=True)

    elif option == 'Live Video':
        st.header("Live Facial Landmark Detection")
        st.write("This will use your webcam to detect facial landmarks.")
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
        
    elif option == 'Documentation':
        st.header('Documentation')
        st.subheader('Facial Landmark Detection App Documentation')
        st.markdown('''
        #### Overview
        This application utilizes MediaPipe and Streamlit to perform real-time facial landmark detection. Users can see their facial landmarks overlaid on their video feed in real-time.
        Options can be chosen from the provided SideBar.
        #### How to Install and Run the Application
        1. **Install Required Libraries**: You need to have Python installed on your system. Install the required Python libraries using pip:
        ```
            pip install streamlit cv2 numpy Pillow mediapipe streamlit_webrtc
        ```
        2. **Run the Application**: Navigate to the directory containing the `app.py` file and run the following command:
        ```
            streamlit run app.py
        ```
        3. **Access the Application**: Open your web browser and go to `http://localhost:8501`. The application should be running and ready to use.

        #### How It Works
        - **Video Streaming**: Once the application is running, it will access your webcam. Make sure you permit the browser to use your webcam.
        - **Facial Landmark Detection**: The application processes each video frame to detect facial landmarks using MediaPipe's FaceMesh model. Detected landmarks are then drawn directly on the video feed, providing a visual representation of the face structure in real-time.

        #### Use Cases
        This tool can be used for various purposes, including:
        - Augmented reality development.
        - Facial recognition projects.
        - Studies and applications in human-computer interaction.
        ''')

if __name__ == "__main__":
    main()
