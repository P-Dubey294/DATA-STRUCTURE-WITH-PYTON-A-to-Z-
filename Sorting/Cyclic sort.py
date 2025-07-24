#Cyclic Sort is a very useful algorithm, especially for problems involving numbers
# in a known range like 1 to n or 0 to n-1. It runs in O(n) time and O(1) space.

#🔹 When to Use Cyclic Sort:
'''' When array elements are in the range 1 to n or 0 to n-1
Perfect for sorting such arrays or detecting duplicates/missing numbers in that range.'''

# Time complexity is 0{n^2}
# its a unstable sorting algorithams 
# in- place (menas auxilary space)

def Cyclic_sort(array):
    n = len(array)
    for cycleStart in range(0, n - 1):
        item = array[cycleStart]
        pos = cycleStart

        # Find the correct position for the item
        for i in range(cycleStart + 1, n):
            if array[i] < item:
                pos += 1

        # If the item is already in correct position
        if pos == cycleStart:
            continue

        # Skip duplicates
        while item == array[pos]:
            pos += 1

        # Swap
        array[pos], item = item, array[pos]

        # Rotate rest of the cycle
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]

    return array

arr = [4, 3, 6, 3, 3, 3, 3, 6, 1]
print(Cyclic_sort(arr))



