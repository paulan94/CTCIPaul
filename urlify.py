def urlify(s,true_len):
    total_len = len(s)-1
    for i in range(true_len-1,-1,-1):
        print (s[i])
        print (total_len, i)
        if s[i] != ' ':
            s[total_len] = s[i]
            total_len -= 1
        elif s[i] == ' ':
            s[total_len] = '0'
            s[total_len-1] = '2'
            s[total_len-2] = '%'
            total_len -= 3
        print (s)

    return s

print (urlify(list(x for x in'Mr John Smith    '), 13))
