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

def inorderItrative(root):
    result = []
    current = root
    stack = []
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
            
        current = stack.pop() # cuurent is none 
        result.append(current.val)
        current = current.right
    return result

print(inorderItrative(root))


