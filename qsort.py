from statistics import median

def qsort(A,low,high):
    if low < high:
        p = partition(A, low, high)
        qsort(A, low, p-1)
        qsort(A, p+1, high)


def partition(A, low, high):
    pivot_idx = 0
    pivot_val = median([A[low], A[high], A[(high-low)//2]])
    if A[low] == pivot_val:
        pivot_idx = low
    elif A[high] == pivot_val:
        pivot_idx = high
    else:
        pivot_idx = (high-low)//2
    print ('piv:', A[pivot_idx], A[low:high+1])
    A[pivot_idx], A[low] = A[low], A[pivot_idx]
    border = low

    for i in range(border, high+1):
        if A[i] < pivot_val:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return border

A = [17,41,5,22,54,6,29,3,13]

qsort(A, 0, len(A)-1)
print(A)
    
