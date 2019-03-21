def shortest_substr_pattern(S,P):
    r,l = 0,0
    char_dict = dict()
    best = 9999
    for c in P:
        char_dict[c] = 0
    while not all(x >= 1 for x in char_dict.values()):
        if r >= len(S): break
        if S[r] in char_dict.keys():
            char_dict[S[r]] += 1
        r += 1
    while all(x > 0 for x in char_dict.values()):
        if all(x <= 0 for x in char_dict.values()):
            break
        if S[l] in char_dict.keys():
            char_dict[S[l]] -= 1
        l += 1
        if r - l +1 < best:
            best = r - l + 1
    return best

#more optimal maybe?
##def shortest_substr_pattern(S,P):
##    r,l = 0,0
##    char_dict = dict()
##    best = 9999
##    for c in P:
##        char_dict[c] = 0
##    while r < len(S):
##        if S[r] in char_dict.keys():
##            char_dict[S[r]] += 1
##        r += 1
##        if all(char_dict[char] > 0 for char in P):
##            while all(char_dict[char] > 0 for char in P):
##                if S[l] in char_dict.keys():
##                    char_dict[S[l]] -= 1
##                l += 1
##            if r - l + 1 < best:
##                best = r - l + 1
##    return best


S = 'DADBBCBBB' # 5
S2 = 'DDABBAC' #3
P = 'ABC'
print (shortest_substr_pattern(S,P))
print ('second')
print (shortest_substr_pattern(S2,P))
