# finding a misiing number 
def find_missing(nums):
    
    n = len(nums)
    expected_sum = n*(n+1)//2
    actual_sum = sum(nums)

    return expected_sum-actual_sum

data =  [0,2,3,4,1,6,7,8,9]
print(find_missing(data))