from collections import deque

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
s,fx,fy = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q= deque()
ans =[]
for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            ans.append((graph[x][y],x,y,0))
count =0
ans.sort()
def bfs():
    global count
    for i in ans:
        q.append(i)
    while q:
        a,x,y,time =q.popleft()
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if 0<=next_x<n and 0 <=next_y<n:
                if graph[next_x][next_y] ==0 and graph[x][y]== a:
                    if time+1 <= s:
                        graph[next_x][next_y] = a
                    q.append((a,next_x,next_y,time+1))
        if time == s:
            return
bfs()
print(graph[fx-1][fy-1])