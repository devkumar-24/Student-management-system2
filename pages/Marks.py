import streamlit as st
from db import marks

st.title("📝 Marks Management")

roll = st.text_input("Roll Number")

java = st.number_input("Java")
python = st.number_input("Python")
dbms = st.number_input("DBMS")

if st.button("Save Marks"):

    marks.insert_one({
        "roll": roll,
        "java": java,
        "python": python,
        "dbms": dbms
    })

    st.success("Marks Saved")
