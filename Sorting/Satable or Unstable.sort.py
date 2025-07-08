# Stable or Unstable sorting
# Stable sorting ? 
''' => A sortihg algorithms in which the element are equal and 
 there realtive element in order ie ( 1 before 1` ) called 
stable sort'''

#Example of Stable Sort is Bubble sorting becuse 
# [ 3,4,5,1,2,] swappimg only happed when left > right 

def Bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break

arr = [ 1, 1, 4, 6, 7, 3, 9]
print(arr)
Bubble_sort(arr)
print(arr)

#Unstable Sorting 
''' 
=>A sortihg algorithms in which the element are changes and 
there realtive element in order ie ( 1' before 1 ) called unstable 
sort '''