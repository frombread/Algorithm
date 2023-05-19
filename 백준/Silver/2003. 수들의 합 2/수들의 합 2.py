import sys

input = sys.stdin.readline

m,n = map(int,input().split())
list_num = list(map(int,input().split()))
count =0
test =0
for i in range(m):
    test = list_num[i]
    if test == n:
        count+=1
    for j in range(i+1,m):
        test += list_num[j]
        if test == n:
            count+=1
        elif test >n:
            break
print(count)