def DFS(idx,sum_num):
    global count

    if idx == n:
        return
    if sum_num + start_list[idx] ==fin_num:
        count +=1

    DFS(idx+1,sum_num)

    DFS(idx+1,sum_num + start_list[idx])
    
    
count =0

n,fin_num= map(int,input().split())
start_list = list(map(int,input().split()))
DFS(0,0)
print(count)