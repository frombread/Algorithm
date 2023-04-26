import sys
from collections import defaultdict
input= sys.stdin.readline

n,m = map(int,input().split())
heavy = defaultdict(list)
light = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    light[a].append(b)
    heavy[b].append(a)

count = 0
def dfs(idx,list):
    global count
    flag[idx]=True
    for i in list[idx]:
        if flag[i] ==False:
            count+=1
            dfs(i,list)

ans=0
mid = (n+1)//2
for i in range(1,n+1):
    flag=[True]+[False]*n
    count=0
    dfs(i,heavy)
    if count>=mid:
        ans+=1
    
    count =0
    dfs(i,light)
    if count>=mid:
        ans+=1
    
print(ans)

    