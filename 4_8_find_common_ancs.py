class Node():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


def node_exists(root,node):
    if root == node:
        return True
    if not root:
        return None
    else:
        return node_exists(root.left,node) or node_exists(root.right,node)
    return False

def find_ca(root,A,B):
    if not root: return None
    if not A and not B: return root
    if (node_exists(root.right,A) and node_exists(root.left,B)) or (node_exists(root.right,B) and node_exists(root.left,A)):
        return root
    else:
        return find_ca(root.left,A,B) or find_ca(root.right,A,B)



root = Node(2)
root.left = Node(1)
root.left.left = Node(5)
root.left.right = Node(6)
root.right = Node(3)

print (find_ca(root,root.left.left, root).val)
