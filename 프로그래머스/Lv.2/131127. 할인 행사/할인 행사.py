def solution(want, number, discount):
    answer = 0
    cnt = 0
        
    while cnt <len(discount)-9:
        num_copy =[]
        for i in number:
            num_copy.append(i)
            
        for i in range(len(want)):
            for j in range(cnt,cnt+10):
                if j >len(discount)-1:
                    break
                if want[i]==discount[j]:
                    num_copy[i]-=1
                    if num_copy[i] ==0:
                        break
    
        if sum(num_copy) == 0:
            answer+=1
        cnt+=1            
            
    return answer