''' print a factorial number by using 
recusrion '''
def Facroial (n):
    if n == 0:
        return 1 
    else:
     return n * Facroial(n-1)
print(Facroial(6))


# print the fibonacci Series 
def fibonacci(n):
   if n <= 1:
          return n
   else:
      return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))


# print the sum of array 
def SumofArray(arr , n):
    if n == 0:
        return 0
    else:
        return SumofArray(arr, n-1) + arr[n-1]
    
arr =[1,2,3,4,5]
print(SumofArray(arr,len(arr)))


# Number of ways to climb Strair 
def Stair(n):
    if n == 0 :
        return 1
    if n < 0 : 
        return 0
    else:
        return Stair(n-1)+ Stair(n-2)
n = 5
print(Stair(n))


#Print Numbers from 1 to N
def print_asc(n):
    if n == 0:
        return
    print_asc(n - 1)
    print(n)
print_asc(5)


#Print Numbers from N to 1
def print_desc(n):
    if n == 0: 
        return n
    else :
       print(n)
       print_desc(n-1)
print_desc(5)


#Binary Serching using recursion ...s
def binarySerch(arr , left , right , target):
    while left > right:
        return -1 
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid 
    elif arr[mid] > target:
        return binarySerch(arr , left, mid-1, target)
    else: 
        return binarySerch(arr, mid+1, right, target)
arr=[1,3,5,7,9,11,33,66,77,55]
target = 11
print(binarySerch(arr, 0, len(arr)-1, target))


# Subset OF string 
def SubsetOfString(s , cureent ="" , index = 0):
    if index == len(s): # Base Condition 
        print(cureent)
        print("___________")
        return -1
    #there are tow condition inculded or not 
    SubsetOfString(s, cureent + s[index], index+1)
    SubsetOfString(s, cureent, index+1)
ex = "abc"
print(SubsetOfString(ex))

    


