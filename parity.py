def even_first(A):
    eidx, oidx = 0, len(A)-1

    while eidx < oidx:
        if A[eidx] % 2 == 0:
            eidx += 1
        else:
            A[eidx], A[oidx] = A[oidx], A[eidx]
            oidx -= 1

A = [1,2,3,4,5,6,7,8,9,10,11]

even_first(A)
print (A)
