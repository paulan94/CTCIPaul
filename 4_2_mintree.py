#given sorted arr w unique int elements write alg to create BST w min height

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_min_bst(arr, start, end):
    if start > end:
        return None
    else:
        mid = (start + end)//2
        root = Node(arr[mid])

        root.left = create_min_bst(arr, start, mid-1)
        root.right = create_min_bst(arr, mid+1, end)

        return root

def print_bst_preorder(root):
    if not root: return None
    print (root.val)
    print_bst_preorder(root.left)
    print_bst_preorder(root.right)


arr = [1,2,3,4,5,6,7,9]
r = create_min_bst(arr,0, len(arr)-1)

print_bst_preorder(r)

#5,3,2,1,4,7,6,9

