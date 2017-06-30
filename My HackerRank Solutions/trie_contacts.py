#Paul An

class Trie_Node():
    __slots__ = ["children", "is_leaf"]
    def __init__(self):
        self.children = [None]*26 #init None 26 times for each char in alphabet
        self.is_leaf = False

class Trie():
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return Trie_Node

    def insert(self, contact):
        return

    def find(self, partial):
        return

if __name__ == "__main__":
    n = int(raw_input().strip())  # number of lines
    contact_trie = Trie()
    for a0 in xrange(n):
        op, contact = raw_input().strip().split(' ')  # operations and contact or partial string
        if (str(op) == "add"):
            contact_trie.insert(contact)
        elif (str(op) == "find"):
            contact_trie.find(contact)
        else:
            print "invalid operation. You said {}".format(op)




