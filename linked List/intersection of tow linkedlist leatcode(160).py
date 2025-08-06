class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# intersect at 7 (shared Nodes)

intersect = listNode(7)
intersect.next = listNode(8)

# list (headA) : 1-> 2 -> 3 -> 7 -> 8
headA = listNode(1)
headA.next = listNode(2)
headA.next.next =listNode(3)
headA.next .next.next = intersect

# List (headB) ie listB : 6-> 7-> 8 (intersect at 7)
headB = listNode(6)
headB.next = intersect

#main loogic
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
    
#run it
Intersection_node = getIntersectionNode(headA, headB)
if Intersection_node:
    print( "intersection node at value :", Intersection_node.val)
else:
    print(" there is no intersection")


''' In these approch there time complexity will be o (n + m) and space complexity is will be o(n) '''

def getIntersection_Node(headA, headB):
    #find length A and B
    lenA, lenB = 1,1
    currentA , currentB = headA, headB
    while currentA.next:
        lengthA+=1
        currentA = currentA.next
    while currentB.next:
        lengthB+=1
        currentB = currentB.next
        #differnce lengthA & lengthB
        diff = (lengthA - lengthB)
        if lengthA > lengthB:
            headA = headA.next
            diff -=1
        elif lengthB > lengthA:
            headB = headB.next 
            diff -=1
        #both length are equal then 
        while(lengthA != lengthB):
            headA = headA.next 
            headB = headB.next 
        return headA
    
        





        


