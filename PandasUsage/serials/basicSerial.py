import numpy as np
import pandas as pd

data = pd.Series(index=range(0, 10), dtype=int)
print(data)

# set value for one item, if type not match. will change.
data[0] = 'string'
print(data[0])

data[1] = 100
print(data[1])

# set series as a column in data frame
df = pd.DataFrame()
df['a'] = data
print(df)

# WRONG set series as row in data frame
df2 = pd.DataFrame(index=range(0, 1))
df2.iloc[0] = data
print(df2)
