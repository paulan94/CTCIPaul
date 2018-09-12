class LL_node():
    def __init__(self,val):
        self.val = val
        self.next = None

head = LL_node(2)
head.next = LL_node(5)
head.next.next = LL_node(1)
head.next.next.next = LL_node(2)
