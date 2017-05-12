import numpy as np
import pandas as pd

df = pd.read_csv("")

# change type of one column
df[df.columns[0]].astype(str)
df[df.columns[0]].astype(int)
