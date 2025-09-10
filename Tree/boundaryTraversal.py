class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

# Left Boundary (excluding leaf nodes)
def leftBoundary(root, boundary):
    if root:
        if root.left:
            boundary.append(root.data)
            leftBoundary(root.left, boundary)
        elif root.right:
            boundary.append(root.data)
            leftBoundary(root.right, boundary)

# Right Boundary (excluding leaf nodes, collected in reverse)
def rightBoundary(root, boundary):
    if root:
        if root.right:
            rightBoundary(root.right, boundary)
            boundary.append(root.data)  # add after recursion
        elif root.left:
            rightBoundary(root.left, boundary)
            boundary.append(root.data)

# Print all leaf nodes
def printLeaves(root, boundary):
    if root:
        printLeaves(root.left, boundary)
        if root.left is None and root.right is None:
            boundary.append(root.data)
        printLeaves(root.right, boundary)

# Combine all parts
def PrintBoundary(root):
    boundary = []
    if not root:
        return boundary

    boundary.append(root.data)  # root

    # Left boundary (excluding root and leaves)
    leftBoundary(root.left, boundary)

    # All leaves
    printLeaves(root.left, boundary)
    printLeaves(root.right, boundary)

    # Right boundary (excluding root and leaves)
    rightBoundary(root.right, boundary)

    return boundary


boundary_Traversal = PrintBoundary(root)
print("Boundary Traversal:", boundary_Traversal)
