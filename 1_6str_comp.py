def strcomp(s):
    idx = 0
    new_str = ""
    count = 1
    while idx < len(s)-1:
        if s[idx] != s[idx+1]:
            new_str += s[idx] + str(count)
            count = 1
        else:
            count += 1
        idx += 1
    new_str += s[idx] +str(count)
    if len(new_str) < len(s):
        return new_str
    return s

print (strcomp("aabccccaaa"))
print (strcomp("aabbbbccccaaab"))
