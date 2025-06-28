'''that when you passed the varibles to a function 
copy of the value is send notthe orignal value '''

'''pass by refernce active when datatype are immutable -->  string , tupples , numbers '''

num = 4
def modify_num(num):
    num+= 1
    print("Modified num", num)
print(num)
modify_num(num)
print("Orignal num" , num)

'''passed by refernce 
-> you are passing the memeory adresss into the orignal object 
-> if your are chnges the inside the function it will be effected to the orignal value '''
'''-> arguemnt -> mutables -> dict , list '''

my_list = [1,2,3,4,5,6,7]
def modify_list(li):
    li.append(8)
    print(li)

print("before calling function ", my_list)
modify_list(my_list)
print("before calling the function ", my_list)





