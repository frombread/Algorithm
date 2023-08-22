from collections import deque
queue =deque()
n ,m =map(int,input().split())
graph =[]
for i in range(m):
    graph.append(list(input()))

q=deque()
dx =[1,-1,0,0]
dy =[0,0,1,-1]

def bfs(x,y,soldier):
    cnt =0
    q.append((x,y))
    graph[x][y]= -1
    while q:
        x,y = q.popleft()
        cnt +=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == soldier:
                    q.append((nx,ny))
                    graph[nx][ny]= -1
    return cnt

w_soldier,b_soldier =0,0

for i in range(m):
    for j in range(n):
        if graph[i][j]=="W":
            w_soldier += bfs(i,j,"W")**2
        elif graph[i][j]=="B":
            b_soldier += bfs(i,j,"B")**2
print(w_soldier,b_soldier)