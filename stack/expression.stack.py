def top(stack):
    return stack[-1] if stack else None

def isBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if not stack:
                return False
            if char == ")" and top(stack) != "(":
                return False
            if char == "}" and top(stack) != "{":
                return False
            if char == "]" and top(stack) != "[":
                return False
            stack.pop()
    return len(stack) == 0

expr = "{()}]"

if isBalanced(expr):
    print("BALANCED")
else:
    print("NOT BALANCED")
        


            
  
