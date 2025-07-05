'''Operator overloading allows you to redefine 
the meaning of built-in operators (like +, -, *, etc.) 
for user-defined objects (classes).'''

class ComplexityNium :
    def __init__(self , x ,y):
        self.x = x
        self.y = y
        
    def __add__(self, C): 
        return self.x + C.x, self.y + C.y
    
c1 = ComplexityNium(5,6);
c2 = ComplexityNium(7,2);

print (c1 + c2)

''' jb bhhi hum Operator overloading +,_,* ko use krete hain tho 
corresponding inbuilt magical operator ko extend kiya jata hain 
use manual operator overloading khte hain '''

# another Example 

class NUM :
    def __init__(self, a , b):
        self.a = a 
        self.b = b

    def __add__(self, U):
        return self.a + U.a, self.b + U.b

num1 = NUM(5,2)
num2 = NUM(4,2)
print(num1 + num2)
