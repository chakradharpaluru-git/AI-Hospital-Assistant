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

st.markdown(
"""
<style>

.main {
    background:#F5F9FF;
}


.title {
    font-size:40px;
    font-weight:bold;
    color:#0B5394;
}


.subtitle {
    font-size:18px;
    color:#444444;
}


/* RESULT CARD */

.result-card {

    background:white;

    padding:25px;

    border-radius:15px;

    border:1px solid #dddddd;

    box-shadow:
    0px 5px 15px rgba(0,0,0,0.12);

    margin-top:20px;

}


/* METRIC */

.metric-card {

    background:#F8F9FA;

    padding:20px;

    border-radius:12px;

    border:1px solid #cccccc;

}


.metric-title {

    color:#555555;

    font-size:16px;

}


.metric-value {

    color:#0B5394;

    font-size:28px;

    font-weight:bold;

}



/* CONFIDENCE CARDS */


.success-card {

    background:#D5F5E3;

    color:#145A32;

    padding:20px;

    border-radius:12px;

    border-left:8px solid #27AE60;

}



.warning-card {

    background:#FCF3CF;

    color:#7D6608;

    padding:20px;

    border-radius:12px;

    border-left:8px solid #F1C40F;

}



.danger-card {

    background:#FADBD8;

    color:#922B21;

    padding:20px;

    border-radius:12px;

    border-left:8px solid #E74C3C;

}



.info-box {

    background:white;

    color:#222222;

    padding:20px;

    border-radius:12px;

    border:1px solid #ddd;

}



</style>
""",
unsafe_allow_html=True
)



# ==========================================================
# IMAGE PATH
# ==========================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


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



left,right = st.columns(
    [2,1]
)



# ==========================================================
# FORM
# ==========================================================


with left:


    with st.form(
        "prediction_form"
    ):


        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=22
        )


        gender = st.selectbox(
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
            "🔍 Predict Disease"
        )



# ==========================================================
# IMAGE
# ==========================================================


with right:


    if os.path.exists(doctor_path):

        st.image(
            Image.open(doctor_path),
            width=300
        )



# ==========================================================
# API CALL
# ==========================================================


if submit:


    symptoms=[]


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



    if len(symptoms)==0:

        st.warning(
            "⚠ Please select at least one symptom."
        )

        st.stop()



    payload={

        "symptoms":symptoms

    }



    with st.spinner(
        "🤖 AI is analyzing your symptoms..."
    ):


        try:


            response=requests.post(

                "http://127.0.0.1:8000/disease/predict",

                json=payload,

                timeout=60

            )



            if response.status_code==200:


                result=response.json()



                disease=result.get(
                    "disease",
                    "Unknown"
                )


                confidence=float(
                    result.get(
                        "confidence",
                        0
                    )
                )



                st.success(
                    "Prediction Completed Successfully"
                )



                st.markdown(
                    "<div class='result-card'>",
                    unsafe_allow_html=True
                )


                st.markdown(
                    "## 🩺 Prediction Result"
                )



                c1,c2=st.columns(2)



                with c1:

                    st.markdown(
                    f"""
                    <div class="metric-card">

                    <div class="metric-title">
                    Possible Disease
                    </div>

                    <div class="metric-value">
                    {disease}
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                    )



                with c2:


                    st.markdown(
                    f"""
                    <div class="metric-card">

                    <div class="metric-title">
                    Confidence
                    </div>

                    <div class="metric-value">
                    {confidence:.2f}%
                    </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                    )




                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )



                if confidence>=80:

                    card="success-card"

                    message="🟢 High Confidence Prediction"



                elif confidence>=50:

                    card="warning-card"

                    message="🟡 Moderate Confidence Prediction"



                else:

                    card="danger-card"

                    message="🔴 Low Confidence Prediction"




                st.markdown(
                f"""

<div class="{card}">

<h3>{message}</h3>


<b>Recommendation</b>

<br><br>


Please consult a qualified doctor before taking any medication.

<br><br>

This AI prediction is intended for educational purposes only.

</div>

""",
                unsafe_allow_html=True
                )



            else:


                st.error(
                    "Prediction API Error"
                )

                st.code(
                    response.text
                )



        except requests.exceptions.ConnectionError:


            st.error(
                "❌ Unable to connect to FastAPI Server."
            )



        except Exception as e:


            st.exception(e)




# ==========================================================
# INFORMATION
# ==========================================================


st.divider()


st.subheader(
    "ℹ About Disease Prediction"
)



st.markdown(
"""

<div class="info-box">

This AI model predicts the most likely disease based on selected symptoms.

<br><br>

⚠ The prediction is intended for educational purposes only.

<br><br>

Always consult a qualified healthcare professional for proper diagnosis and treatment.

</div>

""",
unsafe_allow_html=True
)