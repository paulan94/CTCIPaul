from collections import defaultdict

##def check_perm(sstr):
##    sstr = sstr.replace(' ','')
##    char_dict = defaultdict(int)
##    for c in sstr:
##        if char_dict[c] > 0:
##            char_dict[c] -= 1
##        else:
##            char_dict[c] += 1
##    if len(sstr) % 2:
##        if max(char_dict.values()):
##            return True
##        else:
##            return False
##    elif not len(sstr) % 2: #even
##        if not max(char_dict.values()):
##            return True
##        else:
##            return False

def check_perm(inp_str):
    d_dict = defaultdict(int)
    mod_str = inp_str.replace(" ","").lower()
    for char in mod_str:
        if d_dict[char] > 0:
            d_dict[char] -= 1
        elif d_dict[char] <= 0:
            d_dict[char] += 1
    if len(mod_str) % 2 == 1:
        return (max(d_dict.values()) == 1)
    elif len(mod_str) % 2 == 0:
        return (max(d_dict.values()) == 0)

print (check_perm("tact coa"))
print (check_perm("tactf coa"))
print (check_perm("tactcoapapa"))
