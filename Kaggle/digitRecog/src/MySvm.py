# basically the svm for digit recognition doesn't work.
# reason is there is no feature select. the pixel doesn't mean anything for digit.


from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.DataFrame(pd.read_csv('../input/train.csv')[0:10000])

train, test = train_test_split(data, test_size=0.25)
classifier = svm.SVC(kernel='linear', decision_function_shape='ovo')

train_label = train.ix[:, 0].values.astype('int32')
train_features = train.ix[:, 1:].values.astype('float32')

classifier.fit(train_features, train_label)
print(test.ix[:, 0].values.astype('int32'))
print("--------------------------")
print(classifier.predict(test.ix[:, 1:]))



