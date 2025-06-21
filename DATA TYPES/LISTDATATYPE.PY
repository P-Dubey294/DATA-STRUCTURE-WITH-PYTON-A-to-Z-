# WHAT IS liST 
'''
--> LIST IN PYTHON ITS A IN-BUILT DATATYPE USED TO STORE 
THE OR COLLECTION THE DIFFERNT DATATYPE OF ELEMENT

--> LIST ARE ORDERLY ARRANGEMENT OF ELEMENT

...> LIST ARE MUTABLE IT CAN BE CHANGEABLE

''' 

#EXAMPLE

student = ["pratham" , "shruti", "vishwas" , "raj"]
print(student)
print(type(student))

list2 = list(student)
print(list2)

list3 = list("Pratham") #with the help of constructor (list)--> we can suffle the latter or saprated
print(list3)

#list are store or collection the differnt datatypes of elelment 
#Example 

Employee = [1,23456,"Prathamkumar Dubey", "Gondia"]
print(Employee)
print(type(Employee))


# HOW TO ACCESSS THE ELELMENT OF THE LIST 

# THERE ARE THREE CONDITION FOR ACCESSING AND MODIYING THE LIST 

#1>append() method 
'''this method is used to adding or inserting the element at the last of the list or aaray'''
worker = ["Raj" , "niklesh" 'rohit' ,"nohit"]
worker.append("adip")
print(worker)

#2>insert() method 
'''this method is used to adding or inserting the element at specefic possition'''
listABC = [22,33,44,55,66,77,99]
listABC.insert(6 , 88)
print(listABC)

#3>extend() metohd
'''this method is used to exchange the existing of the lsit'''
listA = ["pratham", "shruti" , 1]
listB = [2,3,4,5,6,7]
listA.extend(listB)
print(listA)

