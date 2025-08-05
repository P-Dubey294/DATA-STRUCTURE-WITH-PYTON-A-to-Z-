# find the middle node of the linkedclist 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle_Element(head):
    if head is None or head.next is None:
        return head

    # Step 1: Find the length
    length = 1
    current = head
    while current.next is not None:
        current = current.next
        length += 1

    # Step 2: Find middle
    middle = length // 2
    current = head
    while middle:
        current = current.next
        middle -= 1

    return current
middle = findMiddle_Element(head)
print("Midddle node value",middle.val)







