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

st.write("#### Nesta página eu detalho como está o desempenho dos backtests")

st.markdown('''
        Antes de fazer o deploy de estratégia de *algo trading* em conta real, é preciso estudar em minúcias
        o resultado do backtest por um período de tempo relativamente longo.
            
        -----
            
        ''')

#################################
###  0. Data Prep  ###
#################################