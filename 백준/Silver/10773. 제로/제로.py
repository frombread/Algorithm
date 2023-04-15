import sys
n = int(sys.stdin.readline())

stk_list =[]

for i in range(n):
    num_list = int(sys.stdin.readline())
    
    if num_list == 0:
        pop_num = stk_list.pop()
    else:
        stk_list.append(num_list)
    
print(sum(stk_list))
