import streamlit as st
from db import students

st.set_page_config(page_title="Student Management System")

st.title("🎓 Student Management System")

total_students = students.count_documents({})

st.metric("Total Students", total_students)

st.info("Use the sidebar to navigate between pages.")
