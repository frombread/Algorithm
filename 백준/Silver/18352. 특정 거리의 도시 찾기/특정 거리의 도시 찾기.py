from collections import deque
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().split())

city_list = [[] for _ in range(n+1)]
result =[0]*(n+1) 
for _ in range(m):
    a, b = map(int, input().split())
    city_list[a].append(b)

visited = [True]+[False]*n
value = 0

q = deque([x])
ans =[]
def bfs(start):
    q.append(start)
    visited[start] =True
    result[start] =0
    while q:
        value = q.popleft()
        for i in city_list[value]:
            if visited[i]==False:
                q.append(i)
                visited[i]=True
                result[i]=result[value]+1
                if result[i] == k:
                    ans.append(i)
    if len(ans) ==0:
        print(-1)
    else: 
        ans.sort()
        for i in ans:
            print(i,end='\n')

bfs(x)