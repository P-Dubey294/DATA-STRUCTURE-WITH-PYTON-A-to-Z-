''' what is acesss modifire 
access modifiers are used to control the
visibility or accessibility of class members 
(variables and methods).

There are tow tyoe of Acesse Modifire in python  
1> Private 
2> Public 


# Public 
=> Syntax: No underscore (default)
Accessible: Everywhere (inside and outside the class)  '''

class Person :
    def myinfo(self , name ,  age):
        self.name = name  #by defalut its a public 
        self.age = age
    def greet (self):
        print ("my self ", self.name)
    
obj = Person()
obj.myinfo("Pratham", 25)
obj.greet()

# Private 
'''
=> Syntax: __ underscore (double undersocroe is menedetory )
Accessible: not for Everyone (inside the class) '''

class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    def findAge(self):
        return self.age

    def getSalary(self):
        print(self.__salary)
        self.__calculateTax()

    def __calculateTax(self):
        print("calculating tax")


per = Person("Pratham", 99, 5000)

print(per.name)

per.getSalary()

# per.__calculateSalary()  # This will raise an AttributeError because it's private

    
  
     