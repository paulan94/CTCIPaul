def longestOnes(A, K):
    j, k, ans = 0, 0, 0
    for i, v in enumerate(A):
        if v == 0:
            k += 1
            while k > K and j <= i:
                if A[j] == 0:
                    k -= 1
                j += 1
        ans = max(ans, i-j+1)
    return ans

print (longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
