import streamlit as st
import requests
from PIL import Image
import os

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

# ==========================================================
# CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background:#F5F9FF;
}

.title{
    font-size:40px;
    font-weight:bold;
    color:#0B5394;
}

.subtitle{
    font-size:18px;
    color:gray;
}

.result-box{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.1);
    margin-top:20px;
}

.success-card{
    background:#E8F8F5;
    border-left:8px solid #2ECC71;
    padding:20px;
    border-radius:10px;
}

.warning-card{
    background:#FEF9E7;
    border-left:8px solid #F1C40F;
    padding:20px;
    border-radius:10px;
}

.danger-card{
    background:#FDEDEC;
    border-left:8px solid #E74C3C;
    padding:20px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# IMAGE
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

doctor_path = os.path.join(
    BASE_DIR,
    "assets",
    "doctor.png"
)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
    "<div class='title'>🩺 Disease Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Enter your symptoms and let AI predict the possible disease.</div>",
    unsafe_allow_html=True
)

st.write("")

left, right = st.columns([2,1])

# ==========================================================
# FORM
# ==========================================================

with left:

    with st.form("prediction_form"):

        st.number_input(
            "Age",
            1,
            120,
            30
        )

        st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

        fever = st.checkbox("🤒 Fever")
        cough = st.checkbox("😷 Cough")
        headache = st.checkbox("🤕 Headache")
        fatigue = st.checkbox("😴 Fatigue")
        sore = st.checkbox("😣 Sore Throat")
        pain = st.checkbox("💪 Body Pain")
        nausea = st.checkbox("🤢 Nausea")
        vomiting = st.checkbox("🤮 Vomiting")
        diarrhea = st.checkbox("🚽 Diarrhea")
        breathing = st.checkbox("🫁 Breathing Difficulty")

        submit = st.form_submit_button(
            "🔍 Predict Disease",
            width="stretch"
        )

# ==========================================================
# IMAGE
# ==========================================================

with right:

    if os.path.exists(doctor_path):

        st.image(
            Image.open(doctor_path),
            width="stretch"
        )

# ==========================================================
# API
# ==========================================================

if submit:

    symptoms = []

    if fever:
        symptoms.append("high_fever")

    if cough:
        symptoms.append("cough")

    if headache:
        symptoms.append("headache")

    if fatigue:
        symptoms.append("fatigue")

    if sore:
        symptoms.append("throat_irritation")

    if pain:
        symptoms.append("muscle_pain")

    if nausea:
        symptoms.append("nausea")

    if vomiting:
        symptoms.append("vomiting")

    if diarrhea:
        symptoms.append("diarrhoea")

    if breathing:
        symptoms.append("breathlessness")

    if len(symptoms) == 0:

        st.warning("⚠ Please select at least one symptom.")

        st.stop()

    payload = {
        "symptoms": symptoms
    }

    with st.spinner("🤖 AI is analyzing your symptoms..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/disease/predict",
                json=payload,
                timeout=60
            )

            if response.status_code == 200:

                result = response.json()

                disease = result["disease"]
                confidence = float(result["confidence"])

                st.success("Prediction Completed Successfully")

                st.markdown("## 🩺 Prediction Result")

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "Possible Disease",
                        disease
                    )

                with c2:

                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )

                if confidence >= 80:

                    card = "success-card"
                    message = "🟢 High Confidence Prediction"

                elif confidence >= 50:

                    card = "warning-card"
                    message = "🟡 Moderate Confidence Prediction"

                else:

                    card = "danger-card"
                    message = "🔴 Low Confidence Prediction"

                st.markdown(
                    f"""
<div class="{card}">

<h3>{message}</h3>

<b>Recommendation</b><br>

Please consult a qualified doctor before taking any medication.
This AI prediction is intended for educational purposes only.

</div>
""",
                    unsafe_allow_html=True
                )

            else:

                st.error("Prediction API Error")

                st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error("❌ Unable to connect to FastAPI Server.")

        except Exception as e:

            st.exception(e)

# ==========================================================
# INFO
# ==========================================================

st.divider()

st.subheader("ℹ About Disease Prediction")

st.info(
"""
This AI model predicts the most likely disease based on the selected symptoms.

⚠ The prediction is intended for educational purposes only.

Always consult a qualified healthcare professional for proper diagnosis and treatment.
"""
)