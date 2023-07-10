a_,b_ = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

res =[]
for i in B:
    A.append(i)
A.sort()
for i in A:
    print(i,end=' ')