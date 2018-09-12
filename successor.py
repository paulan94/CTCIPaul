class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None


root = Node(2)
root.right = Node(3)
root.right.parent = root
root.left = Node(1)
root.left.parent = root
root.left.left = Node(4)
root.left.left.parent = root.left
root.left.right = Node(5)
root.left.right.parent = root.left

def find_next_node(inp_node):
    if inp_node.right != None:
        return inp_node.right.val
    if inp_node.parent == None and inp_node.right != None:
        return inp_node.right.val
    if inp_node.parent != None and inp_node == inp_node.parent.left:
        return inp_node.parent.val
    else:
        return None



print (find_next_node(root.left.left)) #1
print (find_next_node(root.left)) #5
print (find_next_node(root.left.right)) #None
print (find_next_node(root)) # 3
        
