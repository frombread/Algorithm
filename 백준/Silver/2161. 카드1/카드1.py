import sys

from collections import deque

q =deque()

n = int(sys.stdin.readline())



for i in range(1,n+1):
    q.append(i)

while len(q)!=1:
    print_result=q.popleft()
    s = q.popleft()
    q.append(s)

    print(print_result)
    
print(q[-1],end="")
