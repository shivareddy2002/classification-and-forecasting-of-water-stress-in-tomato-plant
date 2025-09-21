import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

# Import utilities from utils package
from utils import (
    init_db,
    user_exists,
    verify_password,
    add_user,
    load_models,
    preprocess_data,
    load_scaler,
)

# ------------------- Streamlit Config -------------------
st.set_page_config(
    page_title="Classification and Forecasting of Water Stress in Tomato Plant using Bioristor Data",
    layout="wide",
    page_icon="🍅"
)

# 🌿 Custom Styling
page_bg = """
<style>
    .stApp {
        background: linear-gradient(135deg, #0D1B1E, #1B5E20, #0B3D0B);
        color: #E8F5E9;
        background-attachment: fixed;
        background-size: cover;
    }
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("https://www.transparenttextures.com/patterns/asfalt-light.png");
        opacity: 0.08;
        z-index: 0;
    }
    h1 {
        color: #FF5722 !important;
        text-align: center;
        font-weight: bold;
    }
    h2, h3 { color: #C5E1A5 !important; }
    hr { border: 1px solid #66BB6A; }
    div.stButton > button {
        background: linear-gradient(90deg, #2E7D32, #1B5E20);
        color: white;
        border-radius: 10px;
        font-size: 16px;
        height: 3em;
        width: 13em;
        transition: 0.3s;
        z-index: 1;
        position: relative;
    }
    div.stButton > button:hover {
        background: #0D3D0D;
        transform: scale(1.05);
    }
    .stFileUploader label {
        color: #AED581 !important;
        font-weight: bold;
    }
    .stDataFrame {
        background: #1E272E;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Initialize database
init_db()

# ------------------- Session State -------------------
if "page" not in st.session_state:
    st.session_state.page = "login"
if "username" not in st.session_state:
    st.session_state.username = None
if "models" not in st.session_state:
    st.session_state.models = None
if "scaler" not in st.session_state:
    st.session_state.scaler = None
if "expected_columns" not in st.session_state:
    st.session_state.expected_columns = None


# ------------------- Pages -------------------
def login_page():
    st.title("🔑 Login to Continue")

    username = st.text_input("👤 Username")
    password = st.text_input("🔒 Password", type="password")

    if st.button("➡️ Login"):
        if not user_exists(username):
            st.error("🚨 User not found. Please sign up first.")
        else:
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("SELECT password FROM users WHERE username=?", (username,))
            row = c.fetchone()
            conn.close()

            if row and verify_password(password, row[0]):
                st.session_state.username = username
                st.session_state.page = "home"
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

    st.info("Don’t have an account?")
    if st.button("📝 Go to Signup"):
        st.session_state.page = "signup"
        st.rerun()


def signup_page():
    st.title("📝 Create a New Account")

    username = st.text_input("👤 Choose a username")
    password = st.text_input("🔒 Choose a password", type="password")

    if st.button("✅ Create Account"):
        if user_exists(username):
            st.error("⚠️ User already exists. Please login instead.")
        else:
            add_user(username, password)
            st.success("🎉 Account created successfully! Please log in.")
            st.session_state.page = "login"
            st.rerun()

    st.info("Already have an account?")
    if st.button("🔑 Go to Login"):
        st.session_state.page = "login"
        st.rerun()


def home_page():
    st.sidebar.title(f"👋 Welcome, {st.session_state.username}")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.session_state.page = "login"
        st.rerun()

    st.markdown("<h1>🍅 Classification and Forecasting of Water Stress in Tomato Plant using Bioristor Data</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Step 1: Upload Training Data
    st.header("📂 Step 1: Upload Training Data")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Training data uploaded successfully!")
        st.write("### 🔍 Preview of Data", df.head())

        X = preprocess_data(df)
        y = df["y"] if "y" in df.columns else None
        st.session_state.X_train = X
        st.session_state.y_train = y

        if st.button("⚙️ Train Model"):
            with st.spinner("⏳ Training model..."):
                model = load_models(X, y)
                st.session_state.models = model
            st.success("🎉 Model trained and saved successfully!")

    # Step 2: Predictions
    if st.session_state.models:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.header("🔮 Step 2: Make Predictions")

        uploaded_test = st.file_uploader("Upload Test Data (CSV)", type=["csv"])
        if uploaded_test:
            test_df = pd.read_csv(uploaded_test)
            st.write("### 🔍 Preview of Test Data", test_df.head())

            scaler, expected_columns = load_scaler()
            st.session_state.scaler, st.session_state.expected_columns = scaler, expected_columns

            X_test = preprocess_data(test_df, scaler, expected_columns)
            X_test = np.array(X_test).reshape(len(X_test), -1)

            keras_model = st.session_state.models
            y_pred = (keras_model.predict(X_test) > 0.5).astype(int)

            y_mapped = np.where(y_pred.flatten() == 1, "🌱 No Stress", "⚠️ Stress")
            result = pd.DataFrame({"Prediction": y_pred.flatten(), "Status": y_mapped})

            st.success("✅ Predictions generated successfully!")
            st.write("### 📊 Prediction Results", result)

            st.download_button(
                label="⬇️ Download Predictions",
                data=result.to_csv(index=False).encode("utf-8"),
                file_name="predictions.csv",
                mime="text/csv"
            )


# ------------------- Navigation -------------------
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "signup":
    signup_page()
elif st.session_state.page == "home":
    home_page()
