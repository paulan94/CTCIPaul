import collections
def numPairsDivisibleBy60(time):
    c = collections.Counter()
    res = 0
    for t in time:
        res += c[-t % 60]
        c[t % 60] += 1
        print (c)
        print (res)
    return res


print (numPairsDivisibleBy60([30,20,150,100,40]))
