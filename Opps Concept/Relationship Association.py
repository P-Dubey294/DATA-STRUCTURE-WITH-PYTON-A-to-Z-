'''What is Association Realtioship 

Aggregation is a "has-a" relationship where one class contains a reference to another class.
However, the contained object can exist independently of the container object..
Example => 
Person has car '''

''' Aggregation is a "has-a" relationship between
two classes where one class contains a reference to another class, 
but both can exist independently. '''

class Car :
    def __init__(self, brand , color):
        self.brand = brand 
        self.color = color 
    
class Person :
    def __init__(self , name , car):
        self.name = name
        self.car = car 
    
car = Car("BMW", "Black")
per = Person("Pratham Dubey" , car)

print(per.name)
print(car.brand)
print(car.color)

#Compositions

'''Definition:
Composition is also a "has-a" relationship,
but with a stronger bond. The contained object
cannot exist independently of the container object.

Key Point:
The lifetime of the contained object depends on the
container. When the container is destroyed, the
contained object is also destroyed.'''

class  Engine :
    def enginedetails(self):
        print(" Car Engine Model is E126F3")

class Tyers :
    def tyersdetails(self):
        print(" The car of typer is apollo")

class Doors :
    def doordetails(self):
        print(" Door of the car is automatic ")

class Car :
    def __init__(self):
        self.engine = Engine()   # object should be created and car is a exisiting class 
        self.tyers =  Tyers()
        self.door = Doors()

    def printDetails(self):
        self.engine.enginedetails()
        self.tyers.tyersdetails()
        self.door.doordetails()

c = Car()
c.printDetails()



        
