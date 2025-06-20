def PrintNum1toN(n):
    if n == 0:
        return 
    PrintNum1toN(n-1)
    print(n)