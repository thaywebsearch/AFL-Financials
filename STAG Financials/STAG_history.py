import yfinance as yf

stag = yf.Ticker('stag')

hist = stag.history(period="max")

print(stag.history)