

class Queue():
    def __init__(self):
        self.wrong_stack = []
        self.right_stack = []
    
    def enq(self,val):
        while len(self.right_stack) > 0:
            self.wrong_stack.append(self.right_stack.pop())
        self.wrong_stack.append(val)
    def deq(self):
        while len(self.wrong_stack) > 0:
            self.right_stack.append(self.wrong_stack.pop())
        node = self.right_stack.pop()
        return node
        
        
q = Queue()
for i in range(10):
    q.enq(i)

print (q.deq())
print (q.wrong_stack, q.right_stack)
