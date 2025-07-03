'''What is an Abstraction 
=> Abstraction is hidding the unnecessary information  /  
providing only important impoeratant details .

adantages --.
1> Eassy for the coustomer 
2> protect / avoide the important information leaked 

in pyhton world  we have  to provide a abstract class 

what is abstract class ? 
=> abstract class is a class which do not create a object 

=> it shuld be involved  atleast 1 abstract method 

=> child classs should be implemented  '''

class Animmal:            # there is no anywere used 
    def Eat(self):  
        pass

animal = Animmal()
animal.Eat()

''' jb bhi hum existing module ko use krete hain so ie syntax is --->
from abc import ABC '''

from abc import ABC, abstractmethod 

class Animal(ABC):  # Parent class
    @abstractmethod
    def Eat(self): # method overriding ( same method are used in parents and child class)
        pass

# Do not instantiate Animal or call Eat() directly, as it's abstract

'''class Dog(Animal):   # child class 
    def sleep(self):  
        print("dog is sleeping")
    def Eat(self):  # method overriding  its shuld be compusory initalized in abastract method
        print("Dog is eating") 

d = Dog()
d.Eat()
    '''

'''Another example '''

from abc import ABC , abstractmethod

class Person(ABC):
    @abstractmethod
    def Eat(self):
        print("parents is eating")

    def display(self):
        print("Display method in Person")

class child(Animal):
    def running(self):
        print("child is running")
    def Eat(self):
        print("child is eating")

ch = child()
ch.Eat()
ch.running()
        