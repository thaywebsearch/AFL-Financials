import yfinance as yf

afl = yf.Ticker('stag')

hist = afl.history(period="max")

print(stag.history)