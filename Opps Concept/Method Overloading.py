'''
⚠️ Important:
Python does not support method overloading in the traditional 
sense like Java or C++. If you define multiple methods with the
same name in a class, only the last one will be used—the previous
ones get overridden.
'''

class Calculator :
    def Add(self , a ,b ):
        return a + b ;
    def Add (self, a , b, c ):
        return a + b + c ;
cal = Calculator()
print(cal.Add(5,5,7)); # in python world explicit method overloading are not supported.
#print(cal.Add(5,6)) 

'''
❓ Why doesn't Python support method overloading like Java or C++?
🧠 1. Dynamic Typing
Python is a dynamically typed language, which means:

You don’t declare variable or parameter types.
All type checking happens at runtime, not at compile time.

🧠 2. Definations 
last defination will be called it  and implicallity we can achive this behaviour ,

'''

class Calculator :
    def Add(self , a ,b , c=0):#Default argument will be used 
        return a + b + c ;
cal = Calculator()
print(cal.Add(5,5,7)); 
print(cal.Add(5,6)) 



