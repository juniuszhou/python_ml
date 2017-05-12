import pandas as pd

# set chunk size to reduce the memory usage if file is big.
df = pd.read_csv("path", chunksize=10000, iterator=True)

df.to_csv("path", mode='w')
