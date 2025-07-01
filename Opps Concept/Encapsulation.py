'''What is Encapsulation 
=> Encapsulation is binding or hidding the state of an object with 
the method 
  
  or 
  
Encapsulation in Python is one of the fundamental concepts of 
Object-Oriented Programming (OOP). It refers to the bundling 
of data (attributes) and methods (functions) that operate on
that data within a single unit — typically a class — and 
restricting direct access to some of the object's components. 

There are tow method for acessing the private method in Ecapsulation 

1> Getter And Setter Method 
Getter -> to get the method 
Setter -> to set the method 
both are controll the intraction . 

Example -> '''

class person :
    def __init__ (self , name , car ):
        self.__name = name # private fields 
        self.__car = car 
    def getName (self):  # public fileds with the help of getter and setter method you have to be acesss.
        return self.__name 
    def setName (self, name):
        self.__name = name
    def getCar (self):
        return self.__car
    def setCar (self, car):
        self.__car = car
    
per = person("pratham","BMW")
print(per.getName())
per.setName ("prathamkumar Dubey")
print(per.getName())
print(per.getCar())

'''Example '''

class Student :
    def __init__(self,name,age):
        self.__name = name 
        self.__age = age
    def get_Name(self):
        return self.__name
    def set_Name(self,name):
        self.__name = name 

Stu = Student("Pratham" , 23)
print(Stu.get_Name())  #pratham
print(Stu.set_Name("Prathamkumar Praveenkumar Dubey")) # None
print(Stu.get_Name()) # Prathamkumar Praveenkumar Dubey


'''Bank Account Encapsulation '''

class BankAccount :
    def __init__(self , balance):
        self.__balance = balance 
    def deposit ( self , ammount):
        if ammount > 0 :
            self.__balance += ammount
    def withdraw ( self , ammount):
        if 0 < ammount <= self.__balance :
            self.__balance -= ammount 
        else :
            print ("insufficent balance ")
    def get_balance (self):
        return self.__balance 

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance()) 

''' '''

''' salary Employee '''

class Employee :
    def __init__(self , name , salary):
        self.__name = name 
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary (self , new_salary):
        if new_salary  > 0 :
            self.__salary = new_salary
        else :
            print (" invalid salary ")

Emp = Employee("Shruti shrama" , 55000)
print("Salary is :" , Emp.get_salary()) 
Emp.set_salary(75000)
print("New salary will be",Emp.get_salary())
Emp.set_salary(-1000) 

