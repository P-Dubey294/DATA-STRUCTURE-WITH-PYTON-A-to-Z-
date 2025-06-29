'''Lambda function is also called anonymous function or synthetical sugar 
which will takes any no of arguments '''

def my_func():
    #return a new functions 
 return lambda msg : print(msg)
my_func()('Hello pratham good morning!')

addition = lambda a , b : a + b 
print(addition(5,6))

mulyiplication =  lambda a ,b : a * b 
print(mulyiplication(6,3))