class Sort_Stack:
    def __init__(self):
        self.s1 = []

    def push(self,val):
        temp_stack = []
        if len(self.s1) == 0:
            self.s1.append(val)
        else:
            print (self.s1)
            while val > self.s1[-1]:
                temp_stack.append(self.s1.pop())
                if len(self.s1) == 0: break
            self.s1.append(val)
            while len(temp_stack) > 0:
                self.s1.append(temp_stack.pop())


s = Sort_Stack()

for i in [7,6,8,10,2]:
    s.push(i)
print (s.s1)
