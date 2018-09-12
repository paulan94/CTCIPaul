def str_compress(inp_str):
    new_str = ""
    cnt = 1
    last_char = ""
    for idx in range(len(inp_str)-1):
        if inp_str[idx] == inp_str[idx+1]:
            cnt += 1
        elif inp_str[idx] != inp_str[idx+1]:
            new_str += inp_str[idx] + str(cnt)
            cnt = 1
        last_char = inp_str[idx+1]
    new_str += last_char + str(cnt)
    
    if len(new_str) < len(inp_str):
        return new_str
    return inp_str

print (str_compress('aabcccccaaab'))
