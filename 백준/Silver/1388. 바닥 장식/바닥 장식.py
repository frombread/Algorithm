n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(input()))
row=0
column =0
for i in range(n):
    stk_list =[]
    for j in range(m):
        if len(stk_list) ==0 and graph[i][j] =='-':
            row +=1
        elif len(stk_list) != 0 and graph[i][j] != stk_list[-1] and graph[i][j] =="-":
            row +=1
        stk_list.append(graph[i][j])
    
for i in range(m):
    stk_list=[]
    for j in range(n):
        if len(stk_list)== 0 and graph[j][i] !='-':
            column +=1
        elif len(stk_list) != 0 and graph[j][i] != stk_list[-1] and graph[j][i] !="-":
            column +=1
        stk_list.append(graph[j][i])

print(row+column)