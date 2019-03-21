class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

rt = Node(5)
rt.left = Node(2)
rt.right = Node(6)
rt.left.left = Node(1)
rt.left.right = Node(3)

def contains(root,node):
        if not root:
            return False
        if root == node:
            return True
        elif root.left == node or root.right == node:
            return True
        return contains(root.left, node) or contains(root.right, node)


def lowestCommonAncestor(root, p, q):
        if not root:
            return None
        if p == q: return p.val
        if (contains(root.left,p) and contains(root.right,q)) or (contains(root.left,q) and self.contains(root.right,p)):
            return root.val
        return lowestCommonAncestor(root.left,p,q) or lowestCommonAncestor(root.right,p,q)
