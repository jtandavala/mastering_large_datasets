"""
Reduce has 3 parts naminly:
1. Accumulator
2. Sequence
3. Initializer
"""

from functools import reduce

xs = [1, 5, 1, 19, 11, 203]

def my_add(a, b):
    return a + b

print(reduce(my_add, xs, 0))
