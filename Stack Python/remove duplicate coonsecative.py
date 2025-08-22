def duplicate(input_str):
    input_set =  set()
    stack = []
    input_string = input_str

    for char in input_string:
        if char not in input_set:
            stack.append(char)
            input_set.add(char)
    return "".join(stack)

input_str = "aaaabcccccd"
result = duplicate(input_str)
print(result)

