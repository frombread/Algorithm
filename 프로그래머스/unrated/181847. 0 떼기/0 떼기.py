def solution(n_str):
    answer = ''
    true_0 = False
    for i in n_str:
        if int(i)!=0:
            true_0 =True
        if true_0:           
            answer+=i
            
    return answer