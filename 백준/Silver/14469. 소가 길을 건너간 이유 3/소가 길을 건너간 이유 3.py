import sys

input =sys.stdin.readline

N = int(input())
cow_wait_list = []
for i in range(N):
    a,b = map(int,input().split())
    cow_wait_list.append([a,b])

cow_wait_list.sort()
result = cow_wait_list[0][0]+cow_wait_list[0][1]

for i in range(1,len(cow_wait_list)):
    if result < cow_wait_list[i][0]:
        result=cow_wait_list[i][0]+cow_wait_list[i][1]
    else:
        result+=cow_wait_list[i][1]

print(result)