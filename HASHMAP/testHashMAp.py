input_dict = {}
input_dict ["name"] = "Prathamkumar Dubey"
input_dict ["age"] = [23,24,25,26,27]
input_dict ["conactno"] = [9529754950]
input_dict ["adress"] = ["CIVIL LINE GONDIA"]
print(input_dict)


#deleting a perticular key 

input_dict.pop("name")   #1st way 
print(input_dict)

del input_dict['age']   #2nd way
print(input_dict)

input_dict.popitem()   #3rd way
print(input_dict)

# updating he dictnory 
input_dict.update({"name" : "Rohit Kaikade"})
print(input_dict)

# clear all the data
input_dict.clear()
print(input_dict)