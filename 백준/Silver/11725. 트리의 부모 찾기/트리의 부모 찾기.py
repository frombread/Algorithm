import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
def DFS(idx):
    visited[idx] =True
    for i in graph[idx]:
        if visited[i]==False:
            result.append([i,idx])
            DFS(i)
            



if __name__ == "__main__":
    n=int(sys.stdin.readline())
    visited = [True]+[False]*n
    graph = defaultdict(list)
    result=[]
    for _ in range(n-1):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    DFS(1)
    result.sort()
    for i in range(len(result)):
        print(result[i][1])



    # result=[0]*(n+1)
    # for i in ans:
    #     result[i[1]]=i[0]