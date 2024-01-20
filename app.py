import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#batsman insights
batsman=pd.read_csv(r'/content/Top_100_batsman.csv')
st.title('Batsman KPIs')
Batsman_matches = batsman[batsman['Runs']>3000]#MIn 3000
topfive=(Batsman_matches['PLAYER'].iloc[0:5])
df = batsman
fig5 = px.bar(df, x=batsman['PLAYER'], y=batsman['Avg'], color=batsman['SR'])
st.plotly_chart(fig5)
st.title('Top 5 batsman based on runs')
fig6 = go.Figure()
fig6.add_trace(go.Scatter(x=topfive, y=(batsman['Runs'].iloc[0:5]),
                    mode='lines+markers',
                    name='lines+markers'))
st.plotly_chart(fig6)
