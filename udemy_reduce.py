import functools  # for reduce function
import itertools  # for accumulate function
"""
Reduce is an inbuilt function which reduces a sequence continuously until a final value is obtained
"""
# example 1: Finding maximum value in a list
l1 = [10, 20, 30, 55, 65, 100, 1, 5, 400, 64, 854, 3, 8, 9, 0]
print(max(l1))
print(functools.reduce(lambda a, b: a if (a > b) else b, l1))

# example 2: Finding the sum of all the elements of a list/tuple
t1 = (1, 4, 5, 6, 8, 9, 10, 12, 3, 45, 5, 66, 89)
print(functools.reduce(lambda a, b: a + b, t1))
print(list(itertools.accumulate(t1, lambda a, b: a + b)))


def my_func(*args):
    for i in args:
        len()
        print(i[3])


my_func([1, 2, 3, 4])

