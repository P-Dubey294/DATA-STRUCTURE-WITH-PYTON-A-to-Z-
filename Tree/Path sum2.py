class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)


def pathsum(root, targetSum):
    def dfs(node, currentPath, currentSum):
        if not node:
            return

        currentPath.append(node.data)
        currentSum += node.data
        
        # check if it's a leaf and sums match
        if node.left is None and node.right is None and currentSum == targetSum:
            result.append(list(currentPath))

        # continue DFS
        dfs(node.left, currentPath, currentSum)
        dfs(node.right, currentPath, currentSum)

        # backtrack
        currentPath.pop()
    
    result = []
    dfs(root, [], 0)
    return result


print(pathsum(root, 12))



