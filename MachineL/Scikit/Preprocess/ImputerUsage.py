import numpy as np
from sklearn.preprocessing import Imputer
# strategy should be mean median and most_frequent
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X=np.array([[1, 2], [np.nan, 3], [7, 6]])
Y=[[np.nan, 2], [6, np.nan], [7, 6]]
# use X as training data set, then get mean should be (1 + 7) / 3
imp.fit(X)

Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
Y = imp.transform(Y)
# then apply imputer learned to data Y
# just use (1 + 7) / 3 to replace NaN
print(Y)


