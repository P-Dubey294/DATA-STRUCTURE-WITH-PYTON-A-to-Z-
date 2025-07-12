def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [22,44,66,99,11,33,77,55,88]
print("Before sorting", arr)
SelectionSort(arr)
print("After Sorting", arr)

        


# Insertion Sort 
''' start with  the first element ausmining it is already sorted 
take the next element & repelce it with element it is sorted sections ,
moving the one postions yo right to make space if necessary 
insert the element in its corrrect position 
repeted until all element are sorted  '''

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [12, -11, 136, 5, 6]
print("Before sorting", arr)
InsertionSort(arr)
print("After Sorting", arr)



