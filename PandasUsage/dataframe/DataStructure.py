import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create series object via a list and get its element
s = pd.Series([1, 2, 3])
print(s.get(0), s.get(1), s.get(2))
print(s[0:])


# create data frame via numpy array.
dates = pd.date_range('20160101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)


# check data in data frame
df.head()
df.tail()

print("---------- Index ---------")
print(df.index)
print("---------- Columns ---------")
print(df.columns)
print("---------- Values ---------")
print(df.values)

# get a column. name is A
print(df.A)
print(df['A'])
# illegal can't slice from column direction.
# print(df['A':'D'])

# get a row or several rows
print(df[0:3])
print(df['20160102':'20160104'])

# get a block
print(df.iloc[3])
print(df.iloc[:, :])
print(df.iloc[1:2, 2:3])
print(df.iloc[[1, 2, 4], [0, 1]])

# get block via filter
print(df[df.A > 0])
print(df[df > 0])

# sort by index or value
df.sort_index()
df.sort_values(by='A')

