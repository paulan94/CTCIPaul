def replace_space(word1,wlen):
    for i in range(wlen):
        if word1[i] == ' ':
            word1[i] == '%20'
            
    return word1

x = replace_space('hello world  ', 11)
print x
