import sys

stick_list=list(sys.stdin.readline().strip())

stk_list =[]
result =0

for i in range(len(stick_list)):
    if stick_list[i]=="(":
        stk_list.append("(")
    else:
        if stick_list[i-1] =="(":
            stk_list.pop()
            result += len(stk_list)

        else:
            stk_list.pop()
            result += 1

print(result)