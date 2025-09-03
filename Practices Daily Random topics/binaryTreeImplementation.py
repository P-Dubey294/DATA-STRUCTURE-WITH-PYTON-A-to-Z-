class Node:
    def __init__(self,value):
        self.val = value
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

# ptint the tree 
def display(root):
    if root is None:
        return None
    print(root.val, end=" ")
    display(root.left)
    display(root.right)

display(root)

