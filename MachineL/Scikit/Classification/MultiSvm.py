# bad idea. svm just for two class problem.
from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd
import os
cwd = os.getcwd()
print(cwd)
data = pd.read_csv("../../../Data/multi_class.csv")
train, test = train_test_split(data, test_size=0.5)
labels = train.ix[:, 0].values.astype('int32')
X_train = train.ix[:, 1:].values.astype('float32')

test_labels = test.ix[:, 0].values.astype('int32')
test_data = test.ix[:, 1:].values.astype('float32')

X_test = pd.read_csv('../../../Data/binary_class_test.csv').values.astype('float32')

classifier = svm.SVC(gamma=0.001, decision_function_shape='ovo')
classifier.fit(X_train, labels)

predicted = classifier.predict(test_data)

print(classifier.class_weight_)

print(test_labels)
print(predicted)

