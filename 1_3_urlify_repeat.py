def urlify(some_str, truelen): # -> new_str
    count_spaces = 0
    for idx in range(truelen):
        if some_str[idx] == ' ':
            count_spaces += 1

    new_len = truelen + (count_spaces * 2)

    for idx in range(truelen-1,-1,-1):
        if some_str[idx] == ' ':
            some_str[new_len-3] = '%'
            some_str[new_len-2] = '2'
            some_str[new_len-1] = '0'
            new_len -= 3
        else:
            some_str[new_len-1] = some_str[idx]
            new_len -= 1

    return some_str


print (urlify(list("Mr John Smith    "), 13))
