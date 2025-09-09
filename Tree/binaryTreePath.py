class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

def binaryTreePath(root):
    paths = []
    
    def helper(node, path):
        if not node:
            return
        # Add current node value in list instead of string
        path.append(node.value)
        
        # If it's a leaf, append a copy of path
        if not node.left and not node.right:
            paths.append(path[:])
        else:
            helper(node.left, path)
            helper(node.right, path)
        
        # Backtrack
        path.pop()
    
    helper(root, [])
    return paths

print(binaryTreePath(root))

    




