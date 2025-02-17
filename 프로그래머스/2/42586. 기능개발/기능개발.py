from collections import deque
def solution(progresses, speeds):
    progress_dq = deque(progresses)
    speeds_dq = deque(speeds)
    result_list=[]
    for _ in range(len(progresses)):
        max_days = 100
        progress = progress_dq.popleft()
        speed = speeds_dq.popleft()
        days = 100-progress
        day_count=0
        while True:
            day_count+=1
            if days <=0:
                break
            days= days-speed
        result_list.append(day_count-1)
            
    print(result_list)
    answer =[]
    result_dq = deque(result_list)
    while True:
        if len(result_dq)==0:
            break
        el = result_dq.popleft()
        count=1
        while result_dq and result_dq[0] <= el:
            result_dq.popleft()
            count += 1
            
        answer.append(count)
    return answer