def solution(s):
    cnt,cnt2,answer=0,0,0
    first_str = s[0]

    for i in range(0,len(s)-1):
        if s[i] == first_str:
            cnt +=1
        else:
           cnt2 +=1
        if cnt == cnt2:
            cnt,cnt2 = 0,0
            first_str = s[i+1]
            answer +=1 

    answer+=1
    return answer


