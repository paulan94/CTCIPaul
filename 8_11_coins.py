from collections import defaultdict
def make_change(n,coins=[25,10,5,1],idx=0, m = defaultdict(int)):
    if m[(n,idx)] > 0: return m[(n,idx)] 
    if idx == len(coins)-1: return 1
    curr_coin = coins[idx]
    ways = 0
    i = 0
    while i * curr_coin <= n:
        amount_left = n - i * curr_coin
        ways += make_change(amount_left,coins,idx+1,m)
        i += 1
    m[(n,idx)]  = ways
    return m[(n,idx)] 


print (make_change(20))
