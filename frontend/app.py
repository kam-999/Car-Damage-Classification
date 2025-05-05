import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Car Damage Classifier")

st.title("🚗 Car Damage Classifier")
st.write("Upload an image of a car, and the model will predict the type and location of damage.")

uploaded_file = st.file_uploader("Choose a car image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Sending image to the model..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/predict",  # Your FastAPI endpoint
                    files={"file": uploaded_file.getvalue()}
                )
                result = response.json()
                if "prediction" in result:
                    st.success(f"🔍 Prediction: **{result['prediction']}**")
                else:
                    st.error(f"Error: {result.get('error', 'Unknown error')}")
            except Exception as e:
                st.error(f"Failed to connect to backend: {e}")
