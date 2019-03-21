from node import Node

def fca(root,n1,n2):
    if not root: return None
    if not n1 and not n2: return None
    if not n1 or not n2: return None
    if n1 == n2: return n1
    if n1 == n2.left or n1 == n2.right: return n2
    if n2 == n1.left or n2 == n1.right: return n2
    if (contains(root.left, n1) and contains(root.right, n2)) or\
       (contains(root.left, n2) and contains(root.right, n1)):
        return root
    elif contains(root.left, n1) and contains(root.left,n2):
        return fca(root.left,n1,n2)
    elif contains(root.right, n1) and contains(root.right,n2):
        return fca(root.right,n1,n2)
    return None

def contains(root, node):
    if not root: return False
    if root == node: return True
    return contains(root.left, node) or contains(root.right, node)


rt = Node(5)
rt.left = Node(7)
rt.right = Node(10)
rt.left.left = Node(2)
rt.left.right = Node(1)

##print (contains(rt, rt.left))
print (fca(rt, rt.left.left, rt.left.right).val) #7

print (fca(rt, rt.left.left, rt.right).val) #5

print (fca(rt, rt.left.left, rt).val) #5

