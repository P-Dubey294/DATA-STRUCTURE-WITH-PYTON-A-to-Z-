''' what is polymorphism 
=> Poly menas ---> many (multi) 
=> phism means ---> foorm 

defination -> Polymorphism is the ability of different
objects to respond to the same method in different ways.

🔹 Types of Polymorphism in Python
Compile-time Polymorphism (Method Overloading) – Not directly supported in Python.

Run-time Polymorphism (Method Overriding) – Supported using inheritance.

Example :- 

'''   
# important Example for interviwer 
class Birdfly :
    def flybird(self, bird):
        bird.fly()

class parrot :
    def fly(self):
        print("parrot is flying")

class crow :
    def fly(self):
        print("crow is flying")

P = parrot()
C = crow()

bf = Birdfly()


bf.flybird(C)
bf.flybird(P)

''' one  more exampme ''' 

class Animal :
    def speak (self):
     print("animal is speaking")

class cat (Animal):
    def speak (self):
     print ("cat is meawo")

class dog (Animal) :
    def speak (self):
     print ("dog is bark")

c = cat()
d = dog()

animal = Animal()

# Demonstrate polymorphism by calling speak on different objects
c.speak()
d.speak()