import yfinance as yf

stag = yf.Ticker('enb')

hist = stag.history(period="max")

print(stag.history)