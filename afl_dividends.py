import yfinance as yf

afl = yf.Ticker('afl')

print(afl.dividends)