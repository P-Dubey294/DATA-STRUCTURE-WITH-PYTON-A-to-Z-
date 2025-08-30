class Node:
    def __init__(self, vlaue):
        self.val = vlaue
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

#print the Node 
def display(root):
    if root is None:
        return None
    print(root.val, end=" ")
    display(root.left)
    display(root.right)
display(root)

#sum of node 

def sumOfRootNode(root):
    if root is None:
        return 0
    return root.val + sumOfRootNode(root.left) + sumOfRootNode(root.right)
result = sumOfRootNode(root)
print("\nSum of all nodes:", result)

# Maximum of Node 
def maxNode(root):
    if(root is None) or (root.left is None and root.right is None): 
        return root
    max_left = maxNode(root.left)
    max_right = maxNode(root.right)

    return max(max_left, max_right, root,
              key = lambda x: x.val if x else float('-inf'))

print("Maximum node value:", maxNode(root).val)

#find hight of the node 
def max_hight(root):
    if root is None:
        return -1
    return 1 + max(max_hight(root.left), max_hight(root.right))
print("Hight of the node is", max_hight(root))

#size of the tree
def sizeOfTheTree(root):
    if root is None:
        return 0
    return sizeOfTheTree(root.left) + sizeOfTheTree(root.right) + 1
print("The size of the tree is ",sizeOfTheTree(root))