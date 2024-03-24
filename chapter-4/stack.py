list_formula = input().split()

stack = []

for val in list_formula:
    if val in ['+', '-', '*']:
        right = stack.pop()
        left = stack.pop()
        if val == '+':
            result = left + right
        elif val == '-':
            result = left - right
        else:
            result = left * right
        stack.append(result)
    else:
        stack.append(int(val))

print(stack[0])
