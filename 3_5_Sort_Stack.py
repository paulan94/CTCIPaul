class Stack():
    def __init__(self):
        self.stack = []
        
        
    def push(self,val):
        if len(self.stack) == 0:
            self.stack.append(val)
        else:
            temp = []
            while self.stack[-1] < val:
                temp.append(self.stack.pop())
                if len(self.stack) == 0:
                    break
            self.stack.append(val)
            while len(temp) > 0:
                self.stack.append(temp.pop())
                

s = Stack()

s.push(10)
s.push(4)
s.push(6)
s.push(1)
s.push(20)
print (s.stack)
