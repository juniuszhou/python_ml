import numpy as np

# generate 0 to 9 vector
arr = np.arange(10)
print(arr)   # output of  [0 1 2 3 4 5 6 7 8 9]
myList = arr.tolist()
print(myList)

# add
arr1 = np.arange(10)
arr2 = np.arange(10, 20)
print(arr1 + arr2)

# multiply
print(arr1 * arr2)

# dot multiply
print(arr1.dot(arr2))

# average square
diff = abs(arr1 - arr2)
square = diff.dot(diff)
print(square / (len(arr1)))

# summary of ndarray
print("________summary info of ndarray__________")
print(arr1.shape, arr1.size, arr1.dtype, arr1.itemsize, arr1.data)

# np.linspace()





