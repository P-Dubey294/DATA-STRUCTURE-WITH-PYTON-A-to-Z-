'''✅ Problem 1 (Easy)
Q: Sort the array using Bubble Sort.
Input: [4, 2, 1, 5, 3]
Expected Output: [1, 2, 3, 4, 5]

'''

def bubblesort(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        is_swaped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                is_swaped = True
                count = count + 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not is_swaped:
            break
    return count

print(bubblesort([5,4,3,2,1]))