class Node:
    def __init__(self, value):
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

# Depth First Traversal ( PreOrder ie Node - left - right)

def preOrder(root):
    if root is None:
        return
    print(root.val, end =" ")
    preOrder(root.left)
    preOrder(root.right)

print("This is Preorder",preOrder(root))


# Depth First Traversal ( Inorder ie left - Node - right)

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val, end =" ")
    inOrder(root.right)

print("This is Ineorder",inOrder(root))

# Depth First Traversal ( PostOrder ie left - right - Node)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val, end =" ")

print("This is Postorder",postOrder(root))