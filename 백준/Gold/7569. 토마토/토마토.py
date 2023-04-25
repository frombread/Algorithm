from collections import deque

def bfs():
    dx = [1,0,-1,0,0,0]
    dy = [0,1,0,-1,0,0]
    dz = [0,0,0,0,1,-1]

    while q:
        z,y,x = q.popleft()
        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]

            if 0<=next_z< h and 0<=next_y<n and 0<=next_x< m and graph[next_z][next_y][next_x] == 0:
                graph[next_z][next_y][next_x] = graph[z][y][x]+1
                q.append([next_z,next_y,next_x])




if __name__  =="__main__":
    m,n,h = map(int,input().split())
    graph =[]
    # 1은 익토 0은 안익토 -1없음
    q= deque([])
    for i in range(h):
        a = []  # 빈 그래프 생성
        for j in range(n):
            a.append(list(map(int, input().split())))
            for k in range(m):
                if a[j][k] ==1:
                    q.append([i,j,k])
        graph.append(a)
    
    bfs()
    day =0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==0:
                    print(-1)
                    exit(0)
                else:
                    day=max(day,graph[i][j][k])
print(day-1)