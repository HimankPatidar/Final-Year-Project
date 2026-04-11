# import streamlit as st
# import pandas as pd
# import os
# import subprocess
# from datetime import datetime

# # -----------------------------
# # PAGE CONFIG
# # -----------------------------
# st.set_page_config(page_title="Smart Attendance System", layout="wide")

# # -----------------------------
# # GLOBAL UI STYLE (STARTUP LOOK)
# # -----------------------------


# # -----------------------------
# # LOGIN SYSTEM
# # -----------------------------
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     st.markdown('<div class="title">🔐 Admin Login</div>', unsafe_allow_html=True)

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if username == "Himank" and password == "himank123":
#             st.session_state.logged_in = True
#             st.success("Login successful")
#             st.rerun()
#         else:
#             st.error("Invalid credentials")

# if not st.session_state.logged_in:
#     login()
#     st.stop()

# # -----------------------------
# # THEME INIT
# # -----------------------------
# if "theme" not in st.session_state:
#     st.session_state.theme = "light"

# # -----------------------------
# # LOAD DATA
# # -----------------------------
# if os.path.exists("students.csv"):
#     students_df = pd.read_csv("students.csv")
# else:
#     students_df = pd.DataFrame(columns=["Name","Department","Semester","Section","Gender"])

# if os.path.exists("attendance.csv"):
#     df = pd.read_csv("attendance.csv")
# else:
#     df = pd.DataFrame(columns=["Name","Date","Time"])

# # -----------------------------
# # HEADER
# # -----------------------------
# st.markdown(f'<div class="title">📸 Smart Attendance System</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">AI-powered Face Recognition Dashboard</div>', unsafe_allow_html=True)

# # -----------------------------
# # DASHBOARD CARDS
# # -----------------------------
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.markdown(f'<div class="card">👨‍🎓<h3>{len(students_df)}</h3>Total Students</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown(f'<div class="card">📅<h3>{len(df)}</h3>Total Attendance</div>', unsafe_allow_html=True)

# with col3:
#     st.markdown('<div class="card">🟢<h3>Active</h3>Status</div>', unsafe_allow_html=True)

# # -----------------------------
# # SIDEBAR
# # -----------------------------
# st.sidebar.title("📌 Menu")

# # Theme Toggle
# theme_option = st.sidebar.radio("🌗 Theme", ["light", "dark"], horizontal=True, index=0 if st.session_state.theme == "light" else 1)
# if theme_option != st.session_state.theme:
#     st.session_state.theme = theme_option
#     st.rerun()

# menu = st.sidebar.radio("Navigate", [
#     "📸 Take Attendance",
#     "📅 Attendance Records",
#     "👨‍🎓 Manage Students",
#     "📊 Analytics"
# ])

# if st.sidebar.button("🚪 Logout"):
#     st.session_state.logged_in = False
#     st.rerun()

# # Dynamic Theme CSS
# theme_css = """
# <style>
#     :root {
#         --bg-primary: #ffffff;
#         --bg-secondary: #f0f2f6;
#         --card-bg: #ffffff;
#         --text-primary: #1f1f1f;
#         --text-secondary: #6b7280;
#         --accent: #1f77b4;
#         --sidebar-bg: #0E1117;
#         --sidebar-text: #ffffff;
#         --shadow: 0 4px 20px rgba(0,0,0,0.1);
#         --button-bg: #1f77b4;
#         --button-text: white;
#         --transition: all 0.3s ease;
#     }
#     [data-theme="dark"] {
#         --bg-primary: #0a0a0a;
#         --bg-secondary: #1a1a1a;
#         --card-bg: #1e1e1e;
#         --text-primary: #ffffff;
#         --text-secondary: #d1d5db;
#         --accent: #3b82f6;
#         --sidebar-bg: #111827;
#         --sidebar-text: #f9fafb;
#         --shadow: 0 4px 20px rgba(0,0,0,0.3);
#         --button-bg: #3b82f6;
#         --button-text: white;
#     }
#     body {
#         background-color: var(--bg-primary);
#         color: var(--text-primary);
#         transition: var(--transition);
#         font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
#     }
#     .title {
#         font-size: 42px !important;
#         font-weight: bold !important;
#         color: var(--accent) !important;
#         text-align: center !important;
#         margin-bottom: 10px;
#     }
#     .subtitle {
#         text-align: center !important;
#         color: var(--text-secondary) !important;
#         margin-bottom: 20px;
#     }
#     .card {
#         padding: 20px;
#         border-radius: 15px;
#         background: var(--card-bg);
#         box-shadow: var(--shadow);
#         text-align: center;
#         color: var(--text-primary);
#         transition: var(--transition);
#         h3 { color: var(--text-primary); }
#     }
#     .stButton > button {
#         border-radius: 10px !important;
#         height: 3em !important;
#         width: 100% !important;
#         background-color: var(--button-bg) !important;
#         color: var(--button-text) !important;
#         border: none !important;
#         transition: var(--transition);
#     }
#     .stButton > button:hover {
#         transform: translateY(-2px);
#         box-shadow: 0 8px 25px rgba(31,119,180,0.4);
#     }
#     [data-testid="stSidebar"] {
#         background-color: var(--sidebar-bg) !important;
#         color: var(--sidebar-text) !important;
#     }
#     .stDataFrame {
#         background-color: var(--bg-primary);
#     }
#     .stMetric > label {
#         color: var(--text-secondary) !important;
#     }
#     .stMetric > .stMetricValue {
#         color: var(--text-primary) !important;
#     }
#     #MainMenu, footer { visibility: hidden; }
# </style>
# """

# st.markdown(f'<div data-theme="{st.session_state.theme}">{theme_css}</div>', unsafe_allow_html=True)

# # -----------------------------
# # TAKE ATTENDANCE
# # -----------------------------
# if menu == "📸 Take Attendance":

#     st.image("./JECRC-Building.jpg", width=900)

#     st.markdown("""
#     ### 🚀 Welcome
#     Smart AI system for automated attendance.

#     ✔ Contactless  
#     ✔ Secure  
#     ✔ Real-time  
#     """)

#     col1, col2, col3 = st.columns([1,2,1])

#     with col2:
#         if st.button("🚀 Start Attendance"):
#             st.warning("Press ESC to stop camera")
#             subprocess.run(["python", "recognize.py"])

# # -----------------------------
# # ATTENDANCE RECORDS
# # -----------------------------
# elif menu == "📅 Attendance Records":

#     st.subheader("Attendance Viewer")

#     option = st.selectbox("View Type", ["Today", "All", "By Date"])

#     if option == "Today":
#         today = datetime.now().strftime("%Y-%m-%d")
#         filtered = df[df["Date"] == today]

#     elif option == "All":
#         filtered = df

#     else:
#         date = st.date_input("Select Date")
#         filtered = df[df["Date"] == str(date)]

#     merged = pd.merge(filtered, students_df, on="Name", how="left")

#     st.dataframe(merged, width="stretch")

#     st.download_button("⬇ Download CSV",
#                        merged.to_csv(index=False),
#                        "attendance.csv")

# # -----------------------------
# # MANAGE STUDENTS
# # -----------------------------
# elif menu == "👨‍🎓 Manage Students":

#     st.subheader("Student Management")

#     with st.form("register_form"):
#         col1, col2 = st.columns(2)

#         with col1:
#             name = st.text_input("Name")
#             dept = st.text_input("Department")
#             gender = st.selectbox("Gender", ["Male","Female","Other"])

#         with col2:
#             sem = st.text_input("Semester")
#             section = st.text_input("Section")

#         submit = st.form_submit_button("Register")

#     if submit:
#         if name and dept and sem and section:
#             from enroll import enroll
#             result = enroll(name)

#             if result == "duplicate":
#                 st.error("Face already exists")
#             else:
#                 new_row = pd.DataFrame([[name, dept, sem, section, gender]],
#                     columns=["Name","Department","Semester","Section","Gender"])

#                 students_df = pd.concat([students_df, new_row], ignore_index=True)
#                 students_df.to_csv("students.csv", index=False)

#                 st.success("Student Registered")

#     st.markdown("### Students List")
#     st.dataframe(students_df, width="stretch")

#     if not students_df.empty:
#         selected = st.selectbox("Delete Student", students_df["Name"])

#         if st.button("Delete"):
#             students_df = students_df[students_df["Name"] != selected]
#             students_df.to_csv("students.csv", index=False)

#             file = f"encodings/{selected}.npy"
#             if os.path.exists(file):
#                 os.remove(file)

#             st.success("Deleted")

# # -----------------------------
# # ANALYTICS
# # -----------------------------
# elif menu == "📊 Analytics":

#     st.subheader("Analytics Dashboard")

#     col1, col2 = st.columns(2)
#     col1.metric("📊 Total Records", len(df))
#     avg = round(len(df) / max(len(students_df), 1), 1)
#     col2.metric("📈 Avg per Student", avg)

#     counts = df["Name"].value_counts().sort_values(ascending=False)
#     st.dataframe(counts, width="stretch")

#     st.markdown("### Low Attendance")
#     low = df["Name"].value_counts()
#     st.dataframe(low[low < 2], width="stretch")


import streamlit as st
import pandas as pd
import os
import subprocess
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Smart Attendance System", layout="wide")

# -----------------------------
# GLOBAL LIGHT UI STYLE
# -----------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    color: #1f77b4;
    text-align: center;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 20px;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    text-align: center;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    height: 3em;
    width: 100%;
    background-color: #1f77b4;
    color: white;
    border: none;
}

/* LIGHT SIDEBAR */
[data-testid="stSidebar"] {
    background-color: #f8f9fa !important;
    border-right: 1px solid #e5e7eb;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: #1f1f1f !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOGIN SYSTEM
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown('<div class="title">🔐 Admin Login</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "Himank" and password == "himank123":
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# -----------------------------
# LOAD DATA
# -----------------------------
if os.path.exists("students.csv"):
    students_df = pd.read_csv("students.csv")
else:
    students_df = pd.DataFrame(columns=["Name","Department","Semester","Section","Gender"])

if os.path.exists("attendance.csv"):
    df = pd.read_csv("attendance.csv")
else:
    df = pd.DataFrame(columns=["Name","Date","Time"])

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="title">📸 Smart Attendance System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered Face Recognition Dashboard</div>', unsafe_allow_html=True)

# -----------------------------
# DASHBOARD CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="card">👨‍🎓<h3>{len(students_df)}</h3>Total Students</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="card">📅<h3>{len(df)}</h3>Total Attendance</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">🟢<h3>Active</h3>Status</div>', unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📌 Menu")

menu = st.sidebar.radio("Navigate", [
    "📸 Take Attendance",
    "📅 Attendance Records",
    "👨‍🎓 Manage Students",
    "📊 Analytics"
])

if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()

# -----------------------------
# TAKE ATTENDANCE
# -----------------------------
if menu == "📸 Take Attendance":

    st.image("./JECRC-Building.jpg", width=900)

    st.markdown("""
    ### 🚀 Welcome
    Smart AI system for automated attendance.

    ✔ Contactless  
    ✔ Secure  
    ✔ Real-time  
    """)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if st.button("🚀 Start Attendance"):
            st.warning("Press ESC to stop camera")
            subprocess.run(["python", "recognize.py"])

# -----------------------------
# ATTENDANCE RECORDS
# -----------------------------
elif menu == "📅 Attendance Records":

    st.subheader("Attendance Viewer")

    option = st.selectbox("View Type", ["Today", "All", "By Date"])

    if option == "Today":
        today = datetime.now().strftime("%Y-%m-%d")
        filtered = df[df["Date"] == today]

    elif option == "All":
        filtered = df

    else:
        date = st.date_input("Select Date")
        filtered = df[df["Date"] == str(date)]

    merged = pd.merge(filtered, students_df, on="Name", how="left")

    st.dataframe(merged, use_container_width=True)

    st.download_button("⬇ Download CSV",
                       merged.to_csv(index=False),
                       "attendance.csv")

# -----------------------------
# MANAGE STUDENTS
# -----------------------------
elif menu == "👨‍🎓 Manage Students":

    st.subheader("Student Management")

    with st.form("register_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Name")
            dept = st.text_input("Department")
            gender = st.selectbox("Gender", ["Male","Female","Other"])

        with col2:
            sem = st.text_input("Semester")
            section = st.text_input("Section")

        submit = st.form_submit_button("Register")

    if submit:
        if name and dept and sem and section:
            from enroll import enroll
            result = enroll(name)

            if result == "duplicate":
                st.error("Face already exists")
            else:
                new_row = pd.DataFrame([[name, dept, sem, section, gender]],
                    columns=["Name","Department","Semester","Section","Gender"])

                students_df = pd.concat([students_df, new_row], ignore_index=True)
                students_df.to_csv("students.csv", index=False)

                st.success("Student Registered")

    st.markdown("### Students List")
    st.dataframe(students_df, use_container_width=True)

    if not students_df.empty:
        selected = st.selectbox("Delete Student", students_df["Name"])

        if st.button("Delete"):
            students_df = students_df[students_df["Name"] != selected]
            students_df.to_csv("students.csv", index=False)

            file = f"encodings/{selected}.npy"
            if os.path.exists(file):
                os.remove(file)

            st.success("Deleted")

# -----------------------------
# ANALYTICS
# -----------------------------
elif menu == "📊 Analytics":

    st.subheader("Analytics Dashboard")

    col1, col2 = st.columns(2)
    col1.metric("📊 Total Records", len(df))
    avg = round(len(df) / max(len(students_df), 1), 1)
    col2.metric("📈 Avg per Student", avg)

    counts = df["Name"].value_counts().sort_values(ascending=False)
    st.dataframe(counts, use_container_width=True)

    st.markdown("### Low Attendance")
    low = df["Name"].value_counts()
    st.dataframe(low[low < 2], use_container_width=True)