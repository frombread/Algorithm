import sys
from collections import defaultdict ,deque


N,M = map(int, input().split())
graph =defaultdict(list)
indegree = [0]*(N+1)
for _ in range(M):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] +=1
    

def topology_sort():
    result=[] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 depue 라이브러리 사용

    for i in range(1,N+1):
    	if indegree[i]==0:
            q.append(i)
    while q:
        now =q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i, end=" ")

topology_sort()