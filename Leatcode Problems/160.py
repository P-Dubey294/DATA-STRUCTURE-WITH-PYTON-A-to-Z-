class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Shared nodes
intersect = ListNode(7)
intersect.next = ListNode(8)

# List A: 1 -> 2 -> 3 -> 7 -> 8
headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = intersect

# List B: 6 -> 7 -> 8 (intersects at 7)
headB = ListNode(6)
headB.next = intersect

def getIntersectionNode(headA, headB):
    visited = set()
    current = headA
    while current:
        visited.add(current)
        current = current.next

    current = headB
    while current:
        if current in visited:
            return current
        current = current.next
    return None

# Run it
intersection_node = getIntersectionNode(headA, headB)
if intersection_node:
    print("Intersection at node with value:", intersection_node.val)
else:
    print("No intersection")

