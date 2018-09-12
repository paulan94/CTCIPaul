class node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.visited = False


def dfs(root):
    if not root: return None
    root.visited = True
    print (root.val)
    for child in root.left, root.right:
        if child != None and child.visited == False:
            dfs(child)

rt = node(5)
rt.right = node(7)
rt.left = node(3)
rt.left.left = node(2)
rt.left.right = node(4)
rt.left.left.left = node(1)

dfs(rt)
                

