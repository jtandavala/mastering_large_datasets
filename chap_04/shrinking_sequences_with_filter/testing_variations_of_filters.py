from itertools import filterfalse
from toolz.dicttoolz import keyfilter, valfilter, itemfilter

def is_even(n):
    if n % 2 == 0: return True
    else: return False

def both_are_even(n):
    k, v = n
    if is_even(k) and is_even(v): return True
    else: return False

print(list(filterfalse(is_even, range(10))))
print()
print(list(keyfilter(is_even, {1: 2, 2:3, 3:4, 4: 5, 5:6})))
print()
print(list(itemfilter(both_are_even, {1:5, 2:4, 3:3, 4:2, 5:1})))
