import streamlit as st
from db import students

st.title("✏ Update Student")

roll = st.text_input("Roll Number")

student = students.find_one({"roll": roll})

if student:

    name = st.text_input(
        "Name",
        student["name"]
    )

    course = st.text_input(
        "Course",
        student["course"]
    )

    email = st.text_input(
        "Email",
        student["email"]
    )

    if st.button("Update"):

        students.update_one(
            {"roll": roll},
            {
                "$set": {
                    "name": name,
                    "course": course,
                    "email": email
                }
            }
        )

        st.success("Updated Successfully")
