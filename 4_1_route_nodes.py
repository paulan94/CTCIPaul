class Node:
    def __init__(self,val):
        self.val = val
        self.children = []

def route_exists(a,b):
    if a.val == b.val:
        return True
    elif (not a and b) or (not b and a):
        return False
    else:
        for c in a.children:
            if route_exists(c,b):
                return True

        return False


a = Node(5)
b = Node(6)
c = Node(7)
d = Node(8)
e = Node(10)
f = Node(11)

a.children += [b,c,d]
d.children.append(e)

print (route_exists(a,e))
print (route_exists(a,f))
