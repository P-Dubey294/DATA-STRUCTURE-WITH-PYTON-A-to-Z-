def Selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        # Swapping the element
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [44,66,99,22,33,11,55]
print("Before sorting:", arr)
Selectionsort(arr)
print("After sorting:", arr)




