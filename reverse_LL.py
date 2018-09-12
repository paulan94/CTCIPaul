
def reverse_LL(node):
    head = None
    while node != None:
        new_node = LL_node(node.val)
        new_node.next = head
        head = new_node
        node = node.next
    return head
