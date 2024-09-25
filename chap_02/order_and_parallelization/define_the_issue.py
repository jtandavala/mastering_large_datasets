"""
Another condition that can cause us problems when we’re
working in parallel is order sensitivity.
When we work in parallel, we’re not guaranteed that
tasks will be finished in the same order they’re input.
This means that if we’re doing work that needs to be
processed in a linear order, we probably shouldn’t do
it in parallel
"""
from multiprocessing import Pool

if __name__ == '__main__':
    with Pool() as P:
        P.map(print, range(1000))
