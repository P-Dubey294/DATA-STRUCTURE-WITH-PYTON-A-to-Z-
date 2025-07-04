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
