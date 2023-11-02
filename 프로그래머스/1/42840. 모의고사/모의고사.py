def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 =[2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    res_list =[0,0,0]
    for i in range(len(answers)):
        a = i % len(num1)
        b = i % len(num2)
        c = i % len(num3)
        if answers[i] == num1[a]:
            res_list[0] +=1
        if answers[i] == num2[b]:
            res_list[1] +=1
        if answers[i] == num3[c]:
            res_list[2] +=1
    
    max_num = max(res_list)
    
    for i in range(3):
        if max_num == res_list[i]:
            answer.append(i+1)
    
        

    return answer