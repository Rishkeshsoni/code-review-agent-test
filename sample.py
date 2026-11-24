import os, sys


def calculate_total(a, b):
    result = a + b
    return result


def get_numbers():
    numbers = [1, 2, 3, 4, 5]
    total = 0
    for i in numbers:
        total = total + i
    print(total)


x = 10
y = 20
print(calculate_total(x, y))
get_numbers()
