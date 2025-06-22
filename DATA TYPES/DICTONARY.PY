#Dictonaroy --> which used to store the hetrogeneous data in the form of (key & value) pair
#Example

person_details =  {"name" : "Pratham" , "age " : 23 , "City" : "Gondia" }
print(person_details)
print(type(person_details)) 


Human =  {"name" : "Pratham" , "age " : 23 , True : "Gondia" }
print(Human) # beacuse In Python True are represnt in 1 so this is print the out

#2nd Way you have to dictnory for creating a Dictonory constructor 

dict1 = dict (name ="pratham" , age =23 , City = "Gondia")
print (dict)

# Access the element of the dictonary 
student_details = {"name" : "Pratham" , "age" : 23 , "City" : "Gondia"}

print(student_details["name"])
print(student_details["City"])

print(student_details.keys())
 