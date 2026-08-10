import streamlit as st
import requests
from PIL import Image
import os
from datetime import date, timedelta
from utils.config import BACKEND_URL

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Book Appointment",
    page_icon="📅",
    layout="wide"
)


# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------

API_URL = BACKEND_URL


USER_ID = st.session_state.get(
    "user_id",
    1
)



# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown(
"""
<style>

.main{
    background:#F5F9FF;
}

.block-container{
    padding-top:1rem;
}

.title{
    color:#0B5394;
    font-size:36px;
    font-weight:bold;
}

.subtitle{
    color:#555;
    font-size:18px;
}

.card{

    background:white;

    color:#222;

    padding:20px;

    border-radius:15px;

    border:1px solid #ddd;

    box-shadow:
    0px 2px 10px rgba(0,0,0,0.08);

    margin-top:15px;

}


</style>
""",
unsafe_allow_html=True
)



# ---------------------------------------------------
# IMAGE PATHS
# ---------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


appointment_image = os.path.join(
    BASE_DIR,
    "assets",
    "appointment.jpg"
)



doctor_image = os.path.join(
    BASE_DIR,
    "assets",
    "doctor.png"
)



# ---------------------------------------------------
# HEADER IMAGE
# ---------------------------------------------------

if os.path.exists(appointment_image):

    st.image(
        Image.open(appointment_image),
        use_container_width=True
    )



# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<div class='title'>📅 Book Doctor Appointment</div>",
    unsafe_allow_html=True
)



st.markdown(
    "<div class='subtitle'>Book your appointment with experienced doctors.</div>",
    unsafe_allow_html=True
)



st.divider()



# ---------------------------------------------------
# LAYOUT
# ---------------------------------------------------

left,right = st.columns(
    [2,1]
)



# ---------------------------------------------------
# FORM
# ---------------------------------------------------

with left:


    with st.form(
        "appointment_form"
    ):


        patient_name = st.text_input(
            "Patient Name"
        )



        doctor = st.selectbox(

            "Select Doctor",

            [

                "Dr. Rajesh Kumar (General Physician)",

                "Dr. Priya Sharma (Cardiologist)",

                "Dr. Anil Reddy (Neurologist)",

                "Dr. Sneha Patel (Dermatologist)",

                "Dr. Arjun Rao (Orthopedic)",

                "Dr. Kavya Nair (Pediatrician)"

            ]

        )



        appointment_date = st.date_input(

            "Appointment Date",

            min_value=date.today(),

            value=date.today()+timedelta(days=1)

        )



        appointment_time = st.selectbox(

            "Appointment Time",

            [

                "09:00 AM",

                "10:00 AM",

                "11:00 AM",

                "12:00 PM",

                "02:00 PM",

                "03:00 PM",

                "04:00 PM",

                "05:00 PM"

            ]

        )



        symptoms = st.text_area(

            "Symptoms / Reason for Visit"

        )



        submit = st.form_submit_button(

            "📅 Book Appointment"

        )




# ---------------------------------------------------
# RIGHT SIDE
# ---------------------------------------------------

with right:


    if os.path.exists(doctor_image):

        st.image(

            Image.open(doctor_image),

            use_container_width=True

        )



    st.markdown(
"""
<div class="card">

<h3>👨‍⚕️ Consultation</h3>

✔ General Checkup

<br>

✔ Specialist Consultation

<br>

✔ Follow-up Visit

<br>

✔ Health Checkup


</div>
""",
unsafe_allow_html=True
)




# ---------------------------------------------------
# BOOK APPOINTMENT API
# ---------------------------------------------------

if submit:


    appointment_datetime = (

        str(appointment_date)

        +

        "T10:00:00"

    )



    payload = {


        "user_id": USER_ID,


        "patient_name": patient_name,


        "doctor_name": doctor,


        "appointment_date":
        appointment_datetime


    }



    try:


        response = requests.post(

            API_URL +
            "/appointments/book",

            json=payload,

            timeout=60

        )



        if response.status_code in [200,201]:


            st.success(
                "Appointment booked successfully"
            )


            st.info(
f"""
Patient:

{patient_name}


Doctor:

{doctor}


Date:

{appointment_date}


Time:

{appointment_time}


Status:

Booked
"""
            )


        else:


            st.error(
                response.text
            )



    except Exception as e:


        st.error(
            "Backend connection failed"
        )

        st.exception(e)




# ---------------------------------------------------
# APPOINTMENT HISTORY
# ---------------------------------------------------

st.divider()


st.header(
    "📅 My Appointments"
)



if st.button(
    "View My Appointments"
):


    try:


        response = requests.get(

            API_URL +

            f"/profile/{USER_ID}/appointments/user/{USER_ID}",

            timeout=60

        )



        if response.status_code == 200:


            appointments=response.json()



            if appointments:


                for appointment in appointments:


                    st.markdown(
f"""
<div class="card">

👨‍⚕️ Doctor:

{appointment.get('doctor_name')}


<br><br>

📅 Date:

{appointment.get('appointment_date')}


<br><br>

📌 Status:

{appointment.get('status')}


</div>
""",
unsafe_allow_html=True
                    )



            else:


                st.info(
                    "No appointments found"
                )


        else:

            st.error(
                response.text
            )



    except Exception as e:


        st.error(
            "Unable to load appointments"
        )




# ---------------------------------------------------
# CANCEL APPOINTMENT
# ---------------------------------------------------

st.divider()


st.header(
    "❌ Cancel Appointment"
)



appointment_id = st.number_input(

    "Appointment ID",

    min_value=1,

    step=1

)



if st.button(
    "Cancel Appointment"
):


    try:


        response=requests.delete(

            API_URL +

            f"/appointments/cancel/{appointment_id}",

            timeout=60

        )


        if response.status_code==200:


            st.success(
                "Appointment cancelled"
            )


        else:


            st.error(
                response.text
            )


    except Exception as e:


        st.error(
            str(e)
        )




# ---------------------------------------------------
# INFORMATION
# ---------------------------------------------------

st.divider()


st.subheader(
    "Hospital Timing"
)



col1,col2=st.columns(2)



with col1:

    st.success(
"""
Monday - Friday

09:00 AM - 06:00 PM
"""
    )



with col2:

    st.success(
"""
Saturday

09:00 AM - 01:00 PM
"""
    )



st.info(
"""
Please arrive 15 minutes before your appointment.

Carry previous prescriptions and medical reports.
"""
)