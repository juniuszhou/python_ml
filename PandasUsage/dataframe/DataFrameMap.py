import pandas as pd
import numpy as np

aa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

bb = pd.DataFrame(aa, columns=['one', 'two', 'three'])

print(bb)


def add_nine(x):
    if x > 6:
        x += 99
    return x

# map all items on condition
bb = bb.applymap(add_nine)
print('+++++ After apply map method ++++++++')
print(bb)

# map just first column
bb.ix[:, 0] = bb.ix[:, 0].map(add_nine)
print(bb)

# map just first row
bb.ix[0, :] = bb.ix[0, :].map(lambda x: x+10)
print(bb)





