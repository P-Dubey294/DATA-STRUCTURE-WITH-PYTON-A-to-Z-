def push(arr, val):
    arr.append(val)

def pop(arr):
    if (len(arr) == 0):
        print("trying to delete this is not present")
        return
    arr.pop()

def top(arr):
    if (len(arr) == 0):
     print ("Nothing to present any")
     return str(-1)
    return arr[len(arr) - 1]

stack = []
top(stack)
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
pop(stack)
print(pop(stack))
