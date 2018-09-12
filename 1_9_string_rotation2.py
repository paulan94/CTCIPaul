
def str_rotate(s1,s2):
    if len(s1) != len(s2): return False
    s2_idx = len(s2)
    while s2[:s2_idx] not in s1:
        s2_idx -= 1
    s2_edit = s2[:s2_idx]
    s1 = s1.replace(s2_edit, "")
    s2 = s2.replace(s2_edit, "")
    return s1 == s2


print (str_rotate("waterbottle", "erbottlewat"))
