import sys

input = sys.stdin.readline


n=list(input().rstrip())
f=int(input())
n[-1]="0"
n[-2]="0"
num_list = "".join(n)
n = int(num_list)

while n%f !=0:
    n+=1
n=str(n)
print(n[-2:])