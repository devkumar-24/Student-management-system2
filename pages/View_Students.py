import streamlit as st
import pandas as pd
from db import students

st.title("📋 Student Records")

data = list(
    students.find({}, {"_id": 0})
)

if data:
    st.dataframe(pd.DataFrame(data))
else:
    st.warning("No Data Found")
