import pandas as pd

df = pd.DataFrame()

# sort the count to see how many missing value for each feature.
df.count().sort_values()

# check the data variance of each column. if all values are equal for one column.
# you can drop it since it has on impact on our prediction.
df.apply(pd.Series.nunique).sort_values()

# get mean of a column, just for numeric type
df['column'].mean()

# list all columns data type
print(df.dtypes)

#
