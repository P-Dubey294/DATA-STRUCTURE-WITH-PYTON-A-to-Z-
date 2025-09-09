class Node:
    def __init__(self, data):
        self.val = data
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

def preorderIterative(root):
    result = []
    if root is None:
        return result
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
print(preorderIterative(root))
