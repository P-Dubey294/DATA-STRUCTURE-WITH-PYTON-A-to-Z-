#functions -> it is bolck of code that will be called and reused again & again .

def student ():
    print("My Name Is pratham kumar dubey and  iam 23 year old ")
student()

''' Function Passing with the Argument and calling with argument '''

def addfunc(a,b): #function passing with the parameter 
    sum = a + b
    return sum
print(addfunc(5,6))  #function calling with the argument 

#Example :
def Multiplication (a,b,c):
    multiply = a * b * c 
    return multiply
print(Multiplication(3,4,2))

'''function in varible 
there are tow types of varible in function 
1> local scop (varibles)
2> Global scop (varibles) '''

# local scope are decalre inside the function 
# global scope are declare outside the function 

'''example '''

x = 101  #global varible
def typeVaribleFunc():
    x = 102 # local varible
    print(x) # calling local varible
typeVaribleFunc()
print(x) # calling global varible



