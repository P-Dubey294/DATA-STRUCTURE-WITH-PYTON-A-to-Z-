num = int(input("please enter the value"))
if (num <= 0):
    print("number entered is not correct. It should be > 0. Entered num", num)
elif num == 1:
    print(1)
elif num == 2:
    print(1, 1, sep=",") 
else:
    print(1, 1, end=",")
    prev = 1
    prev_prev = 1
    for i in range(3, num + 1):
        curr = prev + prev_prev
        print(curr, end="," if i < num else "")
        prev, prev_prev = curr, prev
    print()
        

