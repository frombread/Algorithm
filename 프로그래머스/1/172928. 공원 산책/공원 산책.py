from collections import deque
def solution(park, routes):
    
    route_list = deque(routes)
    
    stone_list=[]
    start_point=[0,0]
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                start_point =[i,j]
            if park[i][j] =='X':
                stone_list.append([i,j])
                
                
                
    while route_list:
        route = route_list.popleft()
        way, dis = route.split(' ')
        dx,dy =start_point
        can_move =True
        for _ in range(int(dis)):
            if way =='N':
                dx-=1
            elif way=='S':
                dx+=1
            elif way =='W':
                dy-=1
            else:
                dy+=1
            if not (0 <= dx < len(park) and 0 <= dy < len(park[0])):
                can_move = False
                break
            if [dx, dy] in stone_list:
                can_move = False
                break
        if can_move:
            start_point = [dx, dy]
    
    print(start_point)
        
    return start_point