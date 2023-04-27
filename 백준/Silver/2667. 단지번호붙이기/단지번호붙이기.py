n =int(input())
graph =[]
flag = [[False] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(input()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global house_count
    flag[x][y]=True
    house_count+=1
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0<=next_x<n and 0<=next_y<n:
            if flag[next_x][next_y]==False and graph[next_x][next_y]=="1":
                DFS(next_x,next_y)
count=0
house_count_list=[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and flag[i][j]==False:
            house_count=0
            DFS(i,j)
            house_count_list.append(house_count)
            count+=1
print(count)
house_count_list.sort()
for i in house_count_list:
    print(i)