def is_unique(some_str):
    s = sorted(some_str)
    if len(s) == 1:
        return True
    else:
        p1 = 0
        p2 = 1
        while p2 < len(s):
            if s[p1] == s[p2]:
                return False
            p1 += 1
            p2 += 2
        return True

print(is_unique("yo"))

print(is_unique("yoo"))
print(is_unique("y"))

print(is_unique("fgdfgf"))
