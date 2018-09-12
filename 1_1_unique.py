

def is_unique(some_str):
    char_list = [False] * 128
    for idx in range(len(some_str)):
        val = ord(some_str[idx])
        if char_list[val]: return False
        else:
            char_list[val] = True

    return True


print (is_unique("hello"))
print (is_unique("helo"))
print (is_unique("asdbj8123l"))
