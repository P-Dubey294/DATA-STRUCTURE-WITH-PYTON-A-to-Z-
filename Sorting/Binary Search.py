'''
what is serch 
 The process of finding a specefic item or value within
 a collection of items .
 
 There are tow types of Serching 
 a> Binary Serching 
 b> Linear Serching 
 
 Binary Searching 
 => An efficient Method finding an element in sorted array by repatedly 
 dividing the Serch space in half 
 '''
 #example 

def BinarySerch(arr, Target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == Target:
            return mid
        elif arr[mid] < Target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(arr)
Target = 17
result = BinarySerch(arr, Target)
print("Index of target:", result)
    
        

        

