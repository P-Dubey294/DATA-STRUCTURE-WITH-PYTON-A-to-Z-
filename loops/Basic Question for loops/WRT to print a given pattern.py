'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''


for row in range (5):#outer loop
    for j in range (row+1): #inner loop
        print("*", end="")
    print() #new line


'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

