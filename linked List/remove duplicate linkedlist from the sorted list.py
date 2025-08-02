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
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(40)

print("Original List:")
print_Linkedlist(head)

# Function to remove duplicates from sorted list
def del_duplicate(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head.next

    while fast:
        if slow.data == fast.data:
            slow.next = fast.next
            fast = fast.next
        else:
            slow = slow.next
            fast = fast.next

    return head

# Remove duplicates
head = del_duplicate(head)

print("List After Removing Duplicates:")
print_Linkedlist(head)

        

        