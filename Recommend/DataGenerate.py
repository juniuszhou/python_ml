__author__ = 'junius'
import random


def generate_uer_item():
    index = 0
    data = []
    while index < 10:
        user = random.randrange(0, 100)
        item = random.randrange(0, 100)
        rank = random.randrange(0, 5)
        data.append((user, item, rank))
        index += 1
    return data

data_set = generate_uer_item()
for i in data_set:
    print(i)

