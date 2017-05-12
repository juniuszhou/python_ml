import numpy as np

matrix_one = np.matrix([[1, 1], [2, 2], [3, 3]])
matrix_two = np.matrix([[5, 6], [7, 8], [9, 10], [11, 12]])

# square
print(np.square(matrix_one))

# matrix multiply
print(matrix_one.dot(matrix_two.T))

# sum , must set the axis, default is sum in all dimension.
print(matrix_one.sum())
print(matrix_one.sum(axis=1)) # each row
print(matrix_one.sum(axis=0)) # each column


# broadcast for matrix with different shape
# if the column 's number is the same.
# matrix_three as a vector can broadcast to each vector in matrix_one for minus
matrix_three = np.matrix([-1, 1])
print(matrix_one - matrix_three)


