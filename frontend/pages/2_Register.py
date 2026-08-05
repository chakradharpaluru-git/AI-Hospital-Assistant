import streamlit as st
import requests
import base64
from pathlib import Path

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Register | AI Hospital Assistant",
    page_icon="🏥",
    layout="centered"
)

# ==========================================================
# BACKEND API
# ==========================================================

API_URL = "http://127.0.0.1:8000"

# ==========================================================
# BACKGROUND IMAGE
# ==========================================================

def set_background(image_file):

    image_path = Path(__file__).parent.parent / "assets" / image_file

    if image_path.exists():

        with open(image_path, "rb") as img:
            encoded = base64.b64encode(img.read()).decode()

        st.markdown(
            f"""
            <style>

            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            </style>
            """,
            unsafe_allow_html=True,
        )

set_background("hospital_bg.jpg")

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Dark overlay */

.stApp::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.45);
    z-index:-1;
}

/* White inputs */

input{
    background:white !important;
    color:black !important;
}

/* Labels */

label{
    color:white !important;
    font-weight:bold;
}

/* Buttons */

.stButton>button{
    width:100%;
    height:48px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

/* Titles */

.title{
    text-align:center;
    color:white;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:18px;
    margin-bottom:25px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOGO
# ==========================================================

logo_path = Path(__file__).parent.parent / "assets" / "logo.png"

if logo_path.exists():
    st.image(str(logo_path), width=120)

# ==========================================================
# TITLE
# ==========================================================

st.markdown(
    '<p class="title">🏥 AI Hospital Assistant</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="subtitle">Create Your Account</p>',
    unsafe_allow_html=True,
)

st.write("")

# ==========================================================
# REGISTER FORM
# ==========================================================

with st.container():

    full_name = st.text_input(
        "Full Name",
        placeholder="Enter your full name"
    )

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    show_password = st.checkbox("Show Password")

    password = st.text_input(
        "Password",
        type="default" if show_password else "password",
        placeholder="Enter password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="default" if show_password else "password",
        placeholder="Re-enter password"
    )

    st.write("")

    if st.button(
        "📝 Register",
        use_container_width=True,
        type="primary"
    ):

        # -----------------------------
        # Validation
        # -----------------------------

        if not full_name:
            st.error("Full Name is required.")

        elif not email:
            st.error("Email is required.")

        elif not password:
            st.error("Password is required.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        else:

            payload = {
                "full_name": full_name,
                "email": email,
                "password": password
            }

            try:

                with st.spinner("Creating your account..."):

                    response = requests.post(
                        f"{API_URL}/auth/register",
                        json=payload,
                        timeout=20
                    )

                if response.status_code in [200, 201]:

                    st.success("✅ Registration Successful!")

                    st.balloons()

                    st.info(
                        "Go to the Login page from the sidebar and sign in."
                    )

                else:

                    try:
                        error = response.json()

                        if "detail" in error:
                            st.error(error["detail"])
                        else:
                            st.error(error)

                    except Exception:
                        st.error(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to FastAPI server.\n\n"
                    "Run:\n"
                    "uvicorn backend.main:app --reload"
                )

            except Exception as e:

                st.error(str(e))

st.write("")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("Already have an account?")

with col2:

    if st.button(
        "🔐 Go to Login",
        use_container_width=True
    ):
        st.switch_page("pages/1_Login.py")