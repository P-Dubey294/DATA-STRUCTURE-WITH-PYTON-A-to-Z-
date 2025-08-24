def removingConsactive(input_str):
    stack = []
    input_string = input_str
    input_set = set()

    for char in input_string:
        if char not in input_set:
            stack.append(char)
            input_set.add(char)
    return"".join(stack)
input_str = "aaaabbddrrggtthhf"
print(removingConsactive(input_str))