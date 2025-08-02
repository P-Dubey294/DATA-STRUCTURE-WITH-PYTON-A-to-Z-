class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def print_Linkedlist(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Creating Linked List: 10 -> 10 -> 20 -> 30 -> 40
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original List:")
print_Linkedlist(head)

# Rotate the linkedlist 
def Rotate_Linkedlist(head, k):
    if not head:
        return head

    # Step 1: Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Normalize k
    k = k % length
    if k == 0:
        return head

    # Step 3: Find new_tail (at length - k - 1)
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Step 4: Rearrange pointers
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head

    return new_head

print("After rotating the linked list by k=2:")
head = Rotate_Linkedlist(head, k=2)
print_Linkedlist(head)
        



