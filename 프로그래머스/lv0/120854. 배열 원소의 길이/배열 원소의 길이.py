def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(list(i)))
    return answer