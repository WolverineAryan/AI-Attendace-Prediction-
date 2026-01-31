# ==================================================
# INTERN 3 - STREAMLIT DASHBOARD
# With Medium Risk Level
# ==================================================

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Attendance Risk Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Load data and model
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/final_clean_attendance_data.csv")

@st.cache_resource
def load_model():
    return joblib.load("model/attendance_risk_model.pkl")

df = load_data()
model = load_model()

# --------------------------------------------------
# Risk thresholds
# --------------------------------------------------

SAFE_LIMIT = 85
MEDIUM_LIMIT = 75

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🎓 Attendance Risk Prediction Dashboard")

st.markdown("""
### Risk Levels
- 🟢 **Safe**
- 🟡 **Medium Risk**
- 🔴 **High Risk**
""")

menu = st.sidebar.radio(
    "Select Section",
    ["Overview", "EDA Analysis", "Prediction", "High‑Risk Students"]
)

# ==================================================
# OVERVIEW
# ==================================================
if menu == "Overview":

    st.subheader("📊 Overview")

    df["Risk_Level"] = df["Attendance_Percentage"].apply(
        lambda x:
        "Safe" if x >= SAFE_LIMIT else
        "Medium" if x >= MEDIUM_LIMIT else
        "High"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", len(df))
    col2.metric("High Risk", (df["Risk_Level"] == "High").sum())
    col3.metric("Medium Risk", (df["Risk_Level"] == "Medium").sum())

    st.dataframe(df)

# ==================================================
# EDA
# ==================================================
elif menu == "EDA Analysis":
    df["Risk_Level"] = df["Attendance_Percentage"].apply(
        lambda x:
        "Safe" if x >= 85 else
        "Medium" if x >= 75 else
        "High"
    )
    st.subheader("📈 Exploratory Data Analysis")

    fig, ax = plt.subplots()
    sns.countplot(x="Risk_Level", data=df, ax=ax)
    st.pyplot(fig)


# ==================================================
# PREDICTION
# ==================================================
elif menu == "Prediction":

    st.subheader("🔍 Predict Attendance Risk")

    attendance = st.slider("Attendance Percentage", 0, 100, 75)
    late_days = st.number_input("Late Days", 0, 100, 2)
    leaves = st.number_input("Leaves", 0, 100, 1)

    discipline_score = late_days + leaves
    attendance_risk = 1 if attendance < 75 else 0

    input_df = pd.DataFrame([{
        "Attendance_Percentage": attendance,
        "Late_Days": late_days,
        "Leaves": leaves,
        "Discipline_Score": discipline_score,
        "Attendance_Risk": attendance_risk
    }])

    ml_prediction = model.predict(input_df)[0]

    # -------------------------------
    # FINAL RISK DECISION
    # -------------------------------

    if attendance >= SAFE_LIMIT:
        st.success("🟢 SAFE — Good Attendance")

    elif attendance >= MEDIUM_LIMIT:
        st.warning("🟡 MEDIUM RISK — Monitor Attendance")

    else:
        if ml_prediction == 1:
            st.error("🔴 HIGH RISK — Immediate Action Required")
        else:
            st.warning("🟡 MEDIUM RISK — Needs Monitoring")

# ==================================================
# HIGH RISK STUDENTS
# ==================================================
elif menu == "High‑Risk Students":

    df["Risk_Level"] = df["Attendance_Percentage"].apply(
        lambda x:
        "Safe" if x >= SAFE_LIMIT else
        "Medium" if x >= MEDIUM_LIMIT else
        "High"
    )

    high_risk_df = df[df["Risk_Level"] == "High"]

    st.subheader("🚨 High‑Risk Students")
    st.dataframe(high_risk_df)

    st.download_button(
        "⬇️ Download High‑Risk List",
        high_risk_df.to_csv(index=False),
        "high_risk_students.csv",
        "text/csv"
    )
