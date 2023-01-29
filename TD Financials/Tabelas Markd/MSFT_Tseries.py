import dataclasses
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'E0DBWOY6S1NS2GV5'

ts = TimeSeries(key=api_key, output_format='pandas')
['TIME_SERIES_INTRADAY'] 
meta_data: str = (symbol = 'MSFT')
print(dataclasses)

i = 1

close_data = ['4.close']
percentage_change = close_data.pct_change()

print(percentage_change)

last_change = percentage_change[-1]

if abs(last_change) > 0.0004:
    print("MSFT Alert:" + str(last_change))