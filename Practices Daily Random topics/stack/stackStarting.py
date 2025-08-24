class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack = [data] + self.stack
    
    def pop(self): 
        self.stack.pop()
    
    def printResult(self):
        return self.stack
    
S = Stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
S.push(50)
print("After PUSH the element result is :",S.printResult())

S.pop()
print("After POP the element result is :", S.printResult())
        