def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    else :
        pivot = arr [len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
arr = [ 10 ,7 ,8 ,9 ,1 ,5]
sorted_arr = quick_sort(arr)
print("sorted array is" ,sorted_arr)

# Quick Sort in efficent way 

def partition(arr, low, high):
    pivot = arr[high]
    i = low -1 # tracking the possition of element saller than pivot
    for j in range(low , high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j],arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1 

def Quick_Sort(arr, low, high):
    if low < high :
        pi = partition (arr , low , high)
        Quick_Sort(arr, low , pi-1)
        Quick_Sort(arr, pi+1, high)

arr = [ 10 ,7 ,8, 9, 1, 5 , 11]
Quick_Sort(arr , 0, len(arr)-1)
print("efficient sorted array is :", arr)



