'''What is file handling 
file handling is a machanishms to create , open , delete , append
reading , writing the files .'''

'''In python open is a function which is used to openinig the files'''

'''There tow mode for oepening the file 
1> Noraml Mode 
2> Binary mode 
'''

#example for Opening and Reading the File 
file = open("FileHandling/file.txt" , "r")
for line in file:
    print(line) 
    print(file.read()) #another file method for opening and reading the files
#using with satement for file openinig and reading 

with open("FileHandling/demo.txt" , "r") as file:
    data = file.read()
    print(data)

#Read only the first x number of character into the file 
with open("FileHandling/demo.txt", "r") as file:
    data = file.read(5)
    print(data)

# Creating and writitng the file 
with open ("FileHandling/main.txt" , "w+") as file:
    data = file.write("hello kya bolte coding ki public")
    print(data)

# writitng and Appending the file 
with open ("FileHandling/main.txt" , "a") as file:
    data = file.write("hello kya bolte coding ki public ")
    data = file.write("good mornig for everyone ")
    print(data)

# Dealeting the file 
import os
try:
    os.remove("FileHandling/youth.txt")
    print("file sucessfully Deleted!")
except FileNotFoundError:
    print("file unsuccessfully deleted!")

