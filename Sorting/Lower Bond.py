'''Qs> Given a sorted integer array and an integer "x" 
find lower bond of x 

let undertand the Qs > 
we have a given string or array ie [2,2,2,2,5,5,8] 
and find the gretter or eqaul value to the given value x and return 
there index . 
x = 4 
O/p is => 4 index return '''

#Liner Serch 
def LowerBond(arr , x):
    for i in range (len(arr)):
        if arr[i] > x:
            return i
        
    return i + 1

arr = [ 2,2,2,2,5,5,8]
print(arr)
x = 5
print(LowerBond(arr, x))


# Binary Serch
def lowerBond(arr ,x):
    low = 0 
    high = len(arr)-1
    ans = len(arr)

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid -1 
        else:
            low = mid + 1
    return ans
    
arr = [2,2,2,2,5,5,8]
x = 0
print(lowerBond(arr , x))



