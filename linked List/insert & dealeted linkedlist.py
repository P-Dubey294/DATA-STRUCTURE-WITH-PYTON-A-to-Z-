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

'''print_linkedlist(head)'''

        
# Adding new node at the beagninig of the linkedlist
def print_insert_At_First(head,value):
    new_node = Node(value)
    new_node.next = head
    return new_node

head = print_insert_At_First(head,600)
'''print_linkedlist(head)'''

# Adding new node at the last of  (end of) the linkedlist
def print_insert_At_Last(head,value):
    new_node = Node(value)
    if head is None:
        return new_node
    
    current = head
    while current.next is not None:
        current = current.next 
        
    current.next = new_node

    return head  
head = print_insert_At_Last(head, 900)
'''print_linkedlist(head)'''


# Adding new node at the specefic possition of the linkedlist
def insert_at_position(head, value, position):
    new_node = Node(value)

    if position ==1 :
        new_node.next = head
        return new_node
    
    current  =  head
    for i in range(1, position -1 ):
        if current is None :
            print(" Invalid position")
            return head
        
        current = current.next

    if current is None:
        print(" Invalid position")
        return head
    
    new_node.next = current.next
    current.next = new_node

    return head

'''head = insert_at_position(head,8, 3)'''
print_linkedlist(head)



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
head = del_linkedList_At_Last(head)
print_linkedlist(head)

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



