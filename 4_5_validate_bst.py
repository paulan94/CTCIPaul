class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def validate_bst(mn, mx, root):
    if not root: return True
    elif root.val < mn or root.val > mx: return False
    return validate_bst(mn,root.val,root.left) and validate_bst(root.val,mx,root.right)



rt = Node(6)
rt.left = Node(5)
rt.left.right = Node(8)
rt.left.left = Node(1)
rt.right = Node(9)
rt.right.right = Node(11)

print (validate_bst(-100,100,rt))
