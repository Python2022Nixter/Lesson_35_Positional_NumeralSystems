import timeit

def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        i += 1
        s += i
    return s

def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s

def ttt():
    print(f"while_loop: {timeit.timeit(while_loop, number=1)}")
    print(f"for_loop: {timeit.timeit(for_loop, number=1)}")
    
ttt()
