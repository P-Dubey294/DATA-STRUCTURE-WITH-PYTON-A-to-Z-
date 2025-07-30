#creating a node 
class Node :
    def __init__(self, value):
        self.data = value
        self.next = None

#Creating a linkedlist 
class linkedlist:
    def __init__(self):
        self.head = None
        #addding new node 
    def add_Node(self,value):
            new_node = Node(value) # with help pf Node class for creating a node
            #creating head node 
            if self.head is None:
                self.head = new_node
            else:
                current = self.head # current is head 
                while current.next is not None:
                    current = current.next   # updating the current when cureent is not a none
                current.next = new_node

l1 =  linkedlist()
l1.add_Node(value=10)
l1.add_Node(value=15)
l1.add_Node(value=20)

#creating a linkedlist
print(l1.head)
print(l1.head.data)
print(l1.head.next.data)
print(l1.head.next.next.data)

#diisplay a linkedlist in iteratively 
def print_Linked_list(head):
     current = head
     while current is not None:
        print(current.data)
        current = current.next

print_Linked_list(l1.head)


#diisplay a linkedlist in recursively.
def Linked_list_Recursively(head):
    if head is None:
        return
    print(head.data)
    Linked_list_Recursively(head.next)
Linked_list_Recursively(l1.head)


#find the length of the linkedlist
l2 = linkedlist()
for i in range(10):
    l2.add_Node(i*2);
print_Linked_list(l2.head)


#find the length of the linkedlist itratively 
def find_length_itratively(head):
     length = 0 
     while head is not None:
        length+=1
        head = head.next 
        return length
print(find_length_itratively(l2.head))
            
            
#find the length of the linkedlist Recursively
def find_length_Recursively(head):
     if head is None:
            return 0
     return 1 + find_length_Recursively(head.next)

print(find_length_Recursively(l2.head))



