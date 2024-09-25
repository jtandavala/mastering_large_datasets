from multiprocessing import Pool

def print_and_return(x):
    print(x); return x

if __name__ == '__main__':
    with Pool() as P:
        P.map(print_and_return, range(200))
