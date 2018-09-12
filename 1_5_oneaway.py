from collections import defaultdict

def one_away(A,B):
    ddict = defaultdict(int)
    for char in A:
        ddict[char] += 1
    for char in B:
        if ddict[char] == 0:
            ddict[char] += 1
        elif ddict[char] > 0:
            ddict[char] -= 1
    return (sum(ddict.values()) <= 2)

print (one_away('pale', 'ple'))
print (one_away('pales', 'pale'))
print (one_away('pale', 'bale'))
print (one_away('pale', 'bake'))    #F
