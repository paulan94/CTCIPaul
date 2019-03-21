
def sort_rgb(arr):
    l,r = 0, len(arr)-1
    while True:
        while arr[l] == 'R' and l < r:
            l += 1
        while arr[r] != 'R' and l < r:
            r -= 1
        if l >= r: break

        arr[l], arr[r] = arr[r], arr[l]

    r = len(arr)-1
    while True:
        while arr[l] == 'G' and l < r:
            l += 1
        while arr[r] != 'G' and l < r:
            r -= 1
        if l >= r: break

        arr[l], arr[r] = arr[r], arr[l]


    print ("finished sorting")

A = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print (A)
sort_rgb(A)
print (A)
