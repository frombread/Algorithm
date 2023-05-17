import sys

input =sys.stdin.readline
cow_list=[-1] *11
count=0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if cow_list[a] ==-1:
        cow_list[a] =b
    elif cow_list[a] !=b:
        cow_list[a] =b
        count+=1

print(count)
