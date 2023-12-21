def solution(my_string):
    list_ = list(my_string)
    stk =[]
    for i in list_:
        if i not in stk:
            stk.append(i)
    answer = ''.join(stk)
    return answer