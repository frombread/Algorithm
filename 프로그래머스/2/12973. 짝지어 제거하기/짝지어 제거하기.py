def solution(s):
    answer = 0
    s = list(s)
    stc_list =[]
    for _ in range(len(s)):
        pop_elm =s.pop()
        if stc_list:
            if stc_list[-1] !=pop_elm:
                stc_list.append(pop_elm)
            else:
                stc_list.pop()
        else:
            stc_list.append(pop_elm)
    if len(stc_list)==0:
        answer =1
    return answer