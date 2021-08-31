import yfinance as yf
import streamlit as st

st.write("""""")

tickerSymbol = 'PRU'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-12-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)