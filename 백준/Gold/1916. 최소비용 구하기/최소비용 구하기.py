import sys
from sys import maxsize
import heapq
input = sys.stdin.readline
n=int(input())
m=int(input())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    idx,idx2,cost =map(int,input().split())
    graph[idx].append((cost,idx2))

start, end =map(int,input().split())


def dijstra(start):
    visited = [maxsize]*(n+1)
    visited[start]=0
    bus =[]
    heapq.heappush(bus,[0,start])
    while bus:
        dist,node = heapq.heappop(bus)

        if visited[node]<dist: # 기존 최단 거리보다 멀다면 무시
            continue

        for next_dist,next_node in graph[node]:
            distance = dist + next_dist # 인접노드까지의 거리
            if visited[next_node] > distance:
                visited[next_node] = distance
                heapq.heappush(bus,[distance,next_node])

    return visited
               


# def bfs(station):
#     global cost
#     ans =0
#     cost.append(graph[station])
#     visited[station]=True
#     while cost:
#         cost, next_station =cost.popleft()
#         if visited[next_station] ==False:
#             visited[next_station] =True
#             ans= ans+cost

#         for i in cost[station]:
#             if visited[i]==False:
#                 cost.append(graph[i])
#                 visited[i]=True
#         result3.append(ans)

dist_start = dijstra(start)

print(dist_start[end])