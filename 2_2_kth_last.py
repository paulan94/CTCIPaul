from LL_node import LL_node, head

#2-5-1-2

def kth_to_last(head,k):
    p1 = head
    p2 = head

    for idx in range(k):
        if not p1.next: return None
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2.val

print (kth_to_last(head,3))
print (kth_to_last(head,1))
