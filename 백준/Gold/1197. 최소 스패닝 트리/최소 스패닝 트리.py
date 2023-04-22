import heapq

V, E =map(int,input().split())
graph=[[] for _ in range(V+1)]

for _ in range(E):
    idx,idx2,cost =map(int,input().split())
    graph[idx].append((cost,idx2))
    graph[idx2].append((cost,idx))

visited = [False]*(V+1)
heap = graph[1]
visited[1]=True
heapq.heapify(heap)

ans = 0
while heap:
    cost, d = heapq.heappop(heap)
    if visited[d]==False:
        visited[d]=True
        ans+=cost
        for i in graph[d]:
            if visited[i[1]] ==False:
                heapq.heappush(heap,i)

print(ans)