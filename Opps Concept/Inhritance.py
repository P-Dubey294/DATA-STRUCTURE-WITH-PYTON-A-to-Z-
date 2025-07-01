''' What is inheritance 
=> Inheritance is machanishm which represent the parent
child relatioship as wll as inherits the one class from the another 
class (i.e Parent class or supper class ).
'''

class Animal : # Parent
    def __init__(self , name):
        self.name = name 
    def eat(self): # Praent methods
        print (self.name + " animal is easting ")
       
class Dog (Animal):
    def __init__(self, name , type):
        #Call the constructor / initailzer of animal
     Animal.__init__(self, name)
     self.type = type

    def dog_Name(self):
       print(self.name)

dog = Dog("Sheruu" , "BullDog" )
dog.eat()
dog.dog_Name()
            
'''ADAVANTAGES OF INHERITANCE 

1> it help to reuse the code (reuseablity)
2> it help to determined the realtionship i.e Parents to child  '''

'''Super keyword ==> Acess the Parents properties .'''

class Parent :
   property = 90

   def eat(self):                    #same method 
        print("paraent eating")

class Child(Parent) :
   property = 99

   def display(self):
       print("child Properties", self.property)
       print("Parent Property", super().property) # acesss the parent properties with the hel of super keywords .

   def eat(self):                   #same method
        print("child eating")
    
   def callEat(self):
    self.eat() # represent the child
    super().eat() # reprent the parent

obj = Child()
obj.display()
obj.callEat()

'''What is method overide ?
=> whe we called a same method in both parents and cild  with the same properties or behaviour .'''