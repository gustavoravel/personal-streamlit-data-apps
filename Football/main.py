import base64
from datetime import datetime
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from load_data import load_data


st.title("Números dos Jogadores de futebol")
st.write("Web scrapping simples de dados dos jogadores de futebol")
st.write("""
    Dados extraídos de [Football Reference](https://fbref.com/pt/comps/24/Serie-A-Estatisticas)
""")

selected_year = st.selectbox("Selecione o ano", list(reversed(range(1999, int(datetime.now().year+1)))))

playerstats = load_data(selected_year)
