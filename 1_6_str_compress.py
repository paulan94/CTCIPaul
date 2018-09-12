def str_compress(some_str): #  -> some_str or another_str
    new_str = "" #strings are immutable in python
    count = 1
    for idx in range(len(some_str)-1):
        if some_str[idx] != some_str[idx+1]:
            new_str += some_str[idx] + str(count)
            count = 1
        else:
            count += 1
    new_str += some_str[-1] + str(count)

    if len(some_str) <= len(new_str):
        return some_str
    else:
        return new_str


print (str_compress('aabcccccaaa'))
print (str_compress('aaaab'))
print (str_compress('aaab')) #aaab
