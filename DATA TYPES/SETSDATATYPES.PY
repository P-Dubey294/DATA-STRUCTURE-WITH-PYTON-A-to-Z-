#what is sets --> Sets is a collection of hetrogeneouus of data .

# Feture Of Sets 
#1 Sets is mutable 
#2 Duplicacy is not allowed 
#2  its a unorder way 
#3 Hetrogeneous Datatype

# Example of Sets 

s1 = { 1,2,3,4,5,6,7,8,9}
print(s1)
print(type(s1))

#2 Duplicacy is not allowed 
group = {444,555,666,777,888,111,333,555,777,888,999}
print(group)

# how do we add the element into the sets

s3 = {11,22,33,44,66,77,88}  # output will be unorder way 
s3.add(99)
print(s3)

# how do we delete the element into the set 

collection = {'AAA' , 'BBB' 'CCC' ,  1, 2, 3, 4, 5, }
collection.remove('AAA')
print(collection)

# what is forzen sets 
# -> its a type of sets but Forzensets are immmutable datatypes 
# Example 

fz = frozenset({11, 22, 33, 44, 55, 66, 77, 88, 99, 0}) 
print(fz)
print(type(fz))

dict1 = { fz : "Pratham"}
print(dict1)