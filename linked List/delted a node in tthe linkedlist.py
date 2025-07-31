#node 
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

#printing
def print_linkedlist(head):
    current = head
    while current is not None:
        print(current.data, end ="")
        current = current.next

# Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

'''print_linkedlist(head)'''

# Deleting a node at the beagninig of the linkedlist 
def del_linkedlist_At_First(head):
    if head is None:
        print("No Element in the linkedlist")
        return None
    
    new_node = head.next 
    head.next = None
    return new_node

'''head = del_linkedlist_At_First(head)'''
print_linkedlist(head)


# Deleting a node at the last (end) of the linkedlist 
def del_linkedList_At_Last(head):
    if head is None:
        print(" there is no element in the linkedlist")
        return None
    
    if head.next is None:
        return None
    
    current = head
    while current.next.next is not None:
        current = current.next

    current.next = None

    return head
'''head = del_linkedList_At_Last(head)
print_linkedlist(head)'''

# Deleting a node at the specefic possitions of the linkedlist
def del_At_Specefic_Possition(head,value):
    if head is None:
        print(" there is no eleement")
        return None
    
    if head.data == value:
        new_head = head.next 
        head.next = None
        return new_head
    
    current = head
    while current.next is not None and current.next.data != value:
        current = current.next

    if current.next is None:
        print("value is not found")
        return head
    
    temp = current.next 
    current.next = current.next.next 
    temp.next = None
    return head
head = del_At_Specefic_Possition(head, 30)
print_linkedlist(head)