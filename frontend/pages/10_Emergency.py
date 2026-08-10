import streamlit as st
import requests
from PIL import Image
import os
from utils.config import BACKEND_URL

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------

st.set_page_config(
    page_title="Emergency Assistance",
    page_icon="🚑",
    layout="wide"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------

st.markdown("""
<style>

.main{
    background:#FFF5F5;
}

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.title{
    color:#C62828;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    color:#555;
    font-size:18px;
}

.card{
    background:white;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.10);
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# IMAGE PATH
# -----------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

image_path = os.path.join(
    BASE_DIR,
    "assets",
    "emergency.jpg"
)

# -----------------------------------------------------
# HEADER IMAGE
# -----------------------------------------------------

if os.path.exists(image_path):

    image = Image.open(image_path)

    st.image(
        image,
        use_container_width=True
    )

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

st.markdown(
    "<div class='title'>🚑 Emergency Assistance</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitle'>
    Get immediate AI guidance while contacting professional emergency services.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------------------------
# LAYOUT
# -----------------------------------------------------

left, right = st.columns([2,1])

# -----------------------------------------------------
# LEFT COLUMN
# -----------------------------------------------------

with left:

    st.subheader("🧑 Patient Information")

    patient_name = st.text_input(
        "Patient Name",
        placeholder="Enter patient name"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    symptoms = st.multiselect(
        "Select Emergency Symptoms",
        [
            "Chest Pain",
            "Difficulty Breathing",
            "Unconsciousness",
            "High Fever",
            "Severe Bleeding",
            "Stroke Symptoms",
            "Heart Palpitations",
            "Poisoning",
            "Burn Injury",
            "Head Injury",
            "Severe Allergic Reaction",
            "Seizure",
            "Road Accident",
            "Snake Bite"
        ]
    )

    additional_info = st.text_area(
        "Additional Information",
        placeholder="Describe the emergency situation..."
    )

    submit = st.button(
        "🚨 Get Emergency Assessment",
        use_container_width=True
    )

# -----------------------------------------------------
# RIGHT COLUMN
# -----------------------------------------------------

with right:

    st.markdown("""
<div class="card">

### ☎ Emergency Numbers

🚑 **Ambulance : 108**

👮 **Police : 100**

🔥 **Fire : 101**

🏥 **Emergency : 112**

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

### 🩺 First Aid Tips

✔ Stay Calm

✔ Call Emergency Services

✔ Keep Airway Open

✔ Stop Heavy Bleeding

✔ Monitor Breathing

✔ Keep the patient comfortable

✔ Do NOT give unknown medicines

</div>
""", unsafe_allow_html=True)


# -----------------------------------------------------
# API CALL
# -----------------------------------------------------

if submit:

    payload = {

        "patient_name": patient_name,

        "age": age,

        # Backend expects a STRING, not a list
        "symptoms": ", ".join(symptoms),

        "additional_info": additional_info

    }

    try:

        with st.spinner("Analyzing emergency condition..."):

            response = requests.post(

                f"{BACKEND_URL}/emergency/assess",

                json=payload,

                timeout=120

            )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Emergency Assessment Completed")

            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.subheader("🚨 Possible Medical Condition")

            condition = result.get(
                "possible_condition",
                "No condition available."
            )

            st.error(condition)

            st.divider()

            st.subheader("🚦 Emergency Level")

            level = result.get(
                "emergency_level",
                "Unknown"
            )

            if level.lower() == "high":

                st.error(f"🔴 {level}")

            elif level.lower() == "medium":

                st.warning(f"🟠 {level}")

            elif level.lower() == "low":

                st.success(f"🟢 {level}")

            else:

                st.info(level)

            st.divider()

            st.subheader("🩺 Immediate Guidance")

            guidance = result.get(
                "immediate_guidance",
                []
            )

            if guidance:

                for item in guidance:

                    st.write("✅", item)

            else:

                st.info("No guidance available.")




            # -------------------------------------------------
            # AMBULANCE
            # -------------------------------------------------

            st.divider()

            ambulance = result.get(
                "call_ambulance",
                False
            )

            if ambulance:

                st.error("""
🚑 **Immediate Ambulance Required**

Please call **108** immediately.

Do NOT delay seeking emergency medical care.
""")

            else:

                st.success(
                    "🚑 Ambulance is not immediately required based on the current assessment."
                )

            # -------------------------------------------------
            # RECOMMENDED DEPARTMENT
            # -------------------------------------------------

            st.divider()

            st.subheader("🏥 Recommended Department")

            department = result.get(
                "recommended_department",
                "Emergency Department"
            )

            st.info(department)

            # -------------------------------------------------
            # DISCLAIMER
            # -------------------------------------------------

            st.divider()

            st.subheader("⚠ Disclaimer")

            disclaimer = result.get(
                "disclaimer",
                "Seek professional medical care immediately."
            )

            st.warning(disclaimer)

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        else:

            st.error("❌ Backend returned an error.")

            st.code(response.text)

    except requests.exceptions.ConnectionError:

        st.error("❌ Cannot connect to FastAPI backend.")

        st.info("Start your FastAPI server using:\n\nuvicorn backend.main:app --reload")

    except requests.exceptions.Timeout:

        st.error("⏰ Request timed out.")

    except Exception as e:

        st.exception(e)                



# -----------------------------------------------------
# EMERGENCY WARNING
# -----------------------------------------------------

st.divider()

st.error("""
⚠ EMERGENCY WARNING

If the patient has any of the following:

• Unconsciousness
• Difficulty breathing
• Severe chest pain
• Symptoms of heart attack
• Stroke symptoms
• Heavy uncontrolled bleeding
• Severe burns
• Poisoning
• Snake bite

➡ Call **108** immediately.

Do NOT rely only on AI guidance during life-threatening emergencies.
""")

# -----------------------------------------------------
# IMPORTANT INFORMATION
# -----------------------------------------------------

st.info("""
🏥 This Emergency Assistant provides preliminary guidance only.

It is **NOT** a substitute for:

• Emergency Physician
• Hospital Emergency Department
• Ambulance Services
• Qualified Medical Professionals

Always seek immediate medical attention in serious emergencies.
""")

# -----------------------------------------------------
# QUICK EMERGENCY CHECKLIST
# -----------------------------------------------------

st.markdown("### 🚑 Quick Emergency Checklist")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
✅ Stay Calm

✅ Keep Patient Safe

✅ Check Consciousness
""")

with col2:

    st.success("""
✅ Call 108

✅ Monitor Breathing

✅ Stop Bleeding
""")

with col3:

    st.success("""
✅ Follow First Aid

✅ Do Not Panic

✅ Reach Hospital Quickly
""")

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------

st.divider()

st.caption("🏥 AI Hospital Assistant | Emergency Assistance Module | Version 1.0")