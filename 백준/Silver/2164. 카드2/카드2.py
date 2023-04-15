import sys
from collections import deque
a= int(sys.stdin.readline())
q =deque([])

for i in range(1,a+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    result = q.popleft()
    q.append(result)

print(q[0])