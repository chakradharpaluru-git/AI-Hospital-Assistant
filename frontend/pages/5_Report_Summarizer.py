import streamlit as st
import requests
from PIL import Image
import os


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Medical Report Summarizer",
    page_icon="📄",
    layout="wide"
)


# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    background:#F5F9FF;
}

.block-container{
    padding-top:1rem;
}

.title{
    font-size:36px;
    font-weight:bold;
    color:#0B5394;
}

.subtitle{
    color:gray;
    font-size:18px;
}

.card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.section-title{
    color:#0B5394;
    font-size:22px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)



# ---------------------------------------------------
# IMAGE PATH
# ---------------------------------------------------

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


image_path = os.path.join(
    BASE_DIR,
    "assets",
    "report.jpg"
)



# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<div class='title'>📄 Medical Report Summarizer</div>",
    unsafe_allow_html=True
)


st.markdown(
    "<div class='subtitle'>Upload a medical report to receive an AI-generated summary.</div>",
    unsafe_allow_html=True
)


st.write("")



left, right = st.columns([2,1])



# ---------------------------------------------------
# UPLOAD SECTION
# ---------------------------------------------------

with left:

    uploaded_file = st.file_uploader(
        "Upload Medical Report",
        type=[
            "pdf",
            "txt"
        ]
    )


    analyze = st.button(
        "📄 Analyze Report",
        use_container_width=True
    )



# ---------------------------------------------------
# IMAGE SECTION
# ---------------------------------------------------

with right:

    if os.path.exists(image_path):

        img = Image.open(image_path)

        st.image(
            img,
            use_container_width=True
        )



# ---------------------------------------------------
# API CALL
# ---------------------------------------------------

if analyze:


    if uploaded_file is None:

        st.warning(
            "Please upload a report first."
        )


    else:


        with st.spinner(
            "Analyzing medical report..."
        ):


            try:


                files = {

                    "file":
                    (
                        uploaded_file.name,
                        uploaded_file,
                        uploaded_file.type
                    )

                }



                response = requests.post(

                    "http://127.0.0.1:8000/medical-report/summarize",

                    files=files,

                    timeout=120

                )



                if response.status_code == 200:


                    result = response.json()



                    st.success(
                        "Analysis Completed Successfully"
                    )


                    st.divider()



                    # ---------------------------------
                    # DISPLAY BACKEND ANALYSIS
                    # ---------------------------------


                    st.markdown(

                        "<div class='section-title'>Medical Report Analysis</div>",

                        unsafe_allow_html=True

                    )


                    analysis = result.get(

                        "analysis",

                        "No analysis available."

                    )



                    st.markdown(

                    f"""

                    <div class="card">

                    {analysis}

                    </div>

                    """,

                    unsafe_allow_html=True

                    )



                    # ---------------------------------
                    # FILE NAME
                    # ---------------------------------

                    st.markdown(

                    "<div class='section-title'>Uploaded File</div>",

                    unsafe_allow_html=True

                    )


                    st.info(

                        result.get(
                            "filename",
                            "Unknown"
                        )

                    )




                else:


                    st.error(
                        "Backend returned an error"
                    )


                    st.write(
                        response.text
                    )



            except Exception as e:


                st.error(
                    "Unable to connect to backend"
                )


                st.exception(e)




# ---------------------------------------------------
# INFORMATION
# ---------------------------------------------------

st.divider()


st.subheader(
    "About This Feature"
)



st.info(
"""
This AI-powered feature extracts important medical information from uploaded reports.

The generated summary is intended for informational purposes only and should not replace advice from a qualified healthcare professional.
"""
)