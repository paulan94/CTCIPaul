class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def print_bst_arr(root, arr=[]):
    if not root:
        return None
    else:
        arr.append(root.val)
        if root.left != None:
            print_bst_arr(root.left, arr)
            print_bst_arr(root.right, arr)
            print (arr)
def print_bst_arr2(root, arr=[]):
    if not root:
        return None
    else:
        arr.append(root.val)
        if root.right != None:
            print_bst_arr(root.right, arr)
            print_bst_arr(root.left, arr)
            print (arr)

print_bst_arr(root)
print_bst_arr2(root)
