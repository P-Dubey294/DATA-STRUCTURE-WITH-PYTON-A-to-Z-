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
print(student_details.values())
print(student_details.items()) #Combination both key and values

# How do we add Element into the dictonary ...
student_details ['country'] = "INDIA"
print(student_details)

# how do we updated the element into the dictonory 
marks_details = {'Science' : 40 , 'Math' : 52  , 'English' :45 }
student_details.update(marks_details)
print(student_details)

# HOw do we renove the element into the dictonory 
student_details.pop("country")
student_details.popitem()#removing the last eelemt into the dictonory 
print(student_details)