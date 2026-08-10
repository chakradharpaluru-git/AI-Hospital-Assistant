import streamlit as st
import requests
from PIL import Image
import os
from utils.config import BACKEND_URL

# ---------------------------------------------
# PAGE CONFIG
# ---------------------------------------------

st.set_page_config(
    page_title="Medical RAG Assistant",
    page_icon="🤖",
    layout="wide"
)



# ---------------------------------------------
# CSS
# ---------------------------------------------

st.markdown("""
<style>


.main{
    background:#F5F9FF;
}


.title{

font-size:38px;
font-weight:700;
color:#0B5394;

}


.card{

background:white;
padding:25px;
border-radius:15px;
box-shadow:0 3px 12px rgba(0,0,0,0.1);
margin-bottom:20px;

}


.answer-title{

font-size:24px;
font-weight:bold;
color:#0B5394;

}


.sample{

background:#EAF3FF;
padding:10px;
border-radius:8px;

}


</style>

""",
unsafe_allow_html=True)



# ---------------------------------------------
# IMAGE
# ---------------------------------------------

BASE_DIR=os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


image_path=os.path.join(
    BASE_DIR,
    "assets",
    "medical_rag.jpg"
)



# ---------------------------------------------
# HEADER
# ---------------------------------------------


col1,col2=st.columns([2,1])


with col1:

    st.markdown(
    """
    <div class="title">
    🤖 AI Medical RAG Assistant
    </div>
    """,
    unsafe_allow_html=True
    )


    st.write(
    """
    Ask medical questions using our AI Retrieval-Augmented Generation system.
    
    Knowledge Base:
    - WHO Guidelines
    - Drug Manuals
    - Medical Books
    - Hospital SOPs
    """
    )



with col2:

    if os.path.exists(image_path):

        img=Image.open(image_path)

        st.image(
            img,
            use_container_width=True
        )



# ---------------------------------------------
# SAMPLE QUESTIONS
# ---------------------------------------------


st.subheader(
    "💡 Sample Questions"
)


questions=[

"What are the symptoms of diabetes?",

"What are the causes of hypertension?",

"What are the side effects of Paracetamol?",

"Explain pneumonia symptoms and treatment.",

"What are WHO guidelines for infection prevention?",

"What tests are required for diabetes diagnosis?",

"What are the warning signs of stroke?"

]


for q in questions:

    st.markdown(
        f"""
        <div class="sample">
        {q}
        </div>
        """,
        unsafe_allow_html=True
    )



# ---------------------------------------------
# CHAT MEMORY
# ---------------------------------------------


if "messages" not in st.session_state:

    st.session_state.messages=[]



# ---------------------------------------------
# DISPLAY CHAT
# ---------------------------------------------


for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.write(
            msg["content"]
        )



# ---------------------------------------------
# INPUT
# ---------------------------------------------


question=st.chat_input(
    "Ask your medical question..."
)



if question:


    st.session_state.messages.append(

        {
            "role":"user",
            "content":question
        }

    )



    with st.chat_message("user"):

        st.write(question)



    with st.chat_message("assistant"):


        with st.spinner(
            "Searching medical knowledge base..."
        ):


            try:


                response=requests.post(

                    f"{BACKEND_URL}/rag/ask",

                    json={

                        "question":question

                    },

                    timeout=120

                )



                if response.status_code==200:


                    data=response.json()



                    # ------------------------------
                    # FORMAT RESPONSE
                    # ------------------------------


                    if isinstance(data,dict) and "answer" in data:

                        answer=data["answer"]

                    else:

                        answer=data



                    if isinstance(answer,dict):


                        st.markdown(
                        """
                        <div class="card">
                        """,
                        unsafe_allow_html=True
                        )


                        st.markdown(
                        "### 🩺 Medical Summary"
                        )


                        st.write(
                            answer.get(
                                "summary",
                                "No summary"
                            )
                        )



                        st.markdown(
                        "### 📌 Key Guidelines"
                        )


                        for item in answer.get(
                            "key_guidelines",
                            []
                        ):

                            st.write(
                                "✅",
                                item
                            )



                        st.markdown(
                        "### 💊 Medications"
                        )


                        meds=answer.get(
                            "medications",
                            []
                        )


                        if meds:

                            for m in meds:

                                st.write(
                                    "💊",
                                    m
                                )

                        else:

                            st.write(
                                "No medications mentioned"
                            )



                        st.markdown(
                        "### ⚠️ Precautions"
                        )


                        for p in answer.get(
                            "precautions",
                            []
                        ):

                            st.write(
                                "⚠️",
                                p
                            )



                        st.markdown(
                        "### 👨‍⚕️ When to consult doctor"
                        )


                        st.info(
                            answer.get(
                                "when_to_consult_doctor",
                                "Consult doctor if required"
                            )
                        )


                        st.markdown(
                        "</div>",
                        unsafe_allow_html=True
                        )



                        final_answer=str(answer)



                    else:

                        st.write(answer)

                        final_answer=str(answer)



                    st.session_state.messages.append(

                        {
                            "role":"assistant",
                            "content":final_answer
                        }

                    )



                else:

                    st.error(
                        response.text
                    )



            except Exception as e:

                st.error(
                    "Backend connection error"
                )

                st.exception(e)



# ---------------------------------------------
# CLEAR CHAT
# ---------------------------------------------


if st.button(
    "🗑 Clear Chat"
):

    st.session_state.messages=[]

    st.rerun()