import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("""Veeva System""")
prescriber_df = pd.read_csv("Prescriber_Data.csv")

doctor_names = prescriber_df['first_name'] + ' ' + prescriber_df['last_name']

doctors_selectbox = st.selectbox(
    'Select a doctor',
    doctor_names
)
#st.write('Doctor: ', doctors_selectbox)
def locate_row(name):
    first_name, last_name = name.split()
    for row in prescriber_df.iterrows():
        if (first_name == row[1][1]) and (last_name == row[1][2]):
            return row[1][0]




def make_hist(id):
  doctor_NRx = prescriber_df.iloc[id-1, 5:11]
  doctor_NRx = doctor_NRx.to_numpy()
  doctor_TRx = prescriber_df.iloc[id-1, 11:]
  doctor_TRx = doctor_TRx.to_numpy()
  month = ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6']
  fig = go.Figure(
      data = [
              go.Bar(name = 'NRx', x = month, y = doctor_NRx, yaxis='y', offsetgroup = 1),
              go.Bar(name = 'TRx', x = month, y = doctor_TRx, yaxis='y2', offsetgroup =2)
      ],
      layout ={
          'yaxis' : {'title': 'NRx axis'},
          'yaxis2' : {'title' :'TRx axis', 'overlaying': 'y', 'side': 'right'}
      }
  )
  fig.update_layout(barmode='group')
  return fig

index = locate_row(doctors_selectbox)
doctor_fig = make_hist(index)
st.plotly_chart(doctor_fig, use_container_width=True)