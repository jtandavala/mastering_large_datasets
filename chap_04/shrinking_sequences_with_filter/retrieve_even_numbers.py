def is_even(n):
    if n % 2 == 0: return True
    else: return False

print(list(filter(is_even, range(10))))
