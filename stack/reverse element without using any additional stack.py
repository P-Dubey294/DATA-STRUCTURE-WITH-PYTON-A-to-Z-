def top(arr):
    return arr[len(arr)-1]

def reverse(stack):
    if len(stack)==1:
        return
    
    x = top(stack)
    stack.pop()

    reverse(stack)

    insertAtlast(stack, x)

def insertAtlast (stack , val):
    if len(stack)==0:
        stack.append(val)
        return
    
    t = top(stack)
    stack.pop()
    
    insertAtlast(stack, val)
    stack.append(t)


stack = []
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)
reverse(stack)
print(stack)
