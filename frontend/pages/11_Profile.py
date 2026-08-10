import streamlit as st
import requests
import pandas as pd
import os
from utils.config import BACKEND_URL
from PIL import Image


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="wide"
)


# =====================================================
# CONFIG
# =====================================================


API_URL = BACKEND_URL


# =====================================================
# GET USER ID
# =====================================================

if "user_id" in st.session_state:

    USER_ID = st.session_state.user_id

else:

    USER_ID = 1



# =====================================================
# CSS
# =====================================================

st.markdown(
"""
<style>

.profile-card{

background:white;
padding:20px;
border-radius:15px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);

}

.section-title{

font-size:25px;
font-weight:bold;
color:#0B5394;

}

</style>
""",
unsafe_allow_html=True
)



# =====================================================
# API FUNCTIONS
# =====================================================


def get_api(endpoint):

    try:

        response = requests.get(

            API_URL + endpoint,

            timeout=30

        )


        if response.status_code == 200:

            return response.json()


        st.error(response.text)

        return None


    except Exception as e:

        st.error(
            f"Backend connection failed: {e}"
        )

        return None




def put_api(endpoint,data):

    try:

        response = requests.put(

            API_URL + endpoint,

            json=data,

            timeout=30

        )

        return response


    except Exception as e:

        st.error(e)

        return None




# =====================================================
# LOAD DATA
# =====================================================


profile = get_api(
    f"/profile/{USER_ID}"
)


appointments = get_api(
    f"/profile/{USER_ID}/appointments"
)


reports = get_api(
    f"/profile/{USER_ID}/reports"
)


prescriptions = get_api(
    f"/profile/{USER_ID}/prescriptions"
)


insurance = get_api(
    f"/profile/{USER_ID}/insurance"
)



if profile is None:

    st.stop()



# =====================================================
# HEADER
# =====================================================


st.title("👤 My Profile")



# =====================================================
# PROFILE CARD
# =====================================================


col1,col2 = st.columns(
    [1,3]
)



with col1:


    image_path = "assets/profile.png"


    if os.path.exists(image_path):

        st.image(

            Image.open(image_path),

            width=180

        )

    else:

        st.write("👤")




with col2:


    st.markdown(

f"""

<div class="profile-card">

<h2>{profile['full_name']}</h2>

<p>📧 {profile['email']}</p>

<p>🆔 Patient ID : {profile['id']}</p>

</div>

""",

unsafe_allow_html=True

)



# =====================================================
# EDIT PROFILE
# =====================================================


st.divider()


st.subheader(
"✏ Edit Profile"
)



with st.form(
"update_profile"
):


    name = st.text_input(

        "Full Name",

        profile["full_name"]

    )


    email = st.text_input(

        "Email",

        profile["email"]

    )


    save = st.form_submit_button(
        "Update"
    )



    if save:


        result = put_api(

            f"/profile/{USER_ID}",

            {

            "full_name":name,

            "email":email

            }

        )


        if result and result.status_code == 200:


            st.success(
                "Profile updated successfully"
            )


            st.rerun()



# =====================================================
# APPOINTMENTS
# =====================================================


st.divider()


st.subheader(
"📅 Appointment History"
)



if appointments:


    st.dataframe(

        pd.DataFrame(
            appointments
        ),

        width="stretch"

    )


else:

    st.warning(
        "No appointments found"
    )



# =====================================================
# REPORTS
# =====================================================


st.divider()


st.subheader(
"📄 Uploaded Reports"
)



if reports:


    for report in reports:


        st.info(

f"""
📄 File:
{report.get('filename')}


Summary:

{report.get('summary')}
"""

        )


else:

    st.warning(
        "No reports uploaded"
    )



# =====================================================
# PRESCRIPTIONS
# =====================================================


st.divider()


st.subheader(
"💊 Prescription History"
)



if prescriptions:


    for item in prescriptions:


        st.success(

f"""
Diagnosis:

{item.get('diagnosis')}


Medicines:

{item.get('medicines')}


Instructions:

{item.get('instructions')}
"""

        )


else:

    st.warning(
        "No prescriptions found"
    )



# =====================================================
# INSURANCE
# =====================================================


st.divider()


st.subheader(
"🛡 Insurance Details"
)



if insurance and "message" not in insurance:


    st.info(

f"""
Company:

{insurance.get('company')}


Policy Number:

{insurance.get('policy_number')}


Policy Type:

{insurance.get('policy_type')}


Coverage:

{insurance.get('coverage')}
"""

    )


else:

    st.warning(
        "Insurance details unavailable"
    )



# =====================================================
# FOOTER
# =====================================================


st.divider()


st.caption(
"AI Hospital Assistant | Patient Profile Management"
)