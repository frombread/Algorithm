def dfs(start,idx,flag,cost,depth):
    global cost_value
    global n

    flag[idx] =True


    if depth == n-1:
        if cost_value[idx][start] !=0:
            cost_list.append(cost+cost_value[idx][start])
        return

    for i in range(n):
        if flag[i] == False and cost_value[idx][i] != 0:
            dfs(start,i,flag,cost+cost_value[idx][i],depth+1)
            flag[i]=False
    
n=int(input())
cost_value=[[0]*n for _ in range(n)]
for i in range(n):
    temp_list = list(map(int, input().split()))
    for j in range(n):
        cost_value[i][j]=temp_list[j]
        
cost_list =[]


for i in range(n):
    flag = [False] * n
    dfs(i,i,flag,0,0)

print(min(cost_list))