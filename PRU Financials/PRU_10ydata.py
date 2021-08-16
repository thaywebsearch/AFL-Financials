import yfinance as yf
import pandas as pd

yf.download('PRU', period='10y')

pru = yf.download('PRU', period='10y')

pru.head()

pru['Adj Close'].plot(figsize=[10,5], legend=True),
