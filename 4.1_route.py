class Node():
    def __init__(self, val):
        self.val = val
        self.children = []


def route_exists(N, M):
    if not N or not M: return False
    else:
        visited = set()
        queue = [N]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.val == M.val: return True
            visited.add(node)
            for child in node.children:
                if child not in visited:
                    queue.append(child)
        return False
    

n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n0.children.append(n1)
n0.children.append(n4)
n0.children.append(n5)
n1.children.append(n3)
n1.children.append(n4)
n2.children.append(n1)
n3.children.append(n2)
n3.children.append(n4)

print (route_exists(n0,n3)) #T
print (route_exists(n0,n2))#T
print (route_exists(n4,n3))#F
print (route_exists(n4,n4))#T
print (route_exists(n1,n5))#F
print (route_exists(n1,n3))
