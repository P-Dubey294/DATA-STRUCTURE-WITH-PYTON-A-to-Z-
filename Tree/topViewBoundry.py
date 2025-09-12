class Node:
    def __init__(self, data):
        self.data = data
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

from collections import deque
def top_view (root):
    if root is None:
        return 
    hd_map = {}
    queue = [(root,0)]
    while queue:
        node , hd = queue.pop(0)
        if hd not in hd_map:
            hd_map[hd] = node.data
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    
    for hd in sorted(hd_map):
        print(hd_map[hd], end = " ")

top_view(root)



    