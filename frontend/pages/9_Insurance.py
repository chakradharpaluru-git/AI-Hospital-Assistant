import streamlit as st
import requests
from PIL import Image
import os


# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Insurance Assistant",
    page_icon="🛡️",
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

    color:gray;
    font-size:18px;

}


.card{

background:white;
padding:25px;
border-radius:15px;
box-shadow:0px 3px 12px rgba(0,0,0,0.1);
margin-top:20px;

}


.section{

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
    "insurance.jpg"
)



# -------------------------------------------------------
# HEADER
# -------------------------------------------------------

left,right = st.columns([2,1])


with left:


    st.markdown(
        "<div class='title'>🛡️ Insurance Assistant</div>",
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class='subtitle'>
        Upload your insurance policy and ask questions about your coverage.
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



st.write("")



# -------------------------------------------------------
# UPLOAD POLICY
# -------------------------------------------------------

st.subheader(
    "Upload Insurance Policy"
)


uploaded_file = st.file_uploader(

    "Upload Policy Document",

    type=[
        "pdf",
        "txt"
    ]

)



if uploaded_file:


    st.success(
        f"Uploaded: {uploaded_file.name}"
    )



# -------------------------------------------------------
# QUESTION
# -------------------------------------------------------

st.subheader(
    "Ask Your Insurance Question"
)



question = st.text_area(

    "",

    placeholder=
    "Example: Is knee replacement covered under my policy?"

)



# -------------------------------------------------------
# SAMPLE QUESTIONS
# -------------------------------------------------------

st.markdown(
    "<div class='section'>What You Can Ask</div>",
    unsafe_allow_html=True
)


st.write(
"""
✔ Coverage Details

✔ Claim Process

✔ Waiting Period

✔ Exclusions

✔ Premium Information

✔ Cashless Hospitals

✔ Policy Benefits

✔ Renewal Information
"""
)



# -------------------------------------------------------
# BUTTON
# -------------------------------------------------------

ask_button = st.button(

    "🤖 Ask Insurance AI",

    use_container_width=True

)



# -------------------------------------------------------
# API CALL
# -------------------------------------------------------

if ask_button:


    if question.strip()=="":


        st.warning(
            "Please enter your question."
        )


    else:


        payload = {


            "question": question

        }



        try:


            with st.spinner(
                "Analyzing insurance policy..."
            ):


                response = requests.post(


                    "http://127.0.0.1:8000/insurance/ask",


                    json=payload,


                    timeout=120


                )



            if response.status_code == 200:



                result = response.json()



                st.success(
                    " ✅ Answer Generated Successfully"
                )
                answer = result.get("answer", {})


                st.markdown(
                    "---"
                )
                
                
                st.subheader(
                    "🤖 Insurance AI Assistant"
                )



                # Handle different response formats


                if isinstance(answer,dict):


                    if "answer" in answer:
                        answer = answer["answer"]
                        
                    
                    st.markdown("### 📄 Summary")
                    st.info(answer.get("summary", "No summary available."))

                    coverage = answer.get("coverage", [])

                    if coverage:

                        st.markdown("### 🛡️ Coverage")

                        for item in coverage:

                            st.success(f"✔ {item}")


                    documents = answer.get("required_documents", [])

                    if documents:

                        st.markdown("### 📑 Required Documents")

                        for doc in documents:

                            st.write(f"📌 {doc}")



                claim = answer.get("claim_process", {})

                if claim:

                    st.markdown("### 📝 Claim Process")
                    for i,step in enumerate(claim,start=1):

                        st.write(f"**step {i}:** {step}")


                notes = answer.get("notes", "")

                if notes: 

                 sources = result.get("sources", [])

                if len(sources) > 0:

                    st.markdown("### 🗒️ sources")

                    for src in sources:

                        st.caption(src)


                else:

                    st.write(answer)

                    

                st.write(
                    response.text
                )



        except Exception as e:


            st.error(
                "Unable to connect to backend."
            )


            st.exception(e)



# -------------------------------------------------------
# INSURANCE SERVICES
# -------------------------------------------------------

st.divider()


st.markdown(
"<div class='section'>Insurance Services</div>",
unsafe_allow_html=True
)



col1,col2,col3 = st.columns(3)



with col1:


    st.success(
        """
        ✔ Policy Coverage

        ✔ Claim Eligibility

        ✔ Waiting Period
        """
    )



with col2:


    st.success(
        """
        ✔ Network Hospitals

        ✔ Cashless Treatment

        ✔ Premium Information
        """
    )



with col3:


    st.success(
        """
        ✔ Exclusions

        ✔ Renewal Guidance

        ✔ Policy Benefits
        """
    )



# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.divider()


st.info(
"""
This AI Insurance Assistant provides information from uploaded policy documents.

For legal decisions, claim approvals, or policy disputes,
consult your insurance provider or licensed insurance advisor.
"""
)