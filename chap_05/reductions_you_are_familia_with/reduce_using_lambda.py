from functools import reduce

my_products = [
    {"price": 9.99},
    {"sn": "00231"},
    {"price":  74.99},
    {"sn":  "00013"},
    {"price":  19.99},
]

print(reduce(lambda acc, next: acc + next.get('price', 0), my_products, 0))
