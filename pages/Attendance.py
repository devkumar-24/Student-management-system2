import streamlit as st
from db import attendance

st.title("📅 Attendance")

roll = st.text_input("Roll Number")

status = st.radio(
    "Status",
    ["Present", "Absent"]
)

if st.button("Submit"):

    attendance.insert_one({
        "roll": roll,
        "status": status
    })

    st.success("Attendance Saved")
