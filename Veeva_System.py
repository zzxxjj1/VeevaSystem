import streamlit as st
import pandas as pd
import numpy as np

st.title("""Veeva System""")
prescriber_df = pd.read_csv("Prescriber_Data.csv")

doctor_names = prescriber_df['first_name'] + ' ' + prescriber_df['last_name']

doctors_selectbox = st.selectbox(
    'Select a doctor',
    doctor_names
)
#st.write('Doctor: ', doctors_selectbox)