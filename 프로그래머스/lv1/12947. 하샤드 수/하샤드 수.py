def solution(x):
    answer = True
    a = 0
    str_x = list(str(x))
    for i in str_x:
        a += int(i)
        
    if x%a == 0:
        print(a,x, a%x)
        answer =True
    else:
        answer =False
    return answer