from collections import defaultdict



stream = [["Boston", "Mexican", 120],
          ["Boston", "Seafood", 340],
          ["Los Angeles", "Mexican", 1204],
          ["Los Angeles", "Seafood", 432],
          ["Los Angeles", "American", 777]]

expected = [[0,120,340],
            [777,1204,432]]

def main(stream):
    dicts = []
    visited = set()
    diff_food_types = set()
    #keep track of diff food types and put 0 on each city without them.
    res = []

    for s in stream:
        c,t,cnt = s[0],s[1],s[2]
        diff_food_types.add(t)
        if not c in visited:
            visited.add(c)
            d = defaultdict(dict)
            d[c][t] = cnt
            dicts.append(d)
        else:
            d[c][t] = cnt

    for d in dicts:
        for c in visited:
            if d[c]:
                for t in diff_food_types:
                    if not t in d[c]:
                        d[c][t] = 0
                
    for d in dicts:
        for v in (d.values()):
            arr = []
            for v2 in sorted(v.values()):
                arr.append(v2)
            if len(arr) > 0:
                res.append(arr)

    return res
        

        
ans = main(stream)
print (ans)
