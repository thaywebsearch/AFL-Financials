import yfinance as yf
import streamlit as st

st.write("""Shown are the stock **closing price** and ***volume*** of Aflac!""")

tickerSymbol = 'AFL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)