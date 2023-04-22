import sys
sys.setrecursionlimit(1000000)
def DFS(idx):
    visited[idx] =True

    for i in range(n+1):
        if visited[i]==False and graph[idx][i]==1:
            DFS(i)




if __name__ =="__main__":
    n= int(sys.stdin.readline())
    m= int(sys.stdin.readline())


    graph = [[0]*(n+1) for _ in range(n+1)]
    visited =[True] +[False] *n
    for _ in range(m):
        a, b = map(int,sys.stdin.readline().split())
        graph[a][b]=1
        graph[b][a]=1
    
    DFS(1)
    count=0
    # for i in visited:
    #     if i ==True:
    #         count+=1

    ans = visited.count(True)
    print(ans-2)
