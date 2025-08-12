class Stack:
    # this is a constrcutor 
    def __init__(self):
        self.stack = []
    # this is a push operation
    def Push(self, value):
        self.stack.append(value)
    # this is pop opperation 
    def pop(self):
        self.stack.pop()
    # print result function
    def printResult(self):
        return self.stack
    
s = Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(40)
s.Push(50)

print("Pusing the Element :- ",s.printResult())
s.pop()
print("Poping the Element :- ",s.printResult())

