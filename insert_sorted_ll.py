class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self,val):
        #sorted insert
        cur = self.head
        prev = None
        while cur.next != None:
            nxt = cur.next
            prev = cur
            if val > prev.val and val < nxt.val:
                prev.next = Node(val)
                prev.next.next = nxt
                return
            cur = cur.next
        cur.next = Node(val)

ll_head = Node(1)
LL = LinkedList()
LL.head = ll_head

LL.insert(5)
LL.insert(9)
LL.insert(3)
cur = LL.head

while cur != None:
    print (cur.val)
    cur = cur.next


# 1 -> 5 -> 9
##ins(7)
##1 -> 5 -> 7 -> 9
