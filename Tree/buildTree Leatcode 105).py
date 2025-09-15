class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root

# -------- Traversals to check tree --------
def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right)

def levelOrderTraversal(root):
    if not root:
        return []
    from collections import deque
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        res.append(node.data)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


# Example usage
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(preorder, inorder)

print("✅ Inorder Traversal:", inorderTraversal(root))
print("✅ Level Order Traversal:", levelOrderTraversal(root))

