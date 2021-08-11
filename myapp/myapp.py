import yfinance as yf
import streamlit as st
from yfinance import ticker

st.write("""
#Simple Stock Price App

shown are the stock closing price and volume of Aflac!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AFL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period ='1y', start='2020-1-1', end='2020-12-31')
# Open High Low Close Volume Dividends  Stock splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

