class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Tree creation
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)


def findLargestDiameter(root):
    diameter = [0]   # use list so inner function can modify it

    def depth(node):
        if not node:  # base case
            return 0
        left = depth(node.left)
        right = depth(node.right)

        # update diameter
        diameter[0] = max(diameter[0], left + right)

        # return height
        return max(left, right) + 1

    depth(root)
    return diameter[0]


# test
print("Largest Diameter:", findLargestDiameter(root))
