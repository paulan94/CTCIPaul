class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def in_order(root):
    arr = []
    if not root:
        return []
    else:
        left = in_order(root.left)
        right = in_order(root.right)
    return left + [root.val] + right

rt = Node(5)
rt.left = Node(2)
rt.right = Node(7)
rt.left.left = Node(1)

arr =  (in_order(rt))
print (arr)
