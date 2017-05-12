import pandas as pd
import numpy as np
from sklearn import linear_model

data = pd.read_csv("../../../Data/regression.csv", header=None)
labels = data.ix[:, :0]
features = data.ix[:, 1:]

print(labels)
print(features)

regress = linear_model.LinearRegression()
# pay attention the order, features first then label.
regress.fit(features, labels)

print("coefficient is :")
print(regress.coef_)

print("intercept is ")
print(regress.intercept_)

test = pd.read_csv("../../../Data/regression_test.csv", header=None)

print("predict result.")
predict = regress.predict(test.ix[:, :])
print(predict)

print("average loss is ")
print(np.mean((predict - test.ix[:, :0]) ** 2))

