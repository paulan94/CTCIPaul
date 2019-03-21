class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

        
def create_min_tree(arr,s,e):
    if not arr:return False
    if s > e: return False
    mid = (s+e)//2
    root = Node(arr[mid])
    root.left = create_min_tree(arr,s,mid-1)
    root.right = create_min_tree(arr,mid+1,e)
    return root

arr = [3,7,12,20,30]
arr2 = [3,7,12,20,30,40]

r = create_min_tree(arr,0,len(arr)-1)
r2 = create_min_tree(arr2,0,len(arr2)-1)

def print_preorder(root):
    if not root:
        return
    else:
        print (root.val)
        print_preorder(root.left)
        print_preorder(root.right)

print_preorder(r)
print()
print_preorder(r2)
