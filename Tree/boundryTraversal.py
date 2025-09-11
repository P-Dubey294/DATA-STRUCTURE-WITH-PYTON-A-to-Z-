class Node:
    def __init__(self, data):
        self.data = data
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

def leftBoundry(root, boundary):
    if root is None:
        return
    if root.left:
        boundary.append(root.data)
        leftBoundry(root.left, boundary)    
    elif root.right:
        boundary.append(root.data)
        leftBoundry(root.right, boundary)

def rightBoundry(root, boundary):
    if root is None:
        return 
    if root.right:
        boundary.append(root.data)
        leftBoundry(root.right, boundary)
    elif root.left:
        boundary.append(root.data)
        boundary.append(root.left, boundary)

def printLeavesNode(root,boundary):
    if root is None:
        return
    printLeavesNode(root.left, boundary)
    if root.left is None and root.right is None:
        boundary.append(root.data)
    printLeavesNode(root.right, boundary)

def printBoundary(root):
    boundary = []
    if root is None:
        return boundary
    boundary.append(root.data)
    leftBoundry(root.left, boundary)
    printLeavesNode(root.left, boundary)
    printLeavesNode(root.right, boundary)
    rightBoundry(root.right, boundary)
    return boundary

boundary_Traversal =  printBoundary(root)
print('Boundary Traversal Is:',boundary_Traversal)


    



