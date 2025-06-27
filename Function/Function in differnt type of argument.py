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