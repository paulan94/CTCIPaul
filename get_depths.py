class Node:
    def __init__(self,v):
        self.v = v
        self.r = None
        self.l = None

from collections import defaultdict
def get_level(node,level, dd):
    if not node: return None
    else:
        dd[level].append(node.v)
        get_level(node.l,level+1,dd)
        get_level(node.r,level+1,dd)


def main():
    rt = Node(1)
    rt.r = Node(5)
    rt.l = Node(2)
    rt.l.l = Node(7)
    rt.l.r = Node(10)
    rt.r.r = Node(13)
    dd = defaultdict(list)
    get_level(rt,1,dd)
    print (dd.items())

main()
