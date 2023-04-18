import sys


n, k = map(int,sys.stdin.readline().split())
cnt = k
num_list=list(sys.stdin.readline())

stk_list=[]


for i in range(n):

    while stk_list and stk_list[-1]< num_list[i] and cnt>0:
        stk_list.pop()
        cnt-=1

    stk_list.append(num_list[i])


print((''.join(stk_list[:n-k])))

