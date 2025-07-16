''' find first and last possition of element in sorted array. '''
#using linear Serching 
















#using binary serching


#First Occcurance 
def first(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1  # keep searching on the left side for first occurrence

    return res

#Last Occcurance 
def last(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1  # keep searching on the right side for last occurrence

    return res


def firstandlast(arr ,x):
    fi = first(arr, x)
    li = last(arr, x)

    return[fi , li]

arr = [1, 5 ,5 ,5 , 6, 7,  8, 9]
x = 5
print(firstandlast(arr ,x))


 
