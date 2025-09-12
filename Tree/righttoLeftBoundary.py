class Node:
    def __init__(self, data):
        self.data = data
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

from collections import deque
def right_to_left_Traversal(root):
    if root is None:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
right_to_left_Traversal(root)
    