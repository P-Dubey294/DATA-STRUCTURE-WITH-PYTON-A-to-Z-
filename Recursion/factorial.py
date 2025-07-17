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
