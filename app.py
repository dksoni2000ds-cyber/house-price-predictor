import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("house_price_model.pkl")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("About")

st.sidebar.info("""
This application predicts house prices using a Machine Learning model.

Algorithm:
- Linear Regression

Libraries Used:
- Streamlit
- Pandas
- Scikit-Learn
- Joblib
""")

# -----------------------------
# Title
# -----------------------------
st.title("🏠 House Price Predictor")

st.write("Fill in the details below and click **Predict Price**.")

st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "Area (sq ft)",
        min_value=500,
        value=1500
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        value=3
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        value=2
    )

    stories = st.number_input(
        "Stories",
        min_value=1,
        value=2
    )

    parking = st.number_input(
        "Parking Spaces",
        min_value=0,
        value=2
    )

with col2:

    mainroad = st.selectbox(
        "Main Road",
        ["Yes", "No"]
    )

    guestroom = st.selectbox(
        "Guest Room",
        ["Yes", "No"]
    )

    basement = st.selectbox(
        "Basement",
        ["Yes", "No"]
    )

    hotwaterheating = st.selectbox(
        "Hot Water Heating",
        ["Yes", "No"]
    )

    airconditioning = st.selectbox(
        "Air Conditioning",
        ["Yes", "No"]
    )

    prefarea = st.selectbox(
        "Preferred Area",
        ["Yes", "No"]
    )

    furnishingstatus = st.selectbox(
        "Furnishing Status",
        [
            "Unfurnished",
            "Semi-Furnished",
            "Furnished"
        ]
    )

# -----------------------------
# Convert Inputs
# -----------------------------
mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

if furnishingstatus == "Furnished":
    furnishingstatus = 2
elif furnishingstatus == "Semi-Furnished":
    furnishingstatus = 1
else:
    furnishingstatus = 0

# -----------------------------
# Prediction Button
# -----------------------------
st.markdown("---")

if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated House Price: ₹ {prediction[0]:,.2f}"
    )

    st.balloons()