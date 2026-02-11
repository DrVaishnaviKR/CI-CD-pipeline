import streamlit as st
import requests

API_URL = "https://ci-cd-pipeline-qboe.onrender.com/predict"

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("🏠 House Price Prediction")
st.write("Enter property details to get predicted price")

area = st.number_input("Area (sq ft)", min_value=100.0, step=50.0)
bedrooms = st.number_input("Bedrooms", min_value=1, step=1)

if st.button("Predict Price"):
    payload = {
        "area": area,
        "bedrooms": int(bedrooms)
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=30)

        st.write("Status:", response.status_code)
        st.write("Response:", response.text)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price: ₹ {result['Predicted_price']:,.2f}")
        else:
            st.error("Prediction failed. Check response above.")

    except Exception as e:
        st.error(f"Connection error: {e}")
