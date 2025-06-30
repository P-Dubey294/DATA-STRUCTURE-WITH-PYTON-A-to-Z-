'''what is method --> 
method is an function which is belogns to an object especially when the object is created '''

class Car:
    def start_engine(self):
        print("Engine started")

my_car = Car()
my_car.start_engine()  # Calling the method on the object

'''Types of Methods 
1> Instance Method
2> Class  Method 
3> Static Method '''

# Instance Method 
class Person :
   def __init__(self, name , age ):
       self.name = name
       self.age = age

   def findAge(self):
       return self.age # onject instance self is mendetory to write 

per = Person("Prathamkumar dubey" , 23)
print(per.findAge())

'''2 > Class Method
-> class / object both 
-> it has no acess to the object properties 
-> it has acess to the class properties 
 '''

class Person : 
   country  = "India"

   @classmethod    #decortor 
   def greet(cls):
        print(" i am from" , cls.country)

   def __init__(self , name , age):
        self.name = name
        self.age = age

   def findAge(self):
        return self.age # object instance self is mandatory to write 
        
per  = Person("Prathamkumar dubey" , 23)
print(per.findAge())
Person.greet()
per.greet()

'''3> Static Methods -> its is independet means 
there is no acess for both class and object peroperties 
example ->'''

class Person : 
   country  = "India"

   @classmethod    #decortor 
   def greet(cls):
        print(" i am from" , cls.country)  #class method

   @staticmethod
   def hello():
        print("hello Pratham")   #static method

   def __init__(self , name , age):
        self.name = name
        self.age = age

   def findAge(self):
        return self.age # object instance self is mandatory to write 
        
per  = Person("Prathamkumar dubey" , 23)
print(per.findAge())
Person.greet()
per.greet()

Person.hello()
        
''' SUMMARY TABLES '''
'''
| Method Type     | First Arg | Access Instance Data | Access Class Data |    Decorator       |
| --------------- | --------- | -------------------- | ----------------- |   ---------------  |
| Instance Method | `self`    | ✅ Yes                | ❌ No           |    None            |
| Class Method    | `cls`     | ❌ No                 | ✅ Yes          |    `@classmethod`  |
| Static Method   | None      | ❌ No                 | ❌ No           |    `@staticmethod` |

'''