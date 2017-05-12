import pandas as pd
import numpy as np

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

# get a multi dimension tuple via zip
tuples = list(zip(*arrays))

# generate multi index, its data from tuple list
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

# generate data and attach multi index to it.
pd.Series(np.random.randn(8), index=index)
