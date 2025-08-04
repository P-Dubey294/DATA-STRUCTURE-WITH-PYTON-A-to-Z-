#this is now how we creting a node 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None

# insert a node at the beagining of the linkedlist

class insert_at_start:
    def __init__(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

# insert a node at the last (end) of the linkedlist
def insert_at_end(self, data):
    new_node = Node(data)
    if self.head == None:
        self.head = new_node
    else:
        temp = self.head 
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

#insert a node at specefic Possitions on the linkedlist.
def insert_at_possition(self, data, possition):
    new_node = None(data)
    if possition == 0:
        self.insert_at_start(data)
    else:
        temp = self.head
        for i in range(possition -1 ):
            temp = temp.next 
            if temp is None:
                raise IndexError("Possitions out of box")
            new_node.next = temp.next 
            new_node.prev = temp
            if temp.next :
                temp.next.prev = new_node
                temp.next = new_node
                
            return new_node




