def printNUmm(arr , si):
    #Base condition/Terminations
    if(si >=len(arr)):
        return
    #logic
    print(arr[si])
    #Recusively 
    printNUmm(arr, si+1)
printNUmm([2,3,4,5,6,7,8],0)
