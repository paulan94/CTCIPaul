class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_all_paths(root, paths=[]):
    if not root.left and not root.right:
        return [[root.val]]
    if root.left:
        paths.extend([[root.val] + c for c in get_all_paths(root.left,paths)])
    if root.right:
        paths.extend([[root.val] + c for c in get_all_paths(root.right,paths)])
    return paths


def del_invalid_paths(paths, root_val):
    paths_copy = paths[:]
    for path in paths_copy:
        if path[0] != root_val:
            paths.remove(path)
    

r = Node(5)
r.left = Node(3)
r.right = Node(10)
r.right.left = Node(1)
r.left.left = Node(20)
r.left.right = Node(21)

r2 = Node(8)
r2.left = Node(2)
r2.right = Node(6)
r2.left.left = Node(8)
r2.left.right = Node(7)

paths = (get_all_paths(r))
print (paths)
del_invalid_paths(paths,5)
print (paths)
