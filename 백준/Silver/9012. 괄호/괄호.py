import sys

a= int(sys.stdin.readline())

for i in range(a):
    stk_list =[]
    PS_list=sys.stdin.readline()
    for j in PS_list:
        if j =="(":
            stk_list.append(j)
        elif j==")":
            if stk_list:
                stk_list.pop()
            else: 
                print("NO")
                break
    else: 
        if not stk_list:
            print("YES")
        else:
            print("NO")