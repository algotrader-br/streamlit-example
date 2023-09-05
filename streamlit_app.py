#################################
### Importando as bibliotecas ###
#################################

import numpy as np
import datetime as dt
import pandas as pd
import streamlit as st

st.write("# Bem-vindo à página de resultados do AlgoTrader BR! 👋")
st.sidebar.success("Selecione a página acima")

st.markdown(
    """
    ## Introdução

    Nesta página você poderá encontrar os resultados dos meus trades diários em
    **conta real**! A ideia é que a atualização seja quase em *real-time*.     

    Atualmente meus sistemas de **algo trading** são especializados em *day trade* para o mini-indice (**WINFUT**), onde
    os trades são executados de forma **100% automatizadas** utilizando o MetaTrader 5.

   👈 Selecione a página ao lado para obter as informações que você deseja.
    Seja informações de **performance** (backtest e/ou real), **estatísticas dos trades** (e.g. ganhos/perdas),
    e também o detalhamento das **diferenças de backtest e conta real**.

    ### Quer aprender mais?

    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
      forums](https://discuss.streamlit.io)

    ### Contato

    - Dúvidas e sugestões, por favor entrar em contato pelo e-mail: algotraderbr@gmail.com

"""
)