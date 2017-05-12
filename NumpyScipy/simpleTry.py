import numpy as np
import pandas as pd


def ff(a, *b):
    print(a)


num_inputs = 2
input_shape = (4, 5, 6)
output_dim = 3

ff(18, *input_shape)

input_size = num_inputs * np.prod(input_shape)
weight_size = output_dim * np.prod(input_shape)

print(input_size)
print(weight_size)
print(np.prod(input_shape))
print(*input_shape)
print(np.prod(input_shape))
x = np.linspace(-0.1, 0.5, num=input_size).reshape(num_inputs, *input_shape)
w = np.linspace(-0.2, 0.3, num=weight_size).reshape(np.prod(input_shape), output_dim)
b = np.linspace(-0.3, 0.1, num=output_dim)

# print(x)
# print(w)
# print(b)

df = pd.DataFrame(data=[[1, -1]])
print(df.abs())

print(np.abs(df))

