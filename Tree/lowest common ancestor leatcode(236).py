class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    # If root matches one of the nodes, return root
    if root == p or root == q:
        return root

    # Search left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both sides return a node, root is the LCA
    if left and right:
        return root

    # Otherwise return whichever side is not None
    return left or right

    
# Create tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left        # Node 5
q = root.right       # Node 1

lca = lowestCommonAncestor(root, p, q)
print("LCA:", lca.data) 

    
    