
def str_c(S):
    i,j = 0,1
    new_str = ''
    while j < len(S):
        count = 1
        while S[i] == S[j] and (j <len(S)-1):
            count += 1
            j += 1
        new_str += S[i] + str(count)
        i = j
        j = i+1
    if len(new_str) > len(S):
        return S
    return new_str

print (str_c('aabcccccaaa'))
print (str_c('abcd'))

