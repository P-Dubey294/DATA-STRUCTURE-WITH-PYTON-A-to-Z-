''''sorting a linkedlist using merged sort'''

#Merging of two linkedlist 
class listNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

def getMergeOfTwoLinkedlist(list1, list2):
    dummy = listNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next 
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next 

        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
    return dummy.next

# find mid 
def get_Middle(head):
    if not head:
        return head 
    slow = head
    fast = head 

    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow

#using merge sort 
def mergeSort(head):
    if not head or not head.next:
        return head
    #find mid 
    mid = get_Middle(head)
    #break the linkedlist 
    next_to_mid = mid.next
    mid.next = None

    left = mergeSort(head)
    right = mergeSort(next_to_mid)

    #merge sorted linkedlist 
    sorted_list = getMergeOfTwoLinkedlist(left,right)
    return  sorted_list


    



