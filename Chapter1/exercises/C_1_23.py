from random import randint

a = [6, 46, 8, 468, 4, 9, 81, 3, 17]
b = randint(0, len(a)+1)
try:
    print(a[b])
except IndexError:
    print("Don't try buffer overflow attack in Python!")
