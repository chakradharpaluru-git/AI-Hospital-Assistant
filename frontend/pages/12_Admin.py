import streamlit as st
import requests
import pandas as pd
import plotly.express as px


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛡️",
    layout="wide"
)


# =====================================================
# CONFIG
# =====================================================

BACKEND_URL = "http://127.0.0.1:8000"


# =====================================================
# CSS
# =====================================================

st.markdown(
"""
<style>

.main{
    background:#F6F9FC;
}


.title{

font-size:36px;
font-weight:bold;
color:#0B5394;

}


.card{

background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 3px 10px rgba(0,0,0,0.1);

}


</style>

""",
unsafe_allow_html=True
)



# =====================================================
# API FUNCTIONS
# =====================================================


def api_get(endpoint):

    try:

        response = requests.get(

            f"{BACKEND_URL}{endpoint}",

            timeout=30

        )


        if response.status_code == 200:

            return response.json()


        else:

            st.error(response.text)

            return []


    except Exception as e:

        st.error(
            "Backend connection failed"
        )

        return []



# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title(
    "🛡 Admin Panel"
)


page = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",

        "Users",

        "Appointments",

        "Reports",

        "Analytics"

    ]

)



# =====================================================
# HEADER
# =====================================================


st.markdown(

"<div class='title'>🏥 Hospital Admin Dashboard</div>",

unsafe_allow_html=True

)


st.write("")



# =====================================================
# DASHBOARD
# =====================================================


if page == "Dashboard":


    analytics = api_get(
        "/admin/analytics"
    )


    col1,col2,col3 = st.columns(3)



    with col1:

        st.markdown(
        f"""

<div class="card">

<h2>👥 Users</h2>

<h1>{analytics.get('total_users',0)}</h1>


</div>

""",

        unsafe_allow_html=True

        )



    with col2:


        st.markdown(
        f"""

<div class="card">

<h2>📅 Appointments</h2>

<h1>{analytics.get('total_appointments',0)}</h1>

</div>

""",

        unsafe_allow_html=True

        )



    with col3:


        st.markdown(
        f"""

<div class="card">

<h2>📄 Reports</h2>

<h1>{analytics.get('total_reports',0)}</h1>

</div>

""",

        unsafe_allow_html=True

        )





# =====================================================
# USERS
# =====================================================


elif page == "Users":


    st.subheader(
        "👥 User Management"
    )


    users = api_get(
        "/admin/users"
    )


    if users:


        df = pd.DataFrame(users)


        st.dataframe(

            df,

            width="stretch"

        )


    else:

        st.info(
            "No users found"
        )





# =====================================================
# APPOINTMENTS
# =====================================================


elif page == "Appointments":


    st.subheader(
        "📅 Appointment Management"
    )


    appointments = api_get(

        "/admin/appointments"

    )



    if appointments:


        df = pd.DataFrame(
            appointments
        )


        st.dataframe(

            df,

            width="stretch"

        )


    else:


        st.info(
            "No appointments found"
        )





# =====================================================
# REPORTS
# =====================================================


elif page == "Reports":


    st.subheader(
        "📄 Medical Reports"
    )


    reports = api_get(

        "/admin/reports"

    )


    if reports:


        df = pd.DataFrame(
            reports
        )


        st.dataframe(

            df,

            width="stretch"

        )


    else:


        st.info(
            "No reports found"
        )





# =====================================================
# ANALYTICS
# =====================================================


elif page == "Analytics":


    st.subheader(
        "📊 Hospital Analytics"
    )


    analytics = api_get(

        "/admin/analytics"

    )


    data = pd.DataFrame(

        {

        "Category":[

            "Users",

            "Appointments",

            "Reports"

        ],


        "Count":[

            analytics.get(
                "total_users",
                0
            ),

            analytics.get(
                "total_appointments",
                0
            ),

            analytics.get(
                "total_reports",
                0
            )

        ]

        }

    )



    fig = px.bar(

        data,

        x="Category",

        y="Count",

        title="Hospital Statistics"

    )


    st.plotly_chart(

        fig,

        width="stretch"

    )



# =====================================================
# FOOTER
# =====================================================


st.divider()


st.caption(
"AI Hospital Assistant | Admin Management System"
)