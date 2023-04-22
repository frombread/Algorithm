import sys
sys.setrecursionlimit(1000000)

def DFS(idx):
    visited[idx]=True
    for i in range(n+1):
        if visited[i]==False and graph[idx][i]==1:
            DFS(i)

    return

## 입력
if __name__ =="__main__":
    n,m = map(int,sys.stdin.readline().split())
    graph = [[0]*(n+1) for _ in range(n+1)]

    ans=0
    for _ in range(m):
        a, b = map(int,sys.stdin.readline().split())
        graph[a][b]=1
        graph[b][a]=1

    visited =[True]+[False]*n
    count=0
    for i in range(n+1):
        if visited[i]==False:
            count+=1
            DFS(i)

    print(count)