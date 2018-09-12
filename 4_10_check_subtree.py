class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def same_tree(A,B):
    if not A and not B:
        return True
    elif not A or not B:
        return False
    elif A.val != B.val:
        return False
    elif A.val == B.val:
        left = same_tree(A.left,B.left)
        right = same_tree(A.right,B.right)
        return (left and right)


A = Node(5)
A.left = Node(3)
A.right = Node(10)


B = Node(5)
B.left = Node(3)
B.right = Node(10)
##B.left.left = Node(2)

print (same_tree(A,B))
