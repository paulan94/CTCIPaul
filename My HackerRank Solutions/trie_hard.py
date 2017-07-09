class Trie(object):
    def __init__(self):
        self.root = Node('*')

    def add(self, word):
        curr = self.root
        for w_char in word:
            #this returns some child Node or None
            next_node = curr.get_child(w_char)
            if not next_node:
                next_node = Node(w_char)
                curr.children.append(next_node)
            #always add to num_associated words per char
            next_node.num_associated_words += 1
            curr = next_node
        curr.is_word = True

    def find(self, partial):
        curr = self.root
        for w_char in partial:
            next_node = curr.get_child(w_char)
            if not next_node:
                return 0
            curr = next_node
        return curr.num_associated_words

class Node(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_word = False
        self.num_associated_words = 0

    def get_child(self, c):
        #look for children. if it is the same as the char we are looking for, return that child Node
        for child in self.children:
            if child.char == c:
                return child
        return None

n = int(raw_input().strip())  # number of lines
pTrie = Trie()

for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')  # operations and contact or partial string
    if op == "find":
        print pTrie.find(contact)
    elif op == "add":
        pTrie.add(contact)
