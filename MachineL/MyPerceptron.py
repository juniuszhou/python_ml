__author__ = 'junius'
# perception just works for the training data is separable. the algorithm can be done in limited iteration.
import random

data_num = 10


def generate_data():
    num = 0
    points = []
    while num < data_num:
        x = random.randrange(0.0, 10.0)
        y = random.randrange(0.0, 100.0)

        x2 = random.randrange(20.0, 30.0)
        points.append((x, y, -1))
        points.append((x2, y, 1))
        num += 1
    return points


def get_error(data, w0, w1, b):
    num = 0
    sum_y = 0
    sum_x0 = 0
    sum_x1 = 0
    errors = 0
    while num < data_num * 2:
        item = data[num]
        y = item[0] * w0 + item[1] * w1 + b
        if y * item[2] < 0:
            sum_x0 += item[2] * item[0]
            sum_x1 += item[2] * item[1]
            sum_y += item[2]
            errors += 1
        num += 1

    return sum_x0, sum_x1, sum_y, errors


data = generate_data()
for i in data:
    print(i)

iter = 0
w0 = 0.01
w1 = 0.01
b = 0.01
while iter < 4000:
    error = get_error(data, w0, w1, b)
    w0 += error[0] * 0.01
    w1 += error[1] * 0.01
    b += error[2] * 0.01
    print("error as")
    print(error)
    print(w0, w1, b)
    iter += 1
    if error[3] == 0:
        iter += 400000

for i in data:
    print(i, w0*i[0]+w1*i[1]+b)