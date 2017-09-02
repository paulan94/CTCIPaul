#algorithm to see if string has all unique characters

def is_unique(word):
    wL = []
    for i in word:
        if i in wL:
            return False
        wL.append(i)
    return True


assert(is_unique('fdf') == False)
assert(is_unique('thispo') == True)


def is_perm(word1, word2):
    if (len(word1) != len(word2)):
        return False
    wL = []
    for i in word1.lower():
        wL.append(i)
    for j in word2.lower():
        if j not in wL:
            return False
    return True

print is_perm('paul', 'luap')
print is_perm('kill','tenx')
print is_perm('cup', 'dfdf')
