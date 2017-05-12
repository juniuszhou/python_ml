import pandas as pd
import numpy as np

# get data frame from dict.
aa = {'one': [1, 2, 3], 'two': [2, 3, 4], 'three': [3, 4, 5]}
bb = pd.DataFrame(aa)
print(bb)

# set index for bb
bb = pd.DataFrame(aa, index=['first', 'second', 'third'])
print(bb)

# get data frame from multi dimension array
aa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
bb = pd.DataFrame(aa, columns=['one', 'two', 'three'])
print(bb)

# deep copy data frame from bb
cc = bb.copy()
print(cc)

# map operator


# change value of one row
bb.iloc[0, :] = [11, 22, 33]
print(bb)

# change value of one column
bb.iloc[:, 0] = [111, 222, 333]
print(bb)

# map
bb.iloc[0, :] = bb.iloc[0, :] + 1
print(bb)


def add_nine(x):
    if x > 100:
        x += 99
    return x

# map on condition
bb = bb.applymap(add_nine)
print(bb)


