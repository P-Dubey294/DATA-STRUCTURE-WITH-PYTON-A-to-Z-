stack = []
operator = set([ "+", "-", "*", "/", "^"])
expression = "*+abc"

for char in reversed(expression):
    if char not in operator:
        stack.append(char)
    else:
        opt1 = stack.pop()
        opt2 = stack.pop()
        stack.append(f"({opt1} {char} {opt2})")
print(stack.pop())