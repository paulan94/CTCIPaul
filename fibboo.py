def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_cache(n, cache={}):
    if n in cache:
        return cache[n]

    else:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            cache[n] = fib_cache(n-1) + fib_cache(n-2)
            return cache[n]


for i in range(10):
    print (fib_cache(i))
