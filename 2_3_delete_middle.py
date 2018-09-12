class LL_node():
    def __init__(self,val):
        self.val = val
        self.next = None

head = LL_node(2)
head.next = LL_node(5)
head.next.next = LL_node(1)
head.next.next.next = LL_node(2)

#del that node if it is not the start or end
def del_node(node):
    if not node or not node.next:
        return False
    nxt = node.next
    node.val = nxt.val
    node.next = nxt.next

    return True

del_node(head.next.next) #del 3rd ele in head
while head:
    print (head.val)
    head = head.next
    
