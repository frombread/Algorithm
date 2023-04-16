def func(A,B):
    if B==1:
        return A%C
    
    num = func(A,B//2)

    if B%2 == 0:
        return num*num%C
    else:
        return num*num*A %C
    

import sys
A,B,C = map(int,sys.stdin.readline().split())

print(func(A,B))