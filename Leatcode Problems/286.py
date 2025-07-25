# finding the duplicate values 
def findduplicate(nums):
    
    sorted_array =  sorted(nums)
    for i in range (1, len(sorted_array)):
        if sorted_array [i-1] == sorted_array[i]:
            return  sorted_array[i]
    
    return -1
arr = [1,2,3,4,4,5,6,7]
print(findduplicate(arr))
