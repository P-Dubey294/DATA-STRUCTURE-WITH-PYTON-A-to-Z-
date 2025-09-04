class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.value != q.value:  # fixed here
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Tree 1
p = Node(1)
p.left = Node(2)
p.right = Node(3)

# Tree 2
q = Node(1)
q.left = Node(2)
q.right = Node(3)

print(isSameTree(p, q))  # ✅ Output: True
