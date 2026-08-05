import streamlit as st
from streamlit_lottie import st_lottie

from utils.images import (
    LOGO,
    HERO,
    DOCTOR,
    DASHBOARD
)

from components.animations import load_lottie


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Hospital Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------
# Load Lottie Animation
# ---------------------------------------

lottie = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_j1adxtyb.json"
)

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.image(LOGO, width=100)

st.sidebar.title("🏥 AI Hospital")

st.sidebar.success("Navigate using the pages menu.")

# ---------------------------------------
# Header
# ---------------------------------------

col1, col2 = st.columns([1,4])

with col1:

    st.image(LOGO, width=120)

with col2:

    st.title("🏥 AI Hospital Assistant")

    st.markdown(
        "### AI Powered Healthcare Platform"
    )

st.divider()

# ---------------------------------------
# Hero Section
# ---------------------------------------

st.image(
    HERO,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------
# Welcome + Animation
# ---------------------------------------

left, right = st.columns([2,1])

with left:

    st.header("Welcome")

    st.write("""
AI Hospital Assistant provides intelligent healthcare services powered by Artificial Intelligence.

Our platform enables patients to:

- 🩺 Predict Diseases
- 📄 Analyze Medical Reports
- 🤖 Chat with AI Doctor
- 📅 Book Appointments
- 💊 Manage Prescriptions
- 🛡 Insurance Assistance
- 🚑 Emergency Support

Experience fast, secure and smart healthcare.
""")

with right:

    st_lottie(
        lottie,
        height=300,
        key="hospital_animation"
    )

st.divider()

# ---------------------------------------
# Services
# ---------------------------------------

st.header("Our Services")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("🩺 Disease Prediction")

    st.write(
        "Predict diseases using Machine Learning."
    )

with c2:

    st.info("📄 Medical Report Analysis")

    st.write(
        "Summarize reports using Gemini AI."
    )

with c3:

    st.info("🤖 AI Medical Chatbot")

    st.write(
        "Ask medical questions using RAG."
    )

c4, c5, c6 = st.columns(3)

with c4:

    st.success("📅 Appointment Booking")

with c5:

    st.warning("💊 Prescription Management")

with c6:

    st.error("🚑 Emergency Assistance")

st.divider()

# ---------------------------------------
# About Section
# ---------------------------------------

left, right = st.columns([1,2])

with left:

    st.image(
        DOCTOR,
        use_container_width=True
    )

with right:

    st.header("Why Choose AI Hospital Assistant?")

    st.write("""
✔ Fast Disease Prediction

✔ AI Medical Chatbot

✔ Medical Report Summarization

✔ Smart Appointment Booking

✔ Prescription Management

✔ Insurance Assistance

✔ Emergency Response

✔ Secure Patient Records
""")

st.divider()

# ---------------------------------------
# Statistics
# ---------------------------------------

st.header("Hospital Statistics")

a, b, c, d = st.columns(4)

a.metric("Patients", "12,540", "+350")

b.metric("Doctors", "125", "+12")

c.metric("Appointments", "3,240", "+280")

d.metric("AI Accuracy", "97.8%", "+1.2%")

st.divider()

# ---------------------------------------
# Dashboard Banner
# ---------------------------------------

st.image(
    DASHBOARD,
    use_container_width=True
)

st.divider()

# ---------------------------------------
# Footer
# ---------------------------------------

st.markdown(
    """
---
<center>

### 🏥 AI Hospital Assistant

Developed using

FastAPI • Streamlit • Gemini AI • LangChain • LangGraph • ChromaDB

© 2026 AI Hospital Assistant

</center>
""",
    unsafe_allow_html=True
)