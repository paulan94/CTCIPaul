def urlify(inp_str, str_len):
    space_count = 0
    for i in range(str_len):
        if inp_str[i] == ' ':
            space_count += 1
    index = str_len + space_count * 2
##    if (str_len < len(inp_str)): inp_str[str_len] = '\0'
    for idx in range(str_len-1, -1 , -1):
        if inp_str[idx] == ' ':
            inp_str[index-1] = '0'
            inp_str[index-2] = '2'
            inp_str[index-3] = '%'
            index -= 3
        else:
            inp_str[index-1] = inp_str[idx]
            index -= 1
        print (inp_str)

    return inp_str
print (urlify(list("Mr John Smith    "), 13))
