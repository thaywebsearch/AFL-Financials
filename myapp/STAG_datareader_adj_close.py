from pandas_datareader import data

stag = data.DataReader('STAG', start='2010-01-01', end='2020-12-31', data_source='yahoo')['Adj Close']

stag.plot(title='STAG Adj.Closing Price')