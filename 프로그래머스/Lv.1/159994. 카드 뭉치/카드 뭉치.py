def solution(cards1, cards2, goal):
    p_1=0
    p_2=0
    goal_point = 0
    while goal_point != len(goal):
        if goal[goal_point] != cards1[p_1] and goal[goal_point] != cards2[p_2]:
            return "No"
        if goal[goal_point] == cards1[p_1] and p_1 <len(cards1)-1:
            p_1+=1
        if goal[goal_point] == cards2[p_2] and p_2 <len(cards2)-1:
            p_2+=1
        goal_point+=1
    return 'Yes'