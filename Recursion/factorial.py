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