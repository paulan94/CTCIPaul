class LL_node():
    def __init__(self,val):
        self.val = val
        self.next = None

head = LL_node(2)
head.next = LL_node(5)
head.next.next = LL_node(1)
head.next.next.next = LL_node(2)

#O(n) space, O(n) time.
def rm_dup(hd):
    prev,cur = None, hd
    visited = set()

    while cur:
        if cur.val in visited:
            prev.next = cur.next
        else:
            visited.add(cur.val)
            prev = cur
        cur = cur.next
#runner solution without buffer. O(1) space, O(n^2) time
def rm_dup_run(hd):
    cur = hd
    while cur:
        runner = cur
        while runner.next:
            if runner.next.val == cur.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
        
rm_dup_run(head)

while head:
    print (head.val)
    head = head.next
