import streamlit as st
from db import students

st.title("➕ Add Student")

name = st.text_input("Name")
roll = st.text_input("Roll Number")
course = st.selectbox(
    "Course",
    ["BCA", "BBA", "MCA", "MBA"]
)

email = st.text_input("Email")

if st.button("Save Student"):

    students.insert_one({
        "name": name,
        "roll": roll,
        "course": course,
        "email": email
    })

    st.success("Student Added Successfully")
