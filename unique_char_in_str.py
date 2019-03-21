from collections import defaultdict

def find_it(S):
    dd = defaultdict(int)
    ans = []
    for char in S:
        dd[char] += 1
    for c in S:
        ans.append(dd[c])
        
    for i in range(len(ans)):
        if ans[i] == 1:
            return S[i]
    return 0

print (find_it('zabcdbazp'))
