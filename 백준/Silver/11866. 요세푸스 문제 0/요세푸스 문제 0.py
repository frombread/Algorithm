import sys
from collections import deque
a,rotate= map(int,sys.stdin.readline().split())

q =deque([])

answer =[]
for i in range(1,a+1):
    q.append(i)

print("<",end="")
for i in range(a):
    q.rotate(-rotate)    
    result = q.pop()
    if i != a-1:
        print(result, end=", ")
    else:
        print(result,end="")
print(">",end="")