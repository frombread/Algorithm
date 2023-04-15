import sys
from collections import deque
a= int(sys.stdin.readline())
q =deque([])

for i in range(a):
    input = sys.stdin.readline().split()
    word = input[0]

    if word== 'pop':
        if len(q) ==0:
            print(-1)
        else:
            result = q.popleft()
            print(result)
    
    elif word == 'push':
        value = input[1]
        q.append(value)
    
    elif word == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif word == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    
    elif word == 'size':
        print(len(q))

    elif word =="empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)