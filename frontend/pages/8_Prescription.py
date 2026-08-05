import streamlit as st
import requests
from PIL import Image
import os
from datetime import date


# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Prescription Generator",
    page_icon="💊",
    layout="wide"
)


# -------------------------------------------------------
# CSS
# -------------------------------------------------------

st.markdown("""
<style>

.main{
background:#F5F9FF;
}

.title{
font-size:36px;
font-weight:bold;
color:#0B5394;
}

.subtitle{
font-size:18px;
color:gray;
}

.card{

background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 3px 10px rgba(0,0,0,0.1);

}

.section-title{

font-size:22px;
font-weight:bold;
color:#0B5394;

}

</style>
""",
unsafe_allow_html=True)



# -------------------------------------------------------
# IMAGE
# -------------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


image_path = os.path.join(
    BASE_DIR,
    "assets",
    "prescription.jpg"
)



# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

left,right = st.columns([2,1])


with left:

    st.markdown(
        "<div class='title'>💊 AI Prescription Generator</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class='subtitle'>
        Generate AI assisted prescriptions using patient information.
        </div>
        """,
        unsafe_allow_html=True
    )


with right:

    if os.path.exists(image_path):

        st.image(
            Image.open(image_path),
            use_container_width=True
        )

    else:

        st.warning(
            "Image not found. Add prescription.jpg inside assets folder."
        )



st.write("")



# -------------------------------------------------------
# FORM
# -------------------------------------------------------

with st.form(
    "prescription_form"
):


    patient_name = st.text_input(
        "Patient Name",
        placeholder="Example: Chakri"
    )


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
            "Female",
            "Other"
        ]
    )


    disease = st.text_input(
        "Disease",
        placeholder="Example: Viral Fever"
    )


    symptoms = st.text_area(
        "Symptoms",
        placeholder="Example: fever, headache, body pains"
    )


    allergies = st.text_area(
        "Known Allergies",
        placeholder="Example: No known allergies"
    )


    submit = st.form_submit_button(
        "💊 Generate Prescription",
        use_container_width=True
    )



# -------------------------------------------------------
# API
# -------------------------------------------------------

if submit:


    payload = {

        "patient_name": patient_name,

        "age": age,

        "gender": gender,

        "disease": disease,

        "symptoms": symptoms,

        "allergies": allergies

    }



    try:


        response = requests.post(

            "http://127.0.0.1:8000/prescription/generate",

            json=payload,

            timeout=120

        )



        if response.status_code == 200:


            result = response.json()


            prescription = result.get(
                "prescription",
                {}
            )


            st.success(
                "Prescription Generated Successfully"
            )



            st.divider()



            st.markdown(
                "<div class='card'>",
                unsafe_allow_html=True
            )


            st.header(
                "🏥 AI Hospital Assistant"
            )


            st.write(
                "**Date:**",
                date.today()
            )


            st.write(
                "**Patient:**",
                patient_name
            )


            st.write(
                "**Age:**",
                age
            )


            st.write(
                "**Gender:**",
                gender
            )



            st.divider()



            # -------------------------------
            # DIAGNOSIS
            # -------------------------------


            st.markdown(
                "<div class='section-title'>Diagnosis</div>",
                unsafe_allow_html=True
            )


            st.info(
                prescription.get(
                    "disease",
                    disease
                )
            )



            st.divider()



            # -------------------------------
            # MEDICINES
            # -------------------------------


            st.markdown(
                "<div class='section-title'>💊 Medicines</div>",
                unsafe_allow_html=True
            )


            medicines = prescription.get(
                "medicines",
                []
            )



            if medicines:


                for med in medicines:


                    st.success(
                        "💊 " + med["name"]
                    )


                    st.write(
                        "**Dosage:**",
                        med["dosage"]
                    )


                    st.write(
                        "**Purpose:**",
                        med["purpose"]
                    )


                    st.divider()


            else:

                st.warning(
                    "No medicines returned."
                )



            # -------------------------------
            # PRECAUTIONS
            # -------------------------------


            st.markdown(
                "<div class='section-title'>📝 Precautions</div>",
                unsafe_allow_html=True
            )


            precautions = prescription.get(
                "precautions",
                []
            )


            if precautions:


                for item in precautions:

                    st.write(
                        "✅",
                        item
                    )


            else:

                st.warning(
                    "No precautions available."
                )



            st.divider()



            # -------------------------------
            # LIFESTYLE
            # -------------------------------


            st.markdown(
                "<div class='section-title'>🌿 Lifestyle Recommendations</div>",
                unsafe_allow_html=True
            )


            lifestyle = prescription.get(
                "lifestyle",
                []
            )


            if lifestyle:


                for item in lifestyle:

                    st.write(
                        "✅",
                        item
                    )


            else:


                st.write(
                    "Consult your physician if symptoms continue."
                )



            st.divider()



            # -------------------------------
            # DISCLAIMER
            # -------------------------------


            st.markdown(
                "<div class='section-title'>⚠️ Disclaimer</div>",
                unsafe_allow_html=True
            )


            st.warning(
                prescription.get(
                    "disclaimer",
                    "Consult a licensed doctor."
                )
            )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )



            # Download option

            prescription_text = f"""

AI Hospital Assistant Prescription

Date:
{date.today()}


Patient:
{patient_name}


Disease:
{prescription.get("disease")}


Medicines:

{medicines}


Precautions:

{precautions}


Lifestyle:

{lifestyle}


Disclaimer:

{prescription.get("disclaimer")}

"""


            st.download_button(

                "⬇️ Download Prescription",

                prescription_text,

                file_name="AI_Prescription.txt"

            )



        else:


            st.error(
                "Backend Error"
            )

            st.write(
                response.text
            )



    except Exception as e:


        st.error(
            "Backend not connected"
        )


        st.exception(e)



# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.divider()


st.info(
"""
This AI prescription is for demonstration purposes only.

Consult a qualified medical professional before taking medicines.
"""
)