import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv('/home/junius/mygit/python/Data/sample.csv'))

print(df.icol())
print(df.ix[:, :])
print(df.ix[:, :].values.astype('str'))

print(df.ix[:, :].values)

print(df.describe())

np.linalg.eigvals(df.apply(pd.to_numeric, errors='coerce').fillna(0))

