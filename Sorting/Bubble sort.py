'''Bubble sort i aa comparision base algorithm 
its adjacent wihch move largest elelemt to the right '''

def Bubble_sort(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range (n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [ " a " , " b" , " c " , " f"  , " e" , " d"]
print(arr)
Bubble_sort(arr)
print(arr)

''' sorting algorithm  is very very worst case  beacuse its n sqaure
times executes and there time complexity is  O (n sqaure). '''

'''to make better efficient or enhacned the sorting algorithm 
for makimg time complexity efficient '''

def Bubble_sort_enhanced(arr):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break
arr = [1,2,3,4,5]
print(Bubble_sort(arr))




