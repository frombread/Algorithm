import sys
sys.setrecursionlimit(1000000) ## 재귀 깊이 설정


def dfs(x,y, flag, depth): ### DFS
    global n
    global area_list
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    if depth >= n*n:
        return
    
    flag[x][y] =True
    
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if next_x < 0 or next_x > n-1 or next_y < 0 or next_y > n-1:
            continue
        if area_list[next_x][next_y] != 0 and flag[next_x][next_y]==False:
            dfs(next_x,next_y,flag,depth+1)


def water_height(height): ### 물높이
    global n
    global area_list
    for i in range(n):
        for j in range(n):
            if area_list[i][j] < height:
                area_list[i][j] =0



def water_full(): ### 물 가득
    for i in range(n):
        for j in range(n):
            if area_list[i][j] !=0 :
                return False
    return True


###################  입력
n=int(input())
area_list =[[0]*n for _ in range(n)]
for i in range(n):
    temp_list = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        area_list[i][j] = temp_list[j]
##################



##################   main
final_count =[]

for i in range(1, 100):
    flag=[[False]*n for _ in range(n)]
    water_height(i)
    count =0
    for j in range(n):
        for k in range(n):
            if flag[j][k] ==False and area_list[j][k] != 0:
                dfs(j,k,flag,0)
                count +=1
    final_count.append(count)
    if water_full():
        break
##################



print(max(final_count))