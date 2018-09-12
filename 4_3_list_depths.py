from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_LL(root, depth_dict=defaultdict(list), depth=0):
    if not root: return None
    else:
        depth_dict[depth].append(root.val)
        for child in root.left,root.right:
            create_LL(child,depth_dict,depth+1)
    return depth_dict

root = Node(1)
root.left = Node(2)

root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

d = create_LL(root)
for k,v in d.items():
    print (k, v)
