def solution(a, b):
    var = str(a) + str(b)
    var_2 = str(b) + str(a)
    list_=[]
    list_.append(int(var))
    list_.append(int(var_2))
    
    return max(list_)