class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def in_order(root):
    stack = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if len(stack) > 0:
                root = stack.pop()
                print (root.v)
                root = root.right
            else:
                return

def in_order_it(root):
    s = []
    while True:
        if root:
            s.append(root)
            root = root.left
        else:
            if len(s) > 0:
                pop = s.pop()
                print (pop.v)
                if pop.right:
                    s.append(pop.right)
            else:
                return

rt = Node(7)
rt.left = Node(3)
rt.left.left = Node(1)
rt.left.right = Node(5)
rt.left.right.right = Node(8)
rt.right = Node(10)

rt.right.right = Node(15)

##in_order(rt)
in_order_it(rt)
