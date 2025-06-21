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

#how to the renove the element into the list ?
#there are a some method for remove the lsit of the eleemnt 
#1> remove() method --> it remove the the 1st occurence of the eleemnt not all others 

arr = [1,2,3,4,5,6,7,9,8]
arr.remove(9)
print(arr)

arr2 = [22,33,44,55,66,22,77,88,99]  
arr2.remove(22) #Removing the 1st occuence of the element not all others
print(arr2)

#2> pop() or pop([i]) --> # pop() method which is used to remove at last element of the list or array.
#pop([i]) method which is used to remove the specefic elemet accoding to the index of the list

Fruites = ["Apple", "Banana", "Orange" ,"Pinapple"]
#Fruites.pop()
Fruites.pop(2)
print(Fruites)


# how to replece the elemet in the list ?
Alphabtes = ["A", "B" ,"C" , "D" ,"F" , "G"]
Alphabtes [1:5] = 'm' , 'n' ,'o' ,'p'
print(Alphabtes)

#how to reverse the element on the list?
Numbers = [1,2,3,4,5,6,7,8]
Numbers.reverse()
print(Numbers)

#how the copy of the element of the list ?
Numbers_copy = Numbers.copy()
print(Numbers_copy)
print(id(Numbers_copy) , id(Numbers)) # creating a new list with the help of existing list
#both are differnt bacuse both are adress values is differnt
Numbers.sort() # sorting a elelmet (in Ascending order) on the list.
print(Numbers)


