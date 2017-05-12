# broadcast can operate on matrix even the dimension not match exactly.

import numpy as np

matrix_one = np.matrix([[1, 1], [2, 2], [3, 3]])
matrix_two = np.matrix([-1, 1])
# 3 * 2 + 1 * 2, then 1 * 2 will copy several times.
print(matrix_one + matrix_two)

# this way we can copy the 1 * 2 matrix several times.
matrix_three = np.zeros(shape=[3, 2])
print(matrix_three + matrix_two)

