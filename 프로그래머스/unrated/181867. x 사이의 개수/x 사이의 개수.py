def solution(myString):
    answer = []
    num=0
    for i in myString:
        if i !="x":
            num +=1
        else:
            answer.append(num)
            num=0
    answer.append(num)
    return answer