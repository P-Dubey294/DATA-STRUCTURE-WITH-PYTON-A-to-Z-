'''Q) 1 -10th no print } ->
as soon as get the number which is divisible by 4 and stop'''

for num in range (1 , 13):
    if(num%4 == 0):
        break
    print (num)

'''continue'''
for i in range (11):
    if(i%2 !=0):
        continue
    print(i)