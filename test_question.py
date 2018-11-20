import math
def round_nums(a,target):
    floors = list(map(math.floor, a))

    diff = int(target - sum(floors))

    sorted_changes = sorted(enumerate(a), key = lambda x : x[1])
    
    for _ in range(diff):
        floors[sorted_changes.pop()[0]] += 1
        
    return floors

a = [0.70, 2.80, 4.90]
print (round_nums(a, 5))

print (round_nums(a, 8))
