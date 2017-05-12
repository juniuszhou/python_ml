import pandas as pd
import numpy as np

# http://pandas.pydata.org/pandas-docs/stable/timeseries.html

# it is just used as index of data frame.
data = pd.date_range("20170101", periods=3, freq='H')

ts = pd.Series(np.random.rand(len(data)), index=data)


print(ts, len(ts))

# change the frequency and fill in data for missing period.
# data from closest period
freq = ts.asfreq('30Min', method='pad')
print(freq, len(freq))

# statistics based on time series
daily_mean = ts.resample('D').mean()
print(daily_mean)
