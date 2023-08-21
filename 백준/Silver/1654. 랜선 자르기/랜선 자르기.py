k, n =map(int,input().split())
k_list =[]
for _ in range(k):
    k_list.append(int(input()))

k_list.sort()
pl = 1
pr = k_list[-1]
last_list =[]
while pl <= pr:
    cnt =0
    mid =(pr+pl)//2
    for i in k_list:
        cnt += i//mid
    if cnt < n:
        pr = mid-1
    elif cnt >= n:
        pl = mid+1
print(pr)