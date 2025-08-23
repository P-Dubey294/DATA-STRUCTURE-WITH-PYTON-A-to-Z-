class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        # Push into min_stack if it's empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1] if self.stack else None
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

    
minstack = MinStack()
minstack.push(1)
minstack.push(2)
minstack.push(3)
minstack.push(4)
minstack.push(0)
minstack.push(4)

print("Top:", minstack.top())       
print("Min:", minstack.getMin())    
minstack.pop()
print("Min after pop", minstack.getMin())

minstack.pop()
print("Min after pop:", minstack.getMin())


