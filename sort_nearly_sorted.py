a1 = [6, 5, 3, 2, 8, 10, 9]
k1 = 3

a2 = [10, 9, 8, 7, 4, 70, 60, 50]
k2 = 4

#Given an array of n elements, where each element
#is at most k away from its target position

def sort_nearly_sorted(arr, k):
    for n in range(len(arr)):
        s,e = n,n+k
        for kdx in range(n-k, e+1):
            if kdx in range(len(arr)):
                
