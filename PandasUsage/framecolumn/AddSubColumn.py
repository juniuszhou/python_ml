import pandas as pd
import numpy as np

df = pd.read_csv("oatg")
# drop a second column
df.drop(df.columns[1], 1)
# drop a second row
df.drop(1, 0)
