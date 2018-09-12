
def triple_step(n,cache = {}):
    if n in cache:
        return cache[n]
    elif n == 0:
        return 1
    elif n < 0:
        return 0
    cache[n] = triple_step(n-1) + triple_step(n-2) + triple_step(n-3)
    return cache[n]

for i in range(5):
    print (triple_step(i))
