from collections import deque

def reverse_dequeue(q):
    stack = []
#push the element queue to stack
    while q:
        stack.append(q.popleft())
    
#pop the element stack to queue
    while stack:
        q.append(stack.pop())
    return q

queue = reverse_dequeue(deque([1,2,3,4,5,6,7,8,9]))
print(queue)