from random import randint


def my_shuffle(data):
    y = []
    while data:
        x = randint(0, len(data)-1)
        y.append(data[x])
        data.pop(x)
    return y
