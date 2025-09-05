class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Tree creation
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

def invertBinaryTree(root):
    if root is None:
        return None
    
    # Swap children
    root.left, root.right = root.right, root.left
    
    # Recurse
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    
    return root

# Helper to check result (preorder traversal)
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

print("Original Tree Preorder: ")
preorder(root)

invertBinaryTree(root)

print("\nInverted Tree Preorder: ")
preorder(root)



     


    


