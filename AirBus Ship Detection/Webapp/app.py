# Save this script as 'app.py'

import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

# Function to load the pre-trained model
@st.cache(allow_output_mutation=True)
def load_model():
    model = torch.load(r'Model\RNS_model.pkl', map_location=torch.device('cuda'))
    model.eval()
    return model

# Streamlit app
def main():
    st.title("AirBus Ship detection with UNet Segmentation Model")
    st.text("Upload an image for segmentation")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("L")
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Perform inference
        transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
        ])
        image_tensor = transform(image).unsqueeze(0).to('cuda' if torch.cuda.is_available() else 'cpu')

        model = load_model()
        with torch.no_grad():
            output = model(image_tensor)

        # Display segmentation result (assuming binary output)
        mask = output.squeeze().cpu().numpy()
        mask = (mask > 0.5).astype(np.uint8)  # Threshold to create binary mask

        st.image(mask * 255, caption='Segmentation Mask', use_column_width=True)

if __name__ == '__main__':
    main()
