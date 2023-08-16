n = int(input())
n_list =list(map(int, input().split()))
m = int(input())
m_list =list(map(int, input().split()))

n_list.sort()

res =[0]*m
for i in range(m):
    pl = 0
    pr = n
    while pl < pr:
        mid = (pr + pl)//2
        if n_list[mid] == m_list[i]:
            res[i]=1
            break
        if m_list[i] < n_list[mid]:
            pr = mid
        elif m_list[i] >= n_list[mid]:
            pl = mid+1

for i in res:
    print(i,end=' ')
