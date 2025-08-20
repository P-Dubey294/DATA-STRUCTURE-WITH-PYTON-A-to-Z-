class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack = [value] + self.stack
    
    def pop(self):
        self.stack.pop(0)
    
    def result(self):
        return self.stack
    
S = Stack()

S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)

print("After Pusing",S.result())
S.pop()
print("After poping", S.result())
