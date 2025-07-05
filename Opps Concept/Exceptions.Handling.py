'''what is an exceptions ...
=> Exeception is nothing but its a unexpected Behaviour 
which is gracefully handling the error during the execution of the program 
withuot crashing it .'''

'''Syntax of Exception Handling'''
'''
try:
     # Code that may raise an error
except :
    # Code that runs if an error occurs
else:
    # Code that runs if no error occurs
finally:
    # Code that always runs, error or not
    print("Cleanup code here.") '''

#Example of Exception Handling ... 
try:
    num = int(input("Enter a number "));
    result = 10 / num ;
    print("result is",result);
except ZeroDivisionError:
    print("zero is not dvisible by any number");
except ValueError :
    print ("  Enter a valid number");
finally:
    print("Program Ended!")






'''Try block using else '''
num = int(input("Please Enter a number"))
try:
    result = 5 / num;
except ZeroDivisionError:
    print("zero cant be divisible please enter a valid number")
else:
    print("result is" , result)





'''Asert keyword --> 
using when riase the exception '''
write = int(input("enter a number is"))
def cube_Root(num):
    assert num >= 0, "enter a positive number"
    return num**(1/3)

try:
    print(cube_Root(8))
    print(cube_Root(-8))
except AssertionError as e:
    print(e)
print("Last Line")


# Coustome Exceptions 
from ast import arguments
class EmptyExceptions (RuntimeError):
    def __init__(self,argument):
        self.argument = argument
        var = ""
try:
    raise EmptyExceptions("This varibles is empty Strings")
except EmptyExceptions as e:
    print(" Unexpected errors!", e)
else:
    print("this program will be end!")

