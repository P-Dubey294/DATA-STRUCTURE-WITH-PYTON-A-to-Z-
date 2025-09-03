class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)

from collections import deque
def breadthFirstTraversal(root):
    if root is None:
        return
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print(breadthFirstTraversal(root))
            
    

