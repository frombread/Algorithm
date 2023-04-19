import sys

n=int(sys.stdin.readline())
stk_list=[]
answer_list =[]
now =1
find = True
for _ in range(n):
    num = int(sys.stdin.readline())


    while now <= num:
        stk_list.append(now)
        answer_list.append("+")
        now+=1
    if stk_list[-1] == num:
        stk_list.pop()
        answer_list.append('-')
    else:
        find=False
        
if find ==False:
    print("NO")
else:
    for i in answer_list:
        print(i)
