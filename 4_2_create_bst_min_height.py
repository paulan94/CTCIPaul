class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def create_bst_min_height(arr,start, end):
    if not arr or len(arr) == 0 or end < start:
        return None
    else:
        mid = (start + end)//2
        node = Node(arr[mid])
        print (node.val)
        node.left = create_bst_min_height(arr,start,mid-1)
        node.right = create_bst_min_height(arr,mid+1,end)
        return node


arr = [1,2,3]
arr2 = [1,2,3,4,5,6,7,8]

x1 = create_bst_min_height(arr,0,len(arr)-1)
x2 = create_bst_min_height(arr2,0,len(arr2)-1)

print (x1.val, x1.left.val, x1.right.val)
print (x2.val, x2.left.val, x2.right.val, x2.left.left.val, x2.right.right.val )
