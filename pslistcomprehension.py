"""list comprehension"""
from timeit import timeit


def demo1():
    items = [1, 3, 2, 4, 5, 6, 7]
    temp = []

    for item in items:
        temp.append(hex(item))

    return temp


def demo2():
    items = [1, 3, 2, 4, 5, 6, 7]
    temp = [hex(item) for item in items]  # list comprehension
    return temp


if __name__ == '__main__':
    print(timeit('sin(30)', setup='from math import sin', number=100000))
    print(timeit('demo1()', setup='from __main__ import demo1', number=100000))
    print(timeit('demo2()', setup='from __main__ import demo2', number=100000))
