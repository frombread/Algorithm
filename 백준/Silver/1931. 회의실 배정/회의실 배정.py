from collections import deque
n = int(input())
q=deque()
time_list =[]
for _ in range(n):
    a,b = map(int,input().split())
    time_list.append([a,b])
time_list.sort(key=lambda x : (x[1],x[0]))

end_time=0
cnt=0
for start,end in time_list:
    if start >=end_time:
        cnt+=1
        end_time = end
print(cnt)