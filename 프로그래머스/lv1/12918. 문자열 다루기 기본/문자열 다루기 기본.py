def solution(s):
    answer = True
    num_list =["1","2","3","4","5","6","7","8","9","0"]
    f = len(list(s))
    if (f == 4) or (f == 6):
        for i in s:
            if i not in num_list:
                return False
    else:
        return False
            
    return answer