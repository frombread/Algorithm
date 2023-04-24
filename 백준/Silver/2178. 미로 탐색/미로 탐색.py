from collections import deque

miro =[]

n,m = map(int,input().split())

for i in range(n):
    miro.append(list(map(int, input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q= deque([(0,0)])
while q:
    x, y=q.popleft()
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0 <= next_x and 0<=next_y and next_x <n and next_y<m and miro[next_x][next_y] ==1:
            q.append([next_x,next_y])
            miro[next_x][next_y] = miro[x][y] +1

print(miro[n-1][m-1])
