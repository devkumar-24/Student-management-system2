import streamlit as st
from db import students

st.title("🗑 Delete Student")

roll = st.text_input(
    "Enter Roll Number"
)

if st.button("Delete"):

    result = students.delete_one(
        {"roll": roll}
    )

    if result.deleted_count:
        st.success("Deleted")
    else:
        st.error("Student Not Found")
