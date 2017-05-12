import pandas as pd
import numpy as np

matrix_one = np.matrix([[1, 1], [2, -2]])

eigen, eigen_vectors = np.linalg.eig(matrix_one)
print(eigen)
print(eigen_vectors)
np.linalg.norm(matrix_one)


# basic info got from pandas.
df = pd.DataFrame(matrix_one)
print(df.describe())
print(df.shape)
print(df.corr())
print(df.cov())

print(df.sample(frac=0.5))


# both index and columns
print(df.axes)



