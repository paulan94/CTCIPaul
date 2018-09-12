
def stairs(n):
    if n <0: return 0
    if n == 0: return 1

    else: return stairs(n-1) + stairs(n-2) + stairs(n-3)

for i in range(10):
    print( stairs(i))
