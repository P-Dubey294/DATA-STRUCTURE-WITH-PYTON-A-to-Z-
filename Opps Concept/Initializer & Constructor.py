'''
what is initalizer consttructor in python 
In Python, the initializer constructor refers to the
 special method __init__() used in Object-Oriented Programming (OOP).
   It is called automatically when you create an object from a class. 
Its main purpose is to initialize the attributes of the object. '''

class person :
    def __init__ (self, name , age):
        self.name = name 
        self.age = age 
  
per1 = person("Prathamkumar Dubey" , 23)
per2 = person("Shruti Shrama" , 22)


print(per1.name)
print(per1.age)
print(per2.name)
print(per2.age)

'''Suppose We Have A multiple Initaializer __int__()
what will be the heppened? looking an example '''

class PERSON :
    def __init__ (self, name, age): # it will be ignored
        self.name = name
        self.age = age

    def __init__ (self, name): #it shuould be initalized at last number of the __init__
        self.name = name
    
per = PERSON ("prathamkumardubey")
print(per.name)

'''Reasons is  Initalizer are support a multiple init but its shuould be accepet only last of the 
init other are ignoreed it'''

        
'''Supooose we have passed number of argument with parameter or possitional argument then 
what will be the happened ? looking of an example '''
class Student :
    def __init__(self , name = "Pratham" , age = 23 , city = "gondia"):
        self.name = name
        self.age = age
        self.city = city
Stu1 = Student("Vikas")
Stu2 = Student("Rohit", 21 , "Nagpure")
Stu3 = Student("Vishwa" , 22, "Banglore")

print (Stu1.name)
print (Stu1.age)
print (Stu1.city)
print (Stu2.name)
print (Stu2.age)
print (Stu3.name)
print (Stu3.age)
print (Stu3.city)


