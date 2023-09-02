def solution(s):
    answer = True
    string_list = list(s)
    cnt =0
    for i in s:
        if i == "p" or i == "P":
            cnt +=1
        elif i=="y" or i =="Y":
            cnt -=1
    if cnt ==0:
        answer =True
    else:
        answer =False
    
    return answer