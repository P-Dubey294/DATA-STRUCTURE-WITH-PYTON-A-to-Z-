class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

from collections import deque
def printRightBoundary(root):
    result = []
    if root is None:
        return result
    
    queue = deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()

            if node.left:
                 queue.append(node.left)
            if node.right:
                 queue.append(node.right)

            if i == size-1:
                result.append(node.val)
    return result

rightsideBoundaryView = printRightBoundary(root)
print("The Right Side Boundary of the Tree is :",rightsideBoundaryView)







    