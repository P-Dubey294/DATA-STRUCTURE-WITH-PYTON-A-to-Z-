from collections import deque

def remove_even_possition(q):
    temp_queue = deque()
    index = 0

    while q:
        if index%2 == 0:
            temp_queue.append(q.popleft())
        else:
            q.popleft()
        index+=1
    return temp_queue

dequeue =  deque([10,20,30,40,50,60,70])
print(remove_even_possition(dequeue))

    


