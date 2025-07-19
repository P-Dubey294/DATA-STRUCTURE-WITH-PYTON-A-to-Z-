'''📚 What is Merge Sort in Python (DSA Topic)?
Merge Sort is a popular Divide and Conquer algorithm 
used for sorting. It divides the input array into two halves, 
recursively sorts them, and then merges the sorted halves. 

Time Complexity:
Best: O(n log n)
Average: O(n log n)
Worst: O(n log n)

Space Complexity:
Space Complexity: O(n) using extra space 
''' 
def merge_sort(arr):
    if len(arr) > 1:
        # Step 1: Divide
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Step 2: Sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Step 3: Merge sorted halves
        i = j = k = 0

        # Merge both halves into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage 
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)

    
            
            
           

        



