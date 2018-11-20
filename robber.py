arr = [3,4,5,1,3,None,1]

for idx in range(len(arr)):
    if arr[idx] == None:
        arr[idx] = 0

print (arr)


def rob(root):
    """
    :type root: TreeNode
    :rtype: int
     """
    odd_count = 0
    even_count = 0
    height = 0
    #get max by keeping track of sum of even heights vs odd heights
    if len(root) == 0: return 0
    elif len(root) == 1: return root[0]
    while 2**height < len(arr):
        print (height)
        if height == 0:
            even_count += root[0]
        elif height % 2 == 1: # odd
            odd_count += sum(root[2**(height-1):2**(height)+1])
            print (root[(2**(height-1)):(2**(height)+1)])
        else:
            even_count += sum(root[(2**(height-1)+1):((2**(height-1))+(2**(height)+1))])
##            print (root[(2**(height-1)+1):((2**(height-1))+(2**(height)+1))])
        height += 1
        print (odd_count, even_count)
    return max(odd_count, even_count)


print (rob(arr))
