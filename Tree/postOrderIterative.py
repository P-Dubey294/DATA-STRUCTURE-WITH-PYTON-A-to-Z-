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

def PostOrderIterative(root):
    result = []
    if root is None:
        return result
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        result.append(s2.pop().val)
    return result
print(PostOrderIterative(root))
