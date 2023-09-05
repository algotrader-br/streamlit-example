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