class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def PathSum3(self, root, targetSum: int) -> int:
        if not root:
            return 0

        # DFS to count paths starting from this node
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.data
            totalPath = 1 if current_sum == targetSum else 0

            # keep exploring left and right
            totalPath += dfs(node.left, current_sum)
            totalPath += dfs(node.right, current_sum)

            return totalPath

        # Count all paths starting from every node
        def countAllPath(node):
            if not node:
                return 0

            totalpath = dfs(node, 0)  # paths starting from this node
            totalpath += countAllPath(node.left)  # explore left subtree
            totalpath += countAllPath(node.right) # explore right subtree

            return totalpath

        return countAllPath(root)
# Build tree
root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(11)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

print(root.PathSum3(root, 7)) 