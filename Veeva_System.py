import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#from sklearn.linear_model import linearRegression

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

product_name = ['Cholecap', 'Zap-a-Pain', 'Nasalclear', 'Nova-itch']
product_box = st.selectbox(
    'Select a product',
    product_name
)

def make_product_hist(product_name):
    product_grouped = prescriber_df.groupby(prescriber_df.Product)
    p_name = product_grouped.get_group(product_name)
    month = ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6']
    total_NRx_1 = 0
    total_NRx_2 = 0
    total_NRx_3 = 0
    total_NRx_4 = 0
    total_NRx_5 = 0
    total_NRx_6 = 0
    total_TRx_1 = 0
    total_TRx_2 = 0
    total_TRx_3 = 0
    total_TRx_4 = 0
    total_TRx_5 = 0
    total_TRx_6 = 0
    for row in p_name.iterrows():
        total_NRx_1 += row[1][5]
        total_NRx_2 += row[1][6]
        total_NRx_3 += row[1][7]
        total_NRx_4 += row[1][8]
        total_NRx_5 += row[1][9]
        total_NRx_6 += row[1][10]
        total_TRx_1 += row[1][11]
        total_TRx_2 += row[1][12]
        total_TRx_3 += row[1][13]
        total_TRx_4 += row[1][14]
        total_TRx_5 += row[1][15]
        total_TRx_6 += row[1][16]
    NRx = np.array([total_NRx_1, total_NRx_2, total_NRx_3, total_NRx_4, total_NRx_5, total_NRx_6])
    TRx = np.array([total_TRx_1, total_TRx_2, total_TRx_3, total_TRx_4, total_TRx_5, total_TRx_6])
    fig = go.Figure(
        data=[
            go.Bar(name='NRx', x=month, y=NRx, yaxis='y', offsetgroup=1),
            go.Bar(name='TRx', x=month, y=TRx, yaxis='y2', offsetgroup=2)
        ],
        layout={
            'yaxis': {'title': 'NRx axis'},
            'yaxis2': {'title': 'TRx axis', 'overlaying': 'y', 'side': 'right'}
        }
    )
    fig.update_layout(barmode='group')
    return fig

product_fig = make_product_hist(product_box)
st.plotly_chart(product_fig, use_container_width=True)
