
class Node():
    def __init__(self, val):
        self.val = val
        self.created = False
        self.dependson = []


def build_order(p):
    p_cpy = [x for x in p]
    idx = 0
    build_order = []
    while len(p_cpy) > 0:
        if idx >= len(p_cpy): #if visited all elements in p arr, start again
            idx = 0
        node = get_last_node_dfs(p_cpy[idx])
        print (node.val)
        build_order.append(node.val)
        for nd in p:
            if node in nd.dependson:
                nd.dependson.remove(node)
        p_cpy.remove(node)
        idx += 1
    return build_order[::-1]

def get_last_node_dfs(node):
    if len(node.dependson) == 0:
        node.created = True
        return node
    if not node:
        return None
    else:
        for child in node.dependson:
            if not child.created:
                print (child.val)
                return get_last_node_dfs(child)

            
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.dependson = [n4]
n2.dependson = [n4]
n4.dependson = [n3]
n6.dependson = [n1,n2]

p = [n1,n2,n3,n4,n5,n6]

bo = build_order(p)
print (bo)
