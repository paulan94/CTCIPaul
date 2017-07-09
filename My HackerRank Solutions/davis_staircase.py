#Paul An
#david stairs example
def davis_stairs(steps):
    fib1 = 1
    fib2 = 2
    fib3 = 4
    # fib4.. exponential

    for i in range(steps - 1):
        fib1, fib2, fib3 = fib2, fib3, fib1 + fib2 + fib3
    return fib1


s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print davis_stairs(n)

