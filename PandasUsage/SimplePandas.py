import pandas as pd
import numpy as np


def if_positive(x):
    if x['A'] > 0:
        return x

dates = pd.date_range('20160101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

for column in df.columns:
    print(column)
df2 = pd.DataFrame()


for row in df.ix[:, :].values:
    print(row)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
print(df)
print('after apply data to df (((((((((((((((((((')
print(df.apply(if_positive, axis=1).dropna())
print('data will be ))))))))))))))))))))))')
print(df)

