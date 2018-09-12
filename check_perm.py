def check_perm(A,B):
    if len(A) != len(B): return False
    return (sorted(A)) == (sorted(B))

def check_perm2(A,B):
    #ASCII
    ascii_int_arr = [0] * 128
    for idx in range(len(A)):
        val = ord(A[idx])
        ascii_int_arr[val] += 1
    for idx in range(len(B)):
        val = ord(B[idx])
        ascii_int_arr[val] -= 1
        if ascii_int_arr[val] < 0: return False
    return True

print (check_perm("god", "dog"))
print (check_perm("god", "dog "))
print (check_perm("god", "dfog"))

print (check_perm2("god", "dog"))
print (check_perm2("god", "dog "))
print (check_perm2("god", "dfog"))
