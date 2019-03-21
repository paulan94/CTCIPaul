S = 'DADDDBBDCA'
pattern = ('A','B','C')


def find_substr(s, p):
    l,r = 0,0
    best = 10
    while not in_str(s,p) and r < len(s):
        
        if in_str(s[l:r+1],p):
            if not best or len(s[l:r+1]) < best:
                best = len(s[l:r+1])
            while in_str(s[l:r+1],p):
                l += 1
        r += 1

        print (l,r)
    return best
##    while

def in_str(s, p):
    pd = dict()
    for pc in p:
        pd[pc] = False
    for c in s:
        if c in pd:
            pd[c] = True
    for each in pd.values():
        if not each:
            return False
    return True

print (in_str('DADDDBBDCA', ('A','B', 'C')))
print (in_str('abc', ('c','a','b')))
print (in_str('abc', ('c','f','b'))) #F
print (in_str('abc', ('c','a','a')))


print (find_substr(S,pattern))
