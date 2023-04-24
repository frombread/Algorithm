import heapq
n =int(input())

graph =[]
visited = [[0]*n for _ in range(n)]## 언제는 쓰고 언제는 안쓰는지 헷갈린다....
for _ in range(n):
    graph.append(list(map(int, input())))


dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dijstra():
    heap= []
    heapq.heappush(heap,[0,0,0])
    visited[0][0]=1
    while heap:
        a,x,y = heapq.heappop(heap)
        if x== n-1 and y == n-1:
            print(a)
            return
        for i in range(4):
            next_x = x +dx[i]
            next_y = y +dy[i]
            if 0<=next_x<n and 0 <= next_y <n and visited[next_x][next_y]==0:
                visited[next_x][next_y]=1
                if graph[next_x][next_y] ==0:
                    heapq.heappush(heap,[a+1,next_x,next_y])
                else:
                    heapq.heappush(heap,[a,next_x,next_y])
dijstra()