import datetime
import streamlit as st
import yfinance as yf
import pandas as pd


st.title("Ativo de bolsa simples")
st.write("Dados do yahoo finance mostrando dados de fechamento e volume do Google")

tickerSimbol = "GOOGL"
tickerData = yf.Ticker(tickerSimbol)
tickerDf = tickerData.history(period='1d', start='2024-1-1', end=datetime.date.today())

st.write("""
## Preço de fechamento
""")
st.line_chart(tickerDf['Close'])

st.write("""
## Qtd papeis negociados
""")
st.line_chart(tickerDf['Volume'])