''' Function in Differnt type of argument '''

#1> Defualt aargument 

def My_Student(name, message ="Good morning"):
    print(name, message)
My_Student("Pratham")

#2>keywords Argument 
def keyWordsArgs(name,age,message):
    print(message, name, "your age is", age)
keyWordsArgs(message="hello", name="pratham", age=23)

#3)positional Argument 
def positionalArgs(x, y):
    print("x", x)
    print("y", y)
    print(x + y)
positionalArgs(5, 6)

''' Note agar koi function me n number of argument incude hain tho uss time me hume (*args)argument
pass krna hota hain'''

def nNumberargs(*args):
    print(type(args))
    print(args)
    sum = 0
    for num in args:
        sum += num
    return sum
print(nNumberargs(1,2,3,4,5))

''' if i have to passed number of argument with defult argument '''
''' There are tow rules 
1> *args shuld bhi last parameter
2> keyword = argumnets '''

def funct23(*args, a, b):
    print(a)
    print(b)
    print(args)
    print(*args)
funct23(3, 4, 5, 6, 7, a=1, b=2)

'''what is kwargs ?
=> its stand for keywords argument 
=> it is used in a defination for passing the varible number of keywords argument .
=> its a standrd convention 
=> It collects all extra keyword arguments into a dictionary. '''

def my_display(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print({key.capitalize()}, '->', value)

my_display(name = "Pratham", city = "Gondia", age = 23, message = "Sucessfull!")


#example kwargs :->
def my_info(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(kwargs)
    print(type(kwargs))
    print(args)
    for key , value in kwargs.items():
        print(key.capitalize(),'->', value)

my_info(5,6,7,8,9,0 , name = "pratham" , sername = "dubey" , age = 23 , city = "gondia")

'''NOTE ->  kwargs it should be the last parameter '''