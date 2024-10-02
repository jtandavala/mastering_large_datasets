import json
from functools import reduce

def get_profit(d):
    return d.get('price-sell', 0) - d.get('price-buy', 0)

def low_med_hi(d, k, low, high):
    if d[k] < low:
        return "low"
    elif d[k] < high:
        return "med"
    return "high"

def clean_entry(d):
    r = {}
    r['profit'] = get_profit(d)
    r['mpg'] = low_med_hi(d, 'mpg', (18, 35))
    r['odo'] = low_med_hi(d, 'odo', (60000,100000))
    return r

def acc_average(acc, profit):
    acc['total'] = acc.get('total', 0) + profit
    acc['count'] = acc.get('count', 0) + 1
    acc['average'] = acc['total'] / acc['count']
    return acc

def sort_and_add(acc, nxt):
    profit = nxt['profit']
    nxt_mpg = acc['mpg'].get(nxt['mpg'],{})
    nxt_odo = acc['odo'].get(nxt['odo'],{})
    acc['mpg'][nxt['mpg']] = acc_average(nxt_mpg, profit)
    acc['odo'][nxt['odo']] = acc_average(nxt_odo, profit)
    return acc

if __name__=="__main__":
    with open("cars.json") as f:
        xs = json.loado(f)
    results = reduce(sort_and_add, map(clean_entry, xs), {"mpg": {}, "odo": {}})
    print(json.dumps(results, indent=4))
