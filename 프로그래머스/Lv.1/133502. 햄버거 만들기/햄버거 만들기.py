from collections import deque
def solution(ingredient):
    answer = 0
    q= deque(ingredient)
    ham_list= []
    check_list =[]
    while q:
        elm = q.popleft()
        ham_list.append(elm)
        
        if len(ham_list)>=4:          
            fir = ham_list.pop()    
            sec = ham_list.pop()
            thr = ham_list.pop()
            fou = ham_list.pop()
            if fir == 1 and sec == 3 and thr ==2 and fou ==1:
                answer+=1
            else:
                ham_list.append(fou)
                ham_list.append(thr)
                ham_list.append(sec)
                ham_list.append(fir)            
                
    return answer