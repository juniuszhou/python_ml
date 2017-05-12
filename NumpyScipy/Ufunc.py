import numpy as np

# ufunc是universal function的缩写，它是一种能对数组的每个元素进行操作的函数。

array = np.array([1, 2, 3])

# reduce similar to sum.
print(np.add.reduce(array))
print(np.sin(array))
print(np.dot(array, array))

