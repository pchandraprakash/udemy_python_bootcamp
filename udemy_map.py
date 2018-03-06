"""
Map inbuilt function takes two arguments; a function and a sequence.
syntax: map(function, sequence)
first argument is the name of the function and second is the sequence.

Steps:
1. Define a function or a function through a lambda expression
2. Create a sequence(s)
3. Assign the result to a variable, if you are using a return clause
4. Print that variable by casting it to relevant data type
"""
# example 1: Fahrenhit temperatures


def fahrenhit(t):
    return (9.0/5)*t + 32


temp = [20, 10, 32, 45, 100]
f = list(map(fahrenhit, temp))
print(f)

# example 2: Adding two list elements


def add(x, y):
    return x + y


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

s = list(map(add, l1, l2))
print(s)

# using Lambda expressions
print(list(map(lambda x, y: x + y, l1, l2)))


# example 3: Simple Interest
p = [1000, 2000, 3000]
t = [5, 10, 15]
r = [0.15, 0.25, 0.35]
si = list(map(lambda p, t, r: (p*t*r)/100, p, t, r))
print(si)

