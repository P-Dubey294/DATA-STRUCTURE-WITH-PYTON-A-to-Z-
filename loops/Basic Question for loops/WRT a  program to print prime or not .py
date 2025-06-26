num = int (input ("Please enter the value"))

isPrime = True
if (num <=1):
    isPrime = False 

for i in range (2, int(num/2)+1):
    if num%1 ==0:
        isPrime = False
    break
print (" The prime number is :", isPrime)
        

