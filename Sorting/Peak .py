'''
Given an array arr[] of size n, find a peak element. 
An element is a peak if it is greater than or equal 
to its neighbors.
Input: arr = [5, 10, 20, 15]
Output: 20
Explanation: 20 is greater than both 10 and 15
'''

# example 
def Peak_Element(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    for i in range(1, n-1):
        if ((arr[i] > arr[i+1] )and (arr[i] > arr[i-1])):
            return i
    return -1  # If no peak is found

arr = [1,2,3,5]
print(arr)
print(Peak_Element(arr))
  
#using Liner Serching 

def get_peak_element(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and \
           (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid

        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

arr = [5, 2, 1]
print(get_peak_element(arr))  # Output: 0 (since 5 is a peak)

    

    

    