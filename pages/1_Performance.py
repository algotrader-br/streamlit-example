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

st.write("# Performance Monitoring")

st.write("#### On this page we will put all the performance metrics of the strategies into action")

st.markdown('''
        For an informative and complete performance analysis of algo trading strategies
        developed by me, I provide the following metrics and views:
        1. Cumulative Return (in R$) - real account and backtest
        2. Risk/return ratios: a) [Sharpe](https://pt.wikipedia.org/wiki/%C3%8Ddice_de_Sharpe),
            b) [Sortino](https://en.wikipedia.org/wiki/Sortino_ratio),
            c) [Calm](https://www.investopedia.com/terms/c/calmarratio.asp)
        3. Strategy Drawdown
        4. Daily/Weekly Performance
        5. Percentage of winning/losing trades
        
        Note: Whenever we are talking about profit, we mean gross profit before taxes.
        For example, on day trades (as is the case with my strategies), we must pay 20% IR. Read more at:
        https://blog.nubank.com.br/darf-day-trade-2023/ 
            
        -----
            
        ''')

# Selecting the desired strategy
option_strat = st.selectbox(
    'Which Strategy would you like to select?',
    ('2-Surfing the trend', '3-Iron box'))

st.write('You selected:', option_strat)

# this parameter will be used to import some tables
strat = option_strat.split('-')[0]

### Importando json com parametros de data inicial - data final
df_params = pd.read_json(f'params_strat{strat}.json')
data_ini = df_params['data_ini'][0]
data_fim = df_params['data_fim'][0]

# Importando dados de trades reais
dfmt5_2 = pd.read_csv(f'bases/dados_real_mt5_strat{strat}.csv', index_col=['time'], parse_dates=['time'])

# Importando dados teóricos 
dft = pd.read_csv(f'bases/backtest_deploy_strat{strat}.csv', index_col=['time'], parse_dates=['time'])
# Selecionando apenas entradas
dft = dft[dft['strategy_2']!=0]
dft.columns = dft.columns + '_teo'
dft.rename(columns = {'safra_teo': 'safra'}, inplace = True)


#################################
###  1. Performance Acumulada  ###
#################################

## Plotando resultados

# Resultado real
#fig1 = px.line(dfmt5_2, x=dfmt5_2.index, y=["cstrategy_2"])
# Resultado backtest
#fig2 = px.line(dft, x=dft.index, y=["cstrategy_2_teo"], color_discrete_sequence=['red'])
# Unindo figuras
#figret = go.Figure(data = fig1.data + fig2.data)

figret = go.Figure()
figret.add_trace(go.Scatter(
    x=dfmt5_2.index,
    y=dfmt5_2["cstrategy_2"],
    name='Real'
))
figret.add_trace(go.Scatter(
    x=dft.index,
    y=dft["cstrategy_2_teo"],
    name='Backtest',
    line=dict(color="#d62728")
))

# adicionando elementos de layout
figret.update_layout(
    title = dict(text="1. Cumulative Return", font=dict(size=27), automargin=False, yref='paper'),
    xaxis_title= dict(text="<b> Data </b>", font=dict(size=20)),
    yaxis_title= dict(text="<b>Return (R$) </b>", font=dict(size=20)),
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
figret.update_layout(legend_title_text='Legend')
st.plotly_chart(figret, use_container_width=True)


st.write('As we can see above, the algorithm running on a real account adheres to the backtest results')


#################################
###  2. Indices risco/retorno  ###
#################################


#################################
###        3. Drawdown        ###
#################################

# Cálculo do drawdown
dfmt5_2['cummax'] = dfmt5_2['cstrategy_2'].cummax()
dfmt5_2["dd"] = dfmt5_2['cstrategy_2'] - dfmt5_2['cummax']
dfmt5_2["max_dd"] = dfmt5_2["dd"].cummin()

# Plotando
#figdd = px.line(dfmt5_2, x=dfmt5_2.index, y=["dd"])

figdd = go.Figure()
figdd.add_trace(go.Scatter(
    x=dfmt5_2.index,
    y=dfmt5_2["dd"],
    name='Real',
    fill='tozeroy'
))

figdd.update_layout(
    title = dict(text="3. Drawdown", font=dict(size=27), automargin=False, yref='paper'),
    xaxis_title= dict(text="<b> Data </b>", font=dict(size=20)),
    yaxis_title= dict(text="<b>Drawdown (R$) </b>", font=dict(size=20)),
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
st.plotly_chart(figdd, use_container_width=True)

st.write('We can observe a controlled drawdown without many surprises.')

#################################
###  3. Performance Diária  ###
#################################

# Concat para união do real e teórico
df = pd.concat([dfmt5_2[['lucro','cstrategy_2','comment']], dft.iloc[:,2:]], axis =1)

# Dataframe auxiliar para o plot
aux = df.resample('d').sum()
aux = aux[aux['lucro']!=0]
aux.rename(columns={'lucro':'Real', 'strategy_2_teo': 'Backtest'}, inplace = True)

# Plot
figd = px.bar(aux, x=aux.index, y=["Real",'Backtest'], barmode='group',
               color_discrete_sequence=['#1f77b4','#d62728'])

# adicionando elementos de layout
figd.update_layout(
    title = dict(text="4. Daily Return", font=dict(size=27), automargin=False, yref='paper'),
    xaxis_title= dict(text="<b> Data </b>", font=dict(size=20)),
    yaxis_title= dict(text="<b>Return (R$) </b>", font=dict(size=20)),
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
st.plotly_chart(figd, use_container_width=True)

st.write('Again, we can see the good result agreement between the real account result and the \
          expected backtest result.')

#################################
###  4. Trades vencedeores/perdedores  ###
#################################