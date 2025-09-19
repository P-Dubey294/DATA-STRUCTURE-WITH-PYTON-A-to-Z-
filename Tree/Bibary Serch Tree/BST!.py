class Node:
    def __init__(self, value):
        self.val = value
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

def searchBT(root, val):
    if root is None:
        return None

    if root.val == val:
        return root

    if root.val > val:
        return searchBT(root.left, val)
    else:
        return searchBT(root.right, val)

# Call
node = searchBT(root, 3)
print(node.val if node else "Not found")

        