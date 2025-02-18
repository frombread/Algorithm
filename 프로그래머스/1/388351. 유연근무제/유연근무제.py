def solution(schedules, timelogs, startday):
    reward_cnt = 0
    for schedule, timelog in zip(schedules,timelogs):
        pass_time = (schedule//100 *60) + (schedule % 100) +10
        day = startday
        pass_ = True
        for time in timelog:
            time_ = (time//100 *60) + time % 100
            if day>=8:
                day=1
            if day == 6 or day== 7:
                day+=1
                continue
            if pass_time < time_:
                pass_= False
            day+=1
        if pass_ == True:
            reward_cnt+=1
    return reward_cnt