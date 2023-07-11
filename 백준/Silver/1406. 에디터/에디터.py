m = input()
n = int(input())
commands = [input().split() for _ in range(n)]

left_stack = list(m)
right_stack = []

for command in commands:
    if command[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == "B":
        if left_stack:
            left_stack.pop()
    elif command[0] == "P":
        left_stack.append(command[1])

right_stack.reverse()
result = left_stack + right_stack
print("".join(result))