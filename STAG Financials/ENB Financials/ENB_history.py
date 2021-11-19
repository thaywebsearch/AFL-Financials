import yfinance as yf

enb = yf.Ticker('enb')

hist = enb.history(period="max")

print(enb.history)