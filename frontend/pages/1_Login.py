import streamlit as st
import requests
import base64
import time
import os
from utils.config import BACKEND_URL

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Hospital Assistant - Login",
    page_icon="🏥",
    layout="centered"
)


# =====================================================
# BACKEND API URL
# =====================================================





LOGIN_API_URL = f"{BACKEND_URL}/auth/login"

# =====================================================
# IMAGE PATHS
# =====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)


LOGO_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "logo.png"
)


BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "hospital_bg.jpg"
)



# =====================================================
# SET BACKGROUND IMAGE
# =====================================================

def set_background(image_path):

    if os.path.exists(image_path):

        with open(image_path, "rb") as image:

            encoded_image = base64.b64encode(
                image.read()
            ).decode()


        background_css = f"""
<style>

/* =====================================================
   BACKGROUND
===================================================== */

.stApp {{

    background-image:
        linear-gradient(
            rgba(0,0,0,0.45),
            rgba(0,0,0,0.45)
        ),
        url("data:image/jpg;base64,{encoded_image}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* =====================================================
   MAIN CONTENT
===================================================== */

.main .block-container {{
    background: rgba(255,255,255,0.95);
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.35);
    margin-top: 30px;
}}

/* =====================================================
   HEADINGS
===================================================== */

h1 {{
    color: #1565C0 !important;
    text-align: center;
}}

h2, h3 {{
    color: #1565C0 !important;
}}

p {{
    color: #222222 !important;
}}

label {{
    color: #000000 !important;
    font-weight: 600 !important;
}}

/* =====================================================
   INPUT BOXES
===================================================== */

.stTextInput input {{
    background-color: white !important;
    color: black !important;
    border: 2px solid #1565C0 !important;
    border-radius: 8px;
}}

.stTextInput input::placeholder {{
    color: gray !important;
}}

/* =====================================================
   CHECKBOX
===================================================== */

.stCheckbox label {{
    color: black !important;
    font-weight: 600;
}}

/* =====================================================
   BUTTON
===================================================== */

.stButton > button {{
    width: 100%;
    background: #1565C0;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    height: 48px;
    border: none;
}}

.stButton > button:hover {{
    background: #0D47A1;
    color: white;
}}

/* =====================================================
   CAPTION
===================================================== */

[data-testid="stCaptionContainer"] {{
    color: #444444 !important;
}}

</style>
"""
        st.markdown(
            background_css,
            unsafe_allow_html=True
        )


    else:

        st.warning(
            "Background image not found"
        )



# Load background

set_background(
    BACKGROUND_PATH
)



# =====================================================
# SESSION STATE
# =====================================================

if "jwt_token" not in st.session_state:

    st.session_state.jwt_token = None



if "logged_in" not in st.session_state:

    st.session_state.logged_in = False




# =====================================================
# LOGIN PAGE UI
# =====================================================


# Center layout

left, center, right = st.columns(
    [1,2,1]
)



with center:


    # -------------------------------
    # Hospital Logo
    # -------------------------------

    if os.path.exists(LOGO_PATH):

        st.image(
            LOGO_PATH,
            width=120
        )

    else:

        st.write("🏥")



    st.title(
        "AI Hospital Assistant"
    )


    st.write(
        "Smart Healthcare Management System"
    )


    st.divider()



    # -------------------------------
    # Login Form
    # -------------------------------


    st.subheader(
        "🔐 Login"
    )


    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )


    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )


    show_password = st.checkbox(
        "Show Password"
    )


    if show_password:

        password = st.text_input(
            "Password",
            value=password,
            type="default"
        )



    st.write("")



    login_button = st.button(
        "Login",
        use_container_width=True
    )




    # =================================================
    # LOGIN API CALL
    # =================================================


    if login_button:


        if email == "" or password == "":


            st.error(
                "Please enter email and password"
            )


        else:


            try:


                with st.spinner(
                    "Logging in..."
                ):


                    response = requests.post(

                        LOGIN_API_URL,

                        json={

                            "email": email,

                            "password": password

                        },

                        timeout=10

                    )



                    time.sleep(1)



                # ----------------------------
                # Success Response
                # ----------------------------

                if response.status_code == 200:


                    data = response.json()



                    token = (
                        data.get("access_token")
                        or
                        data.get("token")
                    )



                    if token:


                        st.session_state.jwt_token = token


                        st.session_state.logged_in = True



                        st.success(
                            "Login Successful 🎉"
                        )



                        time.sleep(2)



                        st.switch_page(
                            "pages/3_Dashboard.py"
                        )



                    else:


                        st.error(
                            "JWT token missing in response"
                        )



                # ----------------------------
                # Invalid Login
                # ----------------------------

                else:


                    try:

                        error_data = response.json()


                        error_message = (
                            error_data.get("detail")
                            or
                            "Invalid email or password"
                        )


                    except:


                        error_message = (
                            "Invalid email or password"
                        )



                    st.error(
                        error_message
                    )



            except requests.exceptions.ConnectionError:


                st.error(
                    "Backend server is not running"
                )



            except requests.exceptions.Timeout:


                st.error(
                    "Server timeout. Try again."
                )



            except Exception as e:


                st.error(
                    f"Error: {e}"
                )



    st.divider()


    st.caption(
        "© 2026 AI Hospital Assistant | Secure Healthcare Platform"
    )