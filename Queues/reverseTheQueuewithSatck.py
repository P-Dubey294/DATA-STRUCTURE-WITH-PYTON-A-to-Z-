from collections import deque
def reverse_queue(q):
    stack = []

    while q:
        stack.append(q.popleft())
    
    while stack:
        q.append(stack.pop())
    
    return q

queue = reverse_queue(deque([1,2,3,4,5,6,7,8,9]))
print(queue)
