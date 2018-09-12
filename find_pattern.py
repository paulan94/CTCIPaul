
def find_pattern(A,S):
    i,j = 0,0
    if len(S) > len(A): #edge case practice, also need to handle empty inputs
        return find_pattern(S,A)
    while i < len(A) and j < len(S):
        if A[i] == S[j]:
            if j == len(S)-1: #if we reached the last idx of S and we got a match
                return True
            j += 1
        i += 1
    return False

##O(A+S)

print (find_pattern("abcde", "ace")) #True
print (find_pattern("abc", "abc")) #True
print (find_pattern("ppppppl", "pl")) #True

print (find_pattern("pl", "ppppppl")) #True
print (find_pattern("addjakf", "fj")) #F
print (find_pattern("djfjjfda", "aad")) #F

print (find_pattern("cat","ca")) #T
print (find_pattern("cat","cat")) #T
print (find_pattern("catop","cp")) #T
print (find_pattern("cat","pl")) #F
