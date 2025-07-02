# single inheritance 
''' chaild class inherits fron only one (single) Parent class '''

class Animal :
    def speak(self):
        print("Animal is Speak")
    
class Dog (Animal):
    def bark(self):
        print("Animal is bark")
    
dog = Dog()
dog.speak()
dog.bark()

'''Example'''

class Animal :
    def __init__(self, name ):
        self.name = name
    
    def Eat(self):
        print(self.name, "Animal is Eating")
    
class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

d = Dog("Stonio", "Hybrid")
d.Eat()
print(d.type)

#Multiple Inheritance 
'''A child class inherits fron the multiple parents class '''

class Father :
    def Skills(self):
        print("Gardening")

class Mother :
    def Skills(self):
        print("Hosewife")

class Child (Father,Mother):
    def Ohterskill(self):
        print("Cricket")
    
c = Child()
c.Skills() # Will follow Method Resolution Order (MRO).[Method resolutions Order .]

#Multi-level Inheritance 
'''A child class inherits from the parants class which is itshelf inhertis from the another class.'''

class GrandFather :
    def show(self):
        print("GrandFather")
class Parants(GrandFather):
    def display(self):
        print("Parants")
class Child(Parants):
    def speak(self):
        print("Child")

ch = Child()
ch.show()
ch.display()
ch.speak()

#Hirerchical Inheritance 
'''Multiple child class inherits from the single (one) Parents class '''

class Father :
    def VishwarajSingh(self):
        print("I am the father of all these children")
class son1(Father) :
    def Akash(self):
        print("My name is Akash and my parent is VishwarajSingh")
class son2(Father):
    def Sunil(self):
        print("My name is Sunil and my parent is VishwarajSingh")
class son3(Father):
    def Virat(self):
        print("My name is Virat and my parent is VishwarajSingh")
    
s1 = son1()
s2 = son2()
s3 = son3()

s1.Akash()
s2.Sunil()
s3.Virat()

#Hybrid Inheritance 
'''Combination of tow or more inheritance '''

class A :
    def Method_A(self):
        print("A")

class B(A):
    def Method_B(self):
        print("B")

class C(A):
    def Method_C(self):
        print("C")

class D(B,C):
    def Method_D(self):
        print("D")

ca = A()
cb = B()
cc = C()
cd = D()

cd.Method_D()
cd.Method_A()
cd.Method_B()
cd.Method_C()

    