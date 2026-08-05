import streamlit as st
from PIL import Image
import os

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Hospital Assistant - Dashboard",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f9ff;
}

.block-container{
    padding-top:1rem;
}

h1,h2,h3{
    color:#0b5394;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
    text-align:center;
    margin-bottom:20px;
}

.metric{
    font-size:35px;
    font-weight:bold;
    color:#0b5394;
}

.small{
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Image Paths
# ---------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

banner_path = os.path.join(BASE_DIR, "assets", "dashboard_banner.jpg")
doctor_path = os.path.join(BASE_DIR, "assets", "doctor.png")

# ---------------------------------------------------
# Banner
# ---------------------------------------------------
if os.path.exists(banner_path):
    banner = Image.open(banner_path)
    st.image(banner, use_container_width=True)
else:
    st.warning("dashboard_banner.jpg not found.")

st.write("")

# ---------------------------------------------------
# Welcome Section
# ---------------------------------------------------
col1, col2 = st.columns([2,1])

with col1:

    st.title("🏥 AI Hospital Assistant")

    st.markdown("""
Welcome to the **AI Hospital Assistant Dashboard**.

This platform helps patients and doctors using Artificial Intelligence.

### Features

- 🩺 Disease Prediction
- 📄 Medical Report Summarization
- 🤖 AI Medical Chatbot
- 💊 Prescription Generator
- 📅 Appointment Booking
- 🏥 Insurance Assistance
- 🚑 Emergency Support

Use the navigation menu on the left to access all services.
""")

with col2:

    if os.path.exists(doctor_path):
        doctor = Image.open(doctor_path)
        st.image(doctor, width=320)
    else:
        st.warning("doctor.png not found.")

st.divider()

# ---------------------------------------------------
# Statistics Cards
# ---------------------------------------------------
st.subheader("📊 Hospital Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
        <div class="metric">250+</div>
        <div class="small">Doctors</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <div class="metric">12K+</div>
        <div class="small">Patients</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <div class="metric">98%</div>
        <div class="small">Prediction Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
        <div class="metric">24/7</div>
        <div class="small">AI Support</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# Quick Actions
# ---------------------------------------------------
st.subheader("⚡ Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🩺 Disease Prediction", use_container_width=True):
        st.success("Open Disease Prediction from the left sidebar.")

with col2:
    if st.button("📄 Upload Medical Report", use_container_width=True):
        st.success("Open Upload Reports from the sidebar.")

with col3:
    if st.button("🤖 AI Chatbot", use_container_width=True):
        st.success("Open AI Chatbot from the sidebar.")

st.divider()

# ---------------------------------------------------
# Services
# ---------------------------------------------------
st.subheader("🏥 Available Services")

col1, col2 = st.columns(2)

with col1:

    st.info("""
🩺 Disease Prediction

Predict possible diseases using symptoms with AI.
""")

    st.info("""
📄 Medical Report Summarizer

Upload reports and receive an AI-generated summary.
""")

    st.info("""
💊 Prescription Generator

Generate prescriptions after consultation.
""")

with col2:

    st.info("""
📅 Appointment Booking

Book appointments with doctors online.
""")

    st.info("""
🛡 Insurance Assistance

Understand insurance coverage and claims.
""")

    st.info("""
🚑 Emergency Assistance

Quick access to emergency medical services.
""")

st.divider()

# ---------------------------------------------------
# Notifications
# ---------------------------------------------------
st.subheader("🔔 Notifications")

st.success("✔ AI Hospital Assistant is running successfully.")

st.warning("Remember to upload your medical reports in PDF format.")

st.info("Need help? Open the AI Chatbot from the sidebar.")

st.divider()

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("""
<center>

### ❤️ AI Hospital Assistant

Powered by

**FastAPI • Streamlit • Gemini AI • Machine Learning**

</center>
""", unsafe_allow_html=True)