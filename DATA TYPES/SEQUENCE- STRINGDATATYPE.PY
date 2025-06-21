#String is group or collection of sequence of charater 
#String is imutable means once be created it cannot be changed.
#String  can access the element via indexing 
#Example 

NAME = 'pratham'
City = "gondia"
Country = '''INDIA'''
print(NAME , City, Country)

#String is imutable means once be created it cannot be changed.
student_Name = "Shruti Dipak Shrama"
#student_Name [0] = 'X'
print(student_Name) #TypeError: 'str' object does not support item assignment


#String can access the element via indexing 

Person_name = "Dr.vivek kapoor"
print(Person_name[3])
print(Person_name[-2])

#1> Concatination operator
first_Name = " Prathamkumar"
last_Name = "Dubey"
full_name = first_Name +" "+last_Name
print(full_name)

# how to find the length of the string ?

person_Name = "Shri Narendra damodardas modi"
print(len(person_Name));

#What is Slicing 
#Slicing is a pice of part (POrtions) 

College_Name = "GH Raisoni College of engeeneering and Management"
print(College_Name[3:10])
print(College_Name[3:]) #it goes to R to end --tk
print(College_Name[:4]) #it goes to G to R 