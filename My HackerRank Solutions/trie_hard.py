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

    def find_words(self, partial):
        #check if child has children, check if it is a word. if it is a word and has more children,
        #save word and continue looping until we find the end of is_word and it has no children
        curr = self.root
        word_list = []
        word_str = ""

        #w -> word, words, wam
        #wo -> word, words
        for w_char in partial:
            next_node = curr.get_child(w_char)
            if not next_node:
                return 0
            curr = next_node
            word_str += curr.char
        #do something on this line
        #curr is the last node from the given partial word ie: hac
        #from hac: curr.char = c
        print curr.char
        next_node = curr.get_child(curr.char)
        print next_node.children
        while next_node != None: #until next_node is None
            print next_node.char
            word_str += next_node.char
            if not next_node:
                return 0
            if next_node.is_word:
                word_list.append(word_str)
                print "inside if ", word_list
            next_node = next_node.get_child(next_node.char)


        #
        # for w_char in partial: #for each char in word ex. "word"
        #     next_node = curr.get_child(w_char) #next node is child of current. 1st iter: root -> finds Node('w')
        #     while next_node:
        #         if not next_node: #if node doesnt exist, stop find
        #             return 0
        #         curr = next_node #set current to next node. 1st iter: curr = Node('w')
        #         word_str += curr.char #word_str = "" -> "w"
        #         # this is finding the first word and stopping everytime
        #         if curr.is_word:  # if the current Node indicates a end of word signal, append to word list
        #             word_list.append(word_str)
        #         next_node = curr.get_child(curr.char) #next node is child of current. 1st iter: root -> finds Node('w')


        return word_list

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
    elif op == "words":
        print pTrie.find_words(contact)
