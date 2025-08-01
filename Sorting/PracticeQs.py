#Q1> How much max swaps are needed for short of array 6 
#solve=>

def max_Swap(arr):
    n = len(arr)
    count = 0
    for i in range(n - 1):
        is_sorted = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                is_sorted = False
                count += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if is_sorted :
                    break
    return count

print(max_Swap([5, 4, 3, 2, 1]))


'''Q2> sort a string in descending order of value asociate 
after remival the value smaller of x .?'''

''' str = Akshay 45 pratham 79 mohan89 vishwa 45 nikilesh 79
output  x = 50 
removal str is => Akshya 45 < 50  vishwa 45 <  50  
 & the remaining str and vlaue are arrange (sort) in descending order 
ie output = > mohan 89  niklesh 79 pratham 79  '''

def sortTheString(str, x):
    
  #Create the list
  my_list  = str.split()

  n = len(my_list)
 
  #Remove the pair whose value is less than given number
  for i in range(n-1,0,-2):
    if int(my_list[i])<x:
      del(my_list[i-1:i+1])

  n = len(my_list)

  #Sort the given list of elements

  for i in range(1,n, 2):
    for j in range(1,n-i,2):
      if my_list[j] <my_list[j+2] or (my_list[j-1] < my_list[j+1] and my_list[j] == my_list[j+2] ) :
        my_list[j], my_list[j+2] = my_list[j+2] , my_list[j]
        my_list[j-1], my_list[j+1] = my_list[j+1], my_list[j-1]

  return " ".join(my_list)

str = "Akshay 43 Vishwa 79 Mohan 83 Nikhil 79 Shivani 43"   

print(sortTheString(str, 50))

# push zeros to end while maintaning the realtive order of the elements .

''' lets understand the question 

supoose we have a list or array like [ 1, 2, 0 , 4 ,3, 0, 5 ,0] so 
all the zero are push tho the end of the non zero elelment and the non zero element 
are as it same oderder like [ 1, 2 ,4, 3, 5, 0, 0, 0,]'''

def PushTheZeroElemnt(arr):
    count = 0  # count non zero elemment 
    n = len(arr) # n = 8
    temp = [0]*n  #temproroy list or array [0,0,0,0,0,0,0,0]

    for i in range(n): # 0 to 8
        if (arr[i] != 0): 
            temp[count] = arr[i] # arr[i] ki value temp[count] me swap ho jayegi
            count += 1   # count ek increased honga eg 1 then next me 2 then next 3 

    # Fill remaining positions with 0 (already done by temp initialization)
    for i in range(n):
        arr[i] = temp[i]

arr = [1,2,0,3,4,0,5,0]
PushTheZeroElemnt(arr)
print(arr)
              
        
        
