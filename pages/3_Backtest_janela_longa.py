#################################
### Importando as bibliotecas ###
#################################

import numpy as np
import datetime as dt
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

#################################
###       Preâmbulo       ###
#################################

st.write("# Backtests")

st.write("#### On this page I detail how the backtests are performing in the long run")

st.markdown('''
        
        Before deploying an *algo trading* strategy on a real account, it is necessary to study in detail
        the backtest result for a relatively long period of time.
                        
        -----
            
        ''')

#################################
###  0. Data Prep  ###
#################################

# Importando backtest
df = pd.read_csv('bases/sol_6_5m_full.csv', index_col=['time'], parse_dates=['time'])
df = df.dropna()


#################################
###  1. Plot Resultado  ###
#################################


figback = go.Figure()
figback.add_trace(go.Scatter(
    x=df.index,
    y=df["cstrategy"],
    name='Backtest'
))

# adicionando elementos de layout
figback.update_layout(
    title = dict(text="1. Retorno Acumulado", font=dict(size=27), automargin=False, yref='paper'),
    xaxis_title= dict(text="<b> Data </b>", font=dict(size=20)),
    yaxis_title= dict(text="<b>Retorno (R$) </b>", font=dict(size=20)),
    font_family="Arial",
    font_color="black",
    title_font_family="Arial",
    title_font_color="black",
    legend_title_font_color="green",
    showlegend=True,
    autosize=False,
    width=800,
    height=500,
    
    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=15,
            color='black',
        ),
    ),
    yaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        linecolor='white',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=15,
            color='black',
        ),
    )
)

# Plot!
figback.update_layout(legend_title_text='Legend')
st.plotly_chart(figback, use_container_width=True)
