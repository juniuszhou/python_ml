import numpy as np

a = np.array((1, 2, 3))
b = np.array((2, 3, 4))
print(np.hstack((a, b)))

a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
print(np.hstack((a, b)))

a = np.random.random([2, 2])
print(a.shape)
print(a)
one = np.ones((a.shape[0], 1))
print(np.hstack((a, one)))
print(np.hstack((a, np.ones((a.shape[0], 1)))))


