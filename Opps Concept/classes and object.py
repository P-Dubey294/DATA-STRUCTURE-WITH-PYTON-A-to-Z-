'''What is an OOPS ...
Opps stand for Onject Oriented Programming languages it also defined as a real world entity .or 
relationship . '''


''' Classes & Object '''
'''🔹 What is a Class?
A class is a blueprint or template for creating objects. It defines
a set of attributes (variables) and methods (functions) that its objects will have.'''
# examples 
class Person :
    pass 
# or 

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving.")


''' 
🔹 What is an Object?
An object is an instance of a class.
 Once a class is defined, you can create multiple objects from it, each with its own data.'''

#Example 

class person :
    name = "PrathamkumarDubey"
    age = "23"
    city = "GONDIA";

per = person()
print(per.name)
print(per.age)
print(per.city)

per.hobby = "Cricket"
per.nickName = "ItsFirst"

print(per.hobby)
print(per.nickName)

per1 = person()
per2 = person()
per3 = person()

print (per1.name)
print (per2.name)
print (per3.name)

