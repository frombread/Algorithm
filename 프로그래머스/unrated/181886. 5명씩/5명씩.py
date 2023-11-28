def solution(names):
    answer = []
    i=1
    while i<= len(names):
        answer.append(names[i-1])
        i+=5
    return answer