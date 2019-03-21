
def rob_houses(arr):
    dp = [0] * len(arr)
    for i in range(len(arr)):
        if i == 0:
            dp[i] = arr[i]
        elif i == 1:
            dp[i] = max(arr[0],arr[i])
        else:
            dp[i] = max(arr[i] + dp[i-2], dp[i-1])

    return dp[-1]

a = [3,7,2,5,7]
a2 = [2,7,9,3,1]

print (rob_houses(a))
print (rob_houses(a2))
