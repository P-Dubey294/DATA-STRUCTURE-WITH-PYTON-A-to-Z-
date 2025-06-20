def printNUmm(arr , si):
    #Base condition/Terminations
    if(si >=len(arr)): 
        return
    #Recusively 
    printNUmm(arr, si+1)
    #logic
    print(arr[si])
printNUmm([2,3,5],0)
