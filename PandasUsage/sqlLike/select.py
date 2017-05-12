import pandas as pd

df = pd.DataFrame()

some_value = 1

df.loc[df['column_name'] == some_value]

#To select rows whose column value is in an iterable, some_values, use isin:

df.loc[df['column_name'].isin(some_values)]
#Combine multiple conditions with &:

df.loc[(df['column_name'] == some_value) & df['other_column'].isin(some_values)]
#To select rows whose column value does not equal some_value, use !=:

df.loc[df['column_name'] != some_value]
#isin returns a boolean Series, so to select rows whose value is not in some_values, negate the boolean Series using ~:

df.loc[~df['column_name'].isin(some_values)]
