def dfs(idx,flag,text):
    flag[idx]=True
    result.append(idx)
    
    for i in range(vertex+1):
        if flag[i] == False and tree[idx][i]==1:
            dfs(i,flag, text)



def BFS(idx, flag2, text):
    queue.append(idx)
    flag2[idx] = True

    while queue:
        value=queue.popleft()
        result2.append(value)
        for i in range(1,vertex+1):
            if not flag2[i] and tree[value][i] ==1:
                queue.append(i)
                flag2[i]=True




"""입력"""
import sys
from collections import deque
vertex, edge, num = map(int,sys.stdin.readline().split())

tree = [[0]*(vertex+1) for _ in range(vertex + 1)]
for _ in range(edge):
    a, b = map(int,sys.stdin.readline().split())
    tree[a][b]=1
    tree[b][a]=1
result=[]
result2=[]
flag = [False]*(vertex+1)
flag2 = [False]*(vertex+1)
queue = deque()
dfs(num,flag,"")
BFS(num,flag2,"")
for i in result:
    print(i, end=" ")
print()
for i in result2:
    print(i,end=" ")