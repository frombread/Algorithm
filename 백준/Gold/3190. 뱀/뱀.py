from collections import deque
n = int(input())
apple =int(input())

apple_list=[list(map(int,input().split()))for _ in range(apple)]

move_s= int(input())
move_list = list([input().split() for _ in range(move_s)])

q = deque()
q.append([1,1])
time=0
dir_idx= 0
move_idx =0
dx =[0,1,0,-1]
dy =[1,0,-1,0]
while True:
    time+=1
    x,y = q[-1]
    next_x = x+dx[dir_idx]
    next_y = y+dy[dir_idx]

    if [next_x,next_y] in q:
        break

    if next_x >n or next_y >n or next_x < 1 or next_y <1:
        break

    if [next_x,next_y] in apple_list:
        q.append([next_x,next_y])
        apple_list.remove([next_x,next_y])
    else:
        q.popleft()
        q.append([next_x,next_y])

    if time == int(move_list[move_idx][0]):
        if move_list[move_idx][1] == 'D':
            dir_idx = (dir_idx +1)%4
        else:
            dir_idx = (dir_idx-1)%4
        if move_idx < len(move_list) -1:
            move_idx+=1
    
print(time)