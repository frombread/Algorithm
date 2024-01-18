def solution(lottos, win_nums):
    answer=[]
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt+=1
            
    def rank(num):
        rank = [6,5,4,3,2]
        if cnt<=1:
            answer.append(6)
        for i in range(len(rank)):
            if rank[i] ==cnt:
                answer.append(i+1)
        return 
    rank(cnt)
    cnt = cnt+lottos.count(0)
    rank(cnt)
    answer.sort()
    return answer