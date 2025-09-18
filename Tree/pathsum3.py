class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def pathSum3(self,root,targetSum):
        from collections import defaultdict

        def DFS(node,current_sum):
            nonlocal count

            if not node:
                return 
            
            current_sum += node.data

            if current_sum == targetSum:
                count +=1

            count += prefix_sum[current_sum - targetSum]
            prefix_sum[current_sum] +=1

            DFS(node.left, current_sum)
            DFS(node.right, current_sum)

        count = 0
        prefix_sum = defaultdict(int)
        DFS(root,0)
        return count

root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.left = None
root.right.right = Node(11)


print(root.pathSum3(root, 8))
            
        
    