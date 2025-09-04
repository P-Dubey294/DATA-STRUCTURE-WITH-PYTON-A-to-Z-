class Node:
    def __init__(self, vlaue):
        self.val = vlaue
        self.left = None
        self.right = None

#example of binary Tree 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

# print nth level of element into the node  
from collections import deque

def nthlevelElement(root , n):
    if root is None:
        return None
    
    level = 0
    queue = deque([root])

    while queue:
        level_size = len(queue)
        if level == n:
            for i in range(level_size):
                node = queue.popleft()
                print(node.val, end= " ")
            return
            
        for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        level +=1
    print("level is not found")

nthlevelElement(root, n=2)





