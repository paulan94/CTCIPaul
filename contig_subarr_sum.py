arr = [1,4,6,21]

def naive_sol(arr,target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if sum(arr[i:j]) == target: return True
    return False

print (naive_sol(arr,10))
print (naive_sol(arr,9))
