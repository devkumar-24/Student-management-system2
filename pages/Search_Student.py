import streamlit as st
from db import students

st.title("🔍 Search Student")

roll = st.text_input(
    "Roll Number"
)

if st.button("Search"):

    student = students.find_one(
        {"roll": roll},
        {"_id": 0}
    )

    if student:
        st.json(student)
    else:
        st.error("Not Found")
