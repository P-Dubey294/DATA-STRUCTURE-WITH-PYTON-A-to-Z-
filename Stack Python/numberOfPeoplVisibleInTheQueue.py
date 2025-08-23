def visible_people(heights):
    n = len(heights)
    result = [0] * n
    stack = []  # will store indices of people in queue

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        count = 0
        # Pop shorter people (they are visible)
        while stack and heights[i] > heights[stack[-1]]:
            stack.pop()
            count += 1
        # If someone taller/equal is still in stack, that person is also visible
        if stack:
            count += 1
        result[i] = count
        stack.append(i)
    
    return result


# Example 1
heights1 = [10, 6, 8, 5, 11, 9]
print(visible_people(heights1))  # [3, 2, 1, 1, 1, 0]

# Example 2
heights2 = [5, 1, 2, 3, 10]
print(visible_people(heights2))  # [4, 3, 2, 1, 0]





