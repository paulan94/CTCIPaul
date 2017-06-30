#Paul An

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""
def has_cycle(head):
    visited_set = set()
    visited_set.add(head.data)

    while (head.next != None):
        head = head.next
        if (head.data in visited_set):
            return True
        visited_set.add(head.data)
    return False