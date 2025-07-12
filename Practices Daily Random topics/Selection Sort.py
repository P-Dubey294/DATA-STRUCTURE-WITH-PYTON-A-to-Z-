def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [22,44,66,33,11,55]
print(arr)
SelectionSort(arr)
print(arr)