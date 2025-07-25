# finding a misiing number 
def find_missing(nums):
    
    n = len(nums)
    expected_sum = n*(n+1)//2
    actual_sum = sum(nums)

    return expected_sum-actual_sum

data =  [0,2,3,4,1,6,7,8,9]
print(find_missing(data))

'''Time complexity is 0(nlogn)'''

#using cycyle sort 
def Finding_MIssing(nums):
    n = len(nums)
    i = 0 
    
    while i < n :
        correct_index = nums[i]
        if (nums[i] < n )and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] , = nums[correct_index], nums[i]
        else:
            i+=1

        for i in range(n):
            if nums[i] != i:
                return i  
            
        return n
arr = [0,1,2,5,6,7,3]
print(Finding_MIssing(arr))